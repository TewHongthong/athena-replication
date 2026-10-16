#!/usr/bin/env python3
"""tree-sitter based extractors for Java, C#, TypeScript(+TSX) and JavaScript(+JSX)."""
from __future__ import annotations

import re

from facts import (Decl, FileFacts, Tok, UnitCand, line_starts_of, line_of,
                   DECL, REF, MEMBER, TYPE, KEY, KWARG, SHORTHAND, IMPORT, OTHER)

_UPPER = re.compile(r"_?[A-Z][A-Z0-9_]*$")

IDENT_TYPES = {
    "java": {"identifier", "type_identifier"},
    "csharp": {"identifier"},
    "typescript": {"identifier", "type_identifier", "property_identifier", "shorthand_property_identifier",
                   "shorthand_property_identifier_pattern", "private_property_identifier"},
    "javascript": {"identifier", "property_identifier", "shorthand_property_identifier",
                   "shorthand_property_identifier_pattern", "private_property_identifier"},
}
IDENT_TYPES["tsx"] = IDENT_TYPES["typescript"]
COMMENT_TYPES = {"comment", "line_comment", "block_comment"}
STRING_TYPES = {
    "java": {"string_literal", "text_block", "character_literal"},
    "csharp": {"string_literal_content", "interpolated_string_text", "verbatim_string_literal",
               "raw_string_content", "character_literal", "string_literal"},
    "typescript": {"string_fragment", "regex_pattern"},
    "javascript": {"string_fragment", "regex_pattern"},
}
STRING_TYPES["tsx"] = STRING_TYPES["typescript"]


def grammar_for(lang: str, path: str) -> str:
    if lang == "typescript":
        return "tsx" if path.lower().endswith(".tsx") else "typescript"
    return lang


class Ctx:
    """Per-file working state shared by the visitors."""

    def __init__(self, lang, src, ts_lang, root):
        self.lang = lang
        self.src = src
        self.root = root
        self.tokmap = {}
        self.decls = []
        self.units = []
        self.ls = line_starts_of(src)

    def text(self, n):
        return self.src[n.start:n.end].decode("utf-8", errors="replace")

    def decl(self, name_node, kind, ns, exempt=None, **extra):
        if name_node is None:
            return None
        name = self.text(name_node)
        tk = self.tokmap.get(name_node.start)
        if tk is not None and tk.role != IMPORT:
            tk.role = DECL
        d = Decl(name, kind, name_node.start, name_node.end, ns, exempt, extra)
        self.decls.append(d)
        return d

    def add_unit(self, node, label, top_level):
        s = line_of(self.ls, node.start)
        e = line_of(self.ls, max(node.end - 1, node.start))
        self.units.append(UnitCand(s, e, label, top_level))


def _has_child_type(n, types):
    return any(c.type in types for c in n.children)


def _mod_words(n, src):
    """Words of the modifier tokens attached to declaration node `n` (Java/C#/TS)."""
    words = []
    for c in n.children:
        if c.type in ("modifiers",):
            words += src[c.start:c.end].decode("utf-8", "replace").replace("\n", " ").split()
        elif c.type == "modifier":
            words.append(src[c.start:c.end].decode("utf-8", "replace"))
        elif c.type in ("accessibility_modifier", "override_modifier") or (not c.named and c.type in (
                "static", "readonly", "abstract", "async", "get", "set", "const", "final", "public", "private",
                "protected", "declare")):
            words.append(c.type if not c.named else src[c.start:c.end].decode("utf-8", "replace"))
    return words


# ----------------------------------------------------------------------------- token roles

def _classify_tokens(cx: Ctx):
    lang = cx.lang
    idt = IDENT_TYPES[lang]
    for n in cx.root.walk():
        if n.type not in idt:
            continue
        p = n.parent
        role = REF
        t = n.type
        pt = p.type if p else ""
        if lang == "java":
            if t == "type_identifier":
                role = TYPE
            elif pt in ("scoped_identifier", "import_declaration", "package_declaration"):
                role = IMPORT
            elif pt == "field_access" and n.field == "field":
                role = MEMBER
            elif pt == "method_invocation" and n.field == "name":
                role = MEMBER if p.child("object") is not None else REF
            elif pt == "method_reference":
                role = MEMBER if n is p.children[-1] else REF
            elif pt in ("marker_annotation", "annotation") and n.field == "name":
                role = TYPE
            elif pt == "element_value_pair" and n.field == "key":
                role = KEY
            elif pt in ("labeled_statement", "break_statement", "continue_statement"):
                role = OTHER
        elif lang == "csharp":
            if pt in ("qualified_name", "using_directive", "namespace_declaration", "file_scoped_namespace_declaration"):
                role = IMPORT
            elif pt == "member_access_expression" and n.field == "name":
                role = MEMBER
            elif pt == "member_binding_expression":
                role = MEMBER
            elif pt == "name_colon":
                role = KWARG
            elif pt == "assignment_expression" and n.field == "left" and p.parent is not None \
                    and p.parent.type == "initializer_expression":
                role = MEMBER
            elif pt in ("type_argument_list", "base_list", "nullable_type", "array_type", "attribute",
                        "type_constraint", "type_parameter_constraint", "typeof_expression",
                        "primary_constructor_base_type", "tuple_element") or n.field in ("type", "returns"):
                role = TYPE
            elif pt == "generic_name" and n is p.children[0]:
                role = TYPE
        else:  # typescript / javascript
            if t == "type_identifier":
                role = TYPE
            elif t in ("shorthand_property_identifier", "shorthand_property_identifier_pattern"):
                role = SHORTHAND
            elif t in ("property_identifier", "private_property_identifier"):
                if pt == "member_expression" and n.field == "property":
                    role = MEMBER
                elif pt == "pair" and n.field == "key":
                    role = KEY
                elif pt in ("jsx_attribute",):
                    role = KEY
                else:
                    role = MEMBER       # member declaration position (method/field/property names)
            elif pt in ("import_specifier", "import_clause", "namespace_import", "export_specifier",
                        "import_statement", "import_require_clause", "import_alias"):
                role = IMPORT
            elif pt in ("jsx_opening_element", "jsx_closing_element", "jsx_self_closing_element") and n.field == "name":
                role = TYPE
            elif pt in ("labeled_statement", "break_statement", "continue_statement"):
                role = OTHER
            elif pt == "nested_identifier" or pt == "nested_type_identifier":
                role = TYPE
        cx.tokmap[n.start] = Tok(n.start, n.end, cx.text(n), role, t)


# ----------------------------------------------------------------------------- Java

_JAVA_CONST_TYPES = {"String", "Integer", "Long", "Double", "Float", "Short", "Byte", "Boolean", "Character"}
_JAVA_PRIM = {"integral_type", "floating_point_type", "boolean_type"}


def _java(cx: Ctx):
    src = cx.src

    def type_is_const_like(tn):
        if tn is None:
            return False
        if tn.type in _JAVA_PRIM:
            return True
        return tn.type == "type_identifier" and cx.text(tn) in _JAVA_CONST_TYPES

    def params(fp, exempt=None):
        if fp is None:
            return
        for c in fp.children:
            if c.type == "formal_parameter":
                cx.decl(c.child("name"), "parameter", "local", exempt)
            elif c.type == "spread_parameter":
                for d in c.children:
                    if d.type == "variable_declarator":
                        cx.decl(d.child("name"), "parameter", "local", exempt)

    def annotations(n):
        names = set()
        for c in n.children:
            if c.type == "modifiers":
                for a in c.children:
                    if a.type in ("marker_annotation", "annotation"):
                        nm = a.child("name")
                        if nm is not None:
                            names.add(cx.text(nm))
        return names

    def visit(n, where, cls=None):
        t = n.type
        if t in ("class_declaration", "record_declaration", "interface_declaration", "enum_declaration"):
            nm = n.child("name")
            kind = {"class_declaration": "class", "record_declaration": "class",
                    "interface_declaration": "interface", "enum_declaration": "enum"}[t]
            cx.decl(nm, kind, "type", None)
            cname = cx.text(nm) if nm is not None else "?"
            if t == "record_declaration":
                params(n.child("parameters"), "record_component")
            body = n.child("body")
            if body is not None:
                for m in body.children:
                    if t == "enum_declaration":
                        if m.type == "enum_constant":
                            cx.decl(m.child("name"), "enum_member", "member", None)
                            for ch in m.children:
                                visit(ch, "class", cname)
                            continue
                        if m.type == "enum_body_declarations":
                            for mm in m.children:
                                visit_member(mm, "class", cname)
                            continue
                    visit_member(m, "interface" if t == "interface_declaration" else "class", cname)
            return
        for c in n.children:
            visit(c, where, cls)

    def visit_member(m, where, cname):
        t = m.type
        if t in ("class_declaration", "record_declaration", "interface_declaration", "enum_declaration"):
            nm = m.child("name")
            cx.add_unit(m, f"{'class' if t != 'interface_declaration' else 'interface'} {cx.text(nm) if nm is not None else '?'}", False)
            visit(m, where, cname)
        elif t == "method_declaration":
            nm = m.child("name")
            ann = annotations(m)
            ex = "test_method" if ann & {"Test", "ParameterizedTest", "RepeatedTest", "TestFactory"} else None
            cx.decl(nm, "method", "member", ex)
            cx.add_unit(m, f"method {cname}.{cx.text(nm) if nm is not None else '?'}", False)
            params(m.child("parameters"))
            body = m.child("body")
            if body is not None:
                body_visit(body)
        elif t in ("constructor_declaration", "compact_constructor_declaration"):
            nm = m.child("name")
            params(m.child("parameters"))
            cx.add_unit(m, f"constructor {cname}", False)
            body = m.child("body")
            if body is not None:
                body_visit(body)
        elif t in ("field_declaration", "constant_declaration"):
            mods = _mod_words(m, src)
            tn = m.child("type")
            in_iface = where == "interface"
            is_static = "static" in mods
            is_final = "final" in mods
            for d in m.children_of("declarator"):
                nm = d.child("name")
                if t == "constant_declaration" or in_iface or (is_static and is_final):
                    if type_is_const_like(tn):
                        cx.decl(nm, "constant", "member", None)
                    else:
                        cx.decl(nm, "constant", "member", "ambiguous_constant")
                else:
                    cx.decl(nm, "field", "member", None)
                v = d.child("value")
                if v is not None:
                    body_visit(v)
        elif t in ("static_initializer", "block", "initializer"):
            body_visit(m)

    def body_visit(n):
        t = n.type
        if t == "local_variable_declaration":
            for d in n.children_of("declarator"):
                cx.decl(d.child("name"), "variable", "local", None)
        elif t == "enhanced_for_statement":
            cx.decl(n.child("name"), "variable", "local", None)
        elif t == "catch_formal_parameter":
            cx.decl(n.child("name"), "variable", "local", None)
        elif t == "resource":
            cx.decl(n.child("name"), "variable", "local", None)
        elif t == "lambda_expression":
            p = n.child("parameters")
            if p is not None:
                if p.type == "identifier":
                    cx.decl(p, "parameter", "local", "lambda_param")
                elif p.type == "inferred_parameters":
                    for c in p.children:
                        if c.type == "identifier":
                            cx.decl(c, "parameter", "local", "lambda_param")
                else:
                    params(p, "lambda_param")
        elif t in ("class_declaration", "record_declaration", "interface_declaration", "enum_declaration"):
            visit(n, "class")
            return
        elif t == "class_body":  # anonymous class body
            for m in n.children:
                visit_member(m, "class", "anonymous")
            return
        for c in n.children:
            body_visit(c)

    for top in cx.root.children:
        if top.type in ("class_declaration", "record_declaration", "interface_declaration", "enum_declaration"):
            nm = top.child("name")
            kind_word = "interface" if top.type == "interface_declaration" else "class"
            cx.add_unit(top, f"{kind_word} {cx.text(nm) if nm is not None else '?'}", True)
            visit(top, "top")
        else:
            visit(top, "top")


# ----------------------------------------------------------------------------- C#

_CS_TYPE_DECLS = {"class_declaration": "class", "struct_declaration": "class", "record_declaration": "class",
                  "record_struct_declaration": "class", "interface_declaration": "interface",
                  "enum_declaration": "enum"}


def _cs_is_bool(cx, tn):
    if tn is None:
        return False
    t = cx.text(tn).strip()
    return t in ("bool", "bool?", "Boolean", "Boolean?", "System.Boolean")


def _csharp(cx: Ctx):
    src = cx.src

    def params(pl, exempt=None):
        if pl is None:
            return
        for c in pl.children:
            if c.type == "parameter":
                cx.decl(c.child("name"), "parameter", "local", exempt)

    def type_decl(n, top, container):
        t = n.type
        nm = n.child("name")
        name = cx.text(nm) if nm is not None else "?"
        cx.decl(nm, _CS_TYPE_DECLS[t], "type", None)
        cx.add_unit(n, f"{'interface' if t == 'interface_declaration' else 'class'} {name}", top)
        if t in ("record_declaration", "record_struct_declaration"):
            for c in n.children:
                if c.type == "parameter_list":
                    params(c, "record_component")
        body = n.child("body")
        if body is None:
            return
        for m in body.children:
            member(m, t, name)

    def member(m, owner_t, owner):
        t = m.type
        mods = _mod_words(m, src)
        if t in _CS_TYPE_DECLS:
            type_decl(m, False, owner)
        elif t == "enum_member_declaration":
            cx.decl(m.child("name"), "enum_member", "member", None)
        elif t == "method_declaration":
            nm = m.child("name")
            ex = "explicit_interface" if _has_child_type(m, ("explicit_interface_specifier",)) else None
            cx.decl(nm, "method", "member", ex)
            cx.add_unit(m, f"method {owner}.{cx.text(nm) if nm is not None else '?'}", False)
            params(m.child("parameters"))
            b = m.child("body")
            if b is not None:
                body_visit(b)
        elif t == "constructor_declaration":
            params(m.child("parameters"))
            cx.add_unit(m, f"constructor {owner}", False)
            b = m.child("body")
            if b is not None:
                body_visit(b)
        elif t == "property_declaration":
            nm = m.child("name")
            tn = m.child("type")
            ex = "explicit_interface" if _has_child_type(m, ("explicit_interface_specifier",)) else None
            if _cs_is_bool(cx, tn):
                cx.decl(nm, "boolean_variable", "member", ex, base_kind="property")
            else:
                cx.decl(nm, "property", "member", ex)
            body = m.child("value") or m.child("accessors")
            if body is not None:
                body_visit(body)
        elif t == "indexer_declaration":
            for c in m.children:
                if c.type == "bracketed_parameter_list":
                    params(c)
        elif t == "field_declaration":
            vd = None
            for c in m.children:
                if c.type == "variable_declaration":
                    vd = c
            if vd is None:
                return
            tn = vd.child("type")
            is_const = "const" in mods
            public = ("public" in mods) or ("protected" in mods)
            for d in vd.children:
                if d.type != "variable_declarator":
                    continue
                nm = d.child("name")
                if is_const:
                    cx.decl(nm, "constant", "member", None)
                elif public:
                    if _cs_is_bool(cx, tn):
                        cx.decl(nm, "boolean_variable", "member", None, base_kind="field")
                    else:
                        cx.decl(nm, "field", "member", None)
                else:
                    cx.decl(nm, "field", "member", "nonpublic_field")
                for ch in d.children:
                    if ch.named and ch is not nm:
                        body_visit(ch)
        elif t in ("event_field_declaration", "event_declaration", "delegate_declaration",
                   "operator_declaration", "conversion_operator_declaration", "destructor_declaration"):
            for c in m.children:
                body_visit(c)
        elif t == "declaration_list":
            for c in m.children:
                member(c, owner_t, owner)
        else:
            for c in m.children:
                body_visit(c)

    def body_visit(n):
        t = n.type
        if t == "variable_declaration" and n.parent is not None and n.parent.type in (
                "local_declaration_statement", "using_statement", "for_statement", "fixed_statement"):
            mods = _mod_words(n.parent, src) if n.parent.type == "local_declaration_statement" else []
            tn = n.child("type")
            for d in n.children:
                if d.type != "variable_declarator":
                    continue
                nm = d.child("name")
                if "const" in mods:
                    cx.decl(nm, "constant", "local", None)
                elif _cs_is_bool(cx, tn):
                    cx.decl(nm, "boolean_variable", "local", None, base_kind="variable")
                else:
                    cx.decl(nm, "variable", "local", None)
        elif t == "foreach_statement":
            left = n.child("left")
            if left is not None and left.type == "identifier":
                cx.decl(left, "variable", "local", None)
        elif t == "catch_declaration":
            cx.decl(n.child("name"), "variable", "local", None)
        elif t == "declaration_pattern":
            cx.decl(n.child("name"), "variable", "local", "pattern_var")
        elif t == "declaration_expression":
            cx.decl(n.child("name"), "variable", "local", "out_var")
        elif t == "local_function_statement":
            cx.decl(n.child("name"), "method", "member", "local_function")
            params(n.child("parameters"))
        elif t in ("lambda_expression", "anonymous_method_expression"):
            p = n.child("parameters")
            if p is not None:
                if p.type == "implicit_parameter":
                    cx.decl(p, "parameter", "local", "lambda_param")
                elif p.type == "parameter_list":
                    params(p, "lambda_param")
        for c in n.children:
            body_visit(c)

    def walk_top(n):
        if n.type in _CS_TYPE_DECLS:
            type_decl(n, True, None)
        elif n.type in ("namespace_declaration",):
            b = n.child("body")
            if b is not None:
                for c in b.children:
                    walk_top(c)
        elif n.type in ("compilation_unit", "file_scoped_namespace_declaration", "declaration_list"):
            for c in n.children:
                walk_top(c)
        # using directives / global statements ignored

    walk_top(cx.root)


# ----------------------------------------------------------------------------- TypeScript / JavaScript

_FUNC_VALUES = {"arrow_function", "function_expression", "function", "generator_function"}
_JSX_TYPES = {"jsx_element", "jsx_self_closing_element", "jsx_fragment"}


def _contains_jsx(n):
    for c in n.walk():
        if c.type in _JSX_TYPES:
            return True
    return False


def _tsjs(cx: Ctx):
    src = cx.src
    is_ts = cx.lang in ("typescript", "tsx")

    def params(fp, exempt=None):
        if fp is None:
            return
        if fp.type in ("identifier",):
            cx.decl(fp, "parameter", "local", "underscore" if cx.text(fp) == "_" else exempt)
            return
        for c in fp.children:
            t = c.type
            if t in ("required_parameter", "optional_parameter"):
                pat = c.child("pattern")
                mods = [x.type for x in c.children]
                if pat is not None and pat.type == "identifier":
                    ex = exempt
                    if "accessibility_modifier" in mods or "readonly" in mods:
                        ex = "param_property"
                    elif pat.type == "identifier" and cx.text(pat) == "this":
                        ex = "this_param"
                    elif cx.text(pat) == "_":
                        ex = "underscore"
                    cx.decl(pat, "parameter", "local", ex)
                elif pat is not None and pat.type == "rest_pattern":
                    for x in pat.children:
                        if x.type == "identifier":
                            cx.decl(x, "parameter", "local", exempt)
            elif t == "identifier":
                cx.decl(c, "parameter", "local", "underscore" if cx.text(c) == "_" else exempt)
            elif t == "assignment_pattern":
                left = c.child("left")
                if left is not None and left.type == "identifier":
                    cx.decl(left, "parameter", "local", exempt)
                right = c.child("right")
                if right is not None:
                    walk(right, "function")
            elif t == "rest_pattern":
                for x in c.children:
                    if x.type == "identifier":
                        cx.decl(x, "parameter", "local", exempt)

    def is_function_valued(v):
        return v is not None and v.type in _FUNC_VALUES

    def name_exempt_component(name, node):
        return name[:1].isupper() and cx.lang in ("tsx", "javascript") and _contains_jsx(node)

    def class_like(n, where, exported):
        nm = n.child("name")
        cx.decl(nm, "class", "type", None, exported=exported)
        cname = cx.text(nm) if nm is not None else "?"
        body = n.child("body")
        if body is None:
            return
        for m in body.children:
            member(m, cname, exported)

    def member(m, cname, exported, make_unit=True):
        t = m.type
        if t == "field_definition":  # javascript class field
            nm = m.child("property")
            if nm is not None:
                if nm.type == "private_property_identifier":
                    cx.decl(nm, "field", "member", "private_hash")
                else:
                    cx.decl(nm, "field", "member", None)
            v = m.child("value")
            if v is not None:
                walk(v, "function")
        elif t == "public_field_definition":  # typescript class field
            nm = m.child("name")
            mods = [x.type for x in m.children]
            if nm is None:
                return
            if nm.type == "property_identifier":
                if "static" in mods and "readonly" in mods:
                    cx.decl(nm, "constant", "member", None)
                else:
                    cx.decl(nm, "field", "member", None)
            elif nm.type == "private_property_identifier":
                cx.decl(nm, "field", "member", None)
            v = m.child("value")
            if v is not None:
                walk(v, "function")
        elif t == "method_definition":
            nm = m.child("name")
            words = [x.type for x in m.children]
            if nm is not None:
                nt = cx.text(nm)
                if nm.type not in ("property_identifier", "private_property_identifier"):
                    ex = "computed_name"
                elif nt == "constructor":
                    ex = "constructor"
                elif "get" in words or "set" in words:
                    ex = "accessor"
                elif nm.type == "private_property_identifier":
                    ex = "private_hash"
                else:
                    ex = None
                if ex != "constructor" and nm.type in ("property_identifier", "private_property_identifier"):
                    cx.decl(nm, "method", "member", ex)
                if make_unit:
                    cx.add_unit(m, f"method {cname}.{nt}", False)
            params(m.child("parameters"))
            b = m.child("body")
            if b is not None:
                walk(b, "function")
        elif t in ("class_static_block",):
            walk(m, "function")
        else:
            walk(m, "class")

    def declarators(n, where, exported):
        is_const = any(c.type == "const" for c in n.children)
        for d in n.children:
            if d.type != "variable_declarator":
                continue
            nm = d.child("name")
            v = d.child("value")
            if nm is None:
                continue
            if nm.type == "identifier":
                name = cx.text(nm)
                if is_function_valued(v):
                    ex = "react_component" if name_exempt_component(name, v) else None
                    cx.decl(nm, "function", "type", ex, exported=exported)
                elif where == "module" and is_const and _UPPER.match(name) and len(name.lstrip("_")) > 1:
                    cx.decl(nm, "constant", "local", None, exported=exported)
                else:
                    ex = "underscore" if name == "_" else None
                    if v is not None and v.type in ("class",) :
                        cx.decl(nm, "class", "type", None, exported=exported)
                    else:
                        cx.decl(nm, "variable", "local", ex, exported=exported)
            else:
                pass  # destructuring patterns: names are dictated by the source object -> not declared here
            if v is not None:
                walk(v, "function" if is_function_valued(v) else where)

    def walk(n, where, exported=False):
        t = n.type
        if t == "export_statement":
            for c in n.children:
                if c.type in ("class_declaration", "abstract_class_declaration", "function_declaration",
                              "generator_function_declaration", "interface_declaration", "enum_declaration",
                              "lexical_declaration", "variable_declaration", "type_alias_declaration",
                              "internal_module", "module"):
                    walk(c, where, True)
                elif c.named and c.field in ("value",):
                    walk(c, where, True)
            return
        if t in ("class_declaration", "abstract_class_declaration", "class"):
            if t == "class" and n.child("name") is None:
                for c in n.children:
                    if c.type == "class_body":
                        for m in c.children:
                            member(m, "anonymous", exported)
                return
            class_like(n, where, exported)
            return
        if t == "interface_declaration":
            cx.decl(n.child("name"), "interface", "type", None, exported=exported)
            body = n.child("body")
            if body is not None:
                for m in body.children:
                    if m.type == "property_signature":
                        nm = m.child("name")
                        if nm is not None and nm.type == "property_identifier":
                            cx.decl(nm, "property", "member", None)
                        elif nm is not None:
                            pass
                    elif m.type == "method_signature":
                        nm = m.child("name")
                        if nm is not None and nm.type == "property_identifier":
                            cx.decl(nm, "method", "member", None)
                        params(m.child("parameters"))
            return
        if t == "enum_declaration":
            cx.decl(n.child("name"), "enum", "type", None, exported=exported)
            body = n.child("body")
            if body is not None:
                for m in body.children:
                    if m.type == "property_identifier":
                        cx.decl(m, "enum_member", "member", None)
                    elif m.type == "enum_assignment":
                        cx.decl(m.child("name"), "enum_member", "member", None)
            return
        if t in ("function_declaration", "generator_function_declaration"):
            nm = n.child("name")
            if nm is not None:
                name = cx.text(nm)
                ex = "react_component" if name_exempt_component(name, n) else None
                cx.decl(nm, "function", "type", ex, exported=exported)
            params(n.child("parameters"))
            b = n.child("body")
            if b is not None:
                walk(b, "function")
            return
        if t in ("arrow_function", "function_expression", "function", "generator_function"):
            p = n.child("parameter") or n.child("parameters")
            if p is not None:
                params(p)
            b = n.child("body")
            if b is not None:
                walk(b, "function")
            return
        if t in ("lexical_declaration", "variable_declaration"):
            declarators(n, where, exported)
            return
        if t == "catch_clause":
            p = n.child("parameter")
            if p is not None and p.type == "identifier":
                cx.decl(p, "variable", "local", None)
            b = n.child("body")
            if b is not None:
                walk(b, "function")
            return
        if t in ("for_in_statement",):
            left = n.child("left")
            if left is not None and left.type == "identifier":
                cx.decl(left, "variable", "local", "underscore" if cx.text(left) == "_" else None)
            for c in n.children:
                if c.named and c is not left:
                    walk(c, "function")
            return
        if t == "assignment_expression" and not is_ts:
            left = n.child("left")
            if left is not None and left.type == "member_expression":
                obj = left.child("object")
                prop = left.child("property")
                if obj is not None and obj.type == "this" and prop is not None and prop.type == "property_identifier":
                    cx.decl(prop, "property", "member", None, via="this")
        if t == "method_definition":      # object-literal method
            member(n, "object", exported, make_unit=False)
            return
        for c in n.children:
            walk(c, where if t not in ("statement_block",) else "function", exported)

    # top-level units
    for top in cx.root.children:
        inner = top
        exported = False
        if top.type == "export_statement":
            for c in top.children:
                if c.named and c.field == "declaration":
                    inner = c
            exported = True
        it = inner.type
        label = None
        if it in ("function_declaration", "generator_function_declaration", "class_declaration",
                  "abstract_class_declaration", "interface_declaration", "enum_declaration"):
            nm = inner.child("name")
            label = f"{it.split('_')[0]} {cx.text(nm) if nm is not None else '?'}"
        elif it in ("lexical_declaration", "variable_declaration"):
            for d in inner.children:
                if d.type == "variable_declarator" and d.child("name") is not None:
                    v = d.child("value")
                    if v is not None and (v.type in _FUNC_VALUES or v.type in ("class", "object", "call_expression")):
                        label = "const " + cx.text(d.child("name"))
                        break
        if label:
            cx.add_unit(top, label, True)
        walk(top, "module")
    # class member units (methods of classes at any depth in top-level classes)
    # (added in member() via add_unit for methods)


# ----------------------------------------------------------------------------- entry point

def extract(lang: str, path: str, content: bytes, ts) -> FileFacts:
    """lang: corpus language (java|csharp|typescript|javascript); ts: TreeSitter instance."""
    g = grammar_for(lang, path)
    ls = line_starts_of(content)
    ff = FileFacts(language=lang, src=content, line_starts=ls)
    root, has_err = ts.parse(g, content)
    cx = Ctx(g if g in IDENT_TYPES else lang, content, g, root)
    cx.lang = g if g in ("tsx",) else lang
    # `IDENT_TYPES` has a tsx entry; keep lang name for logic branches
    ff.error_spans = [(n.start, n.end) for n in root.walk() if n.is_error or n.is_missing]
    ff.comment_spans = [(n.start, n.end) for n in root.walk() if n.type in COMMENT_TYPES]
    st = STRING_TYPES[g]
    ff.string_spans = [(n.start, n.end) for n in root.walk() if n.type in st]
    ff.shape = tuple(n.type for n in root.walk())

    def reverify(new_src: bytes):
        r2, err2 = ts.parse(g, new_src)
        return tuple(n.type for n in r2.walk()), err2

    ff.reverify = reverify
    ff.parse_ok = True
    _classify_tokens(cx)
    if lang == "java":
        _java(cx)
    elif lang == "csharp":
        _csharp(cx)
    else:
        _tsjs(cx)
    ff.decls = [d for d in cx.decls if d is not None]
    ff.toks = sorted(cx.tokmap.values(), key=lambda t: t.start)
    ff.units = cx.units
    return ff
