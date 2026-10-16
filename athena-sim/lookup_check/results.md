# Graph retrieval vs structured lookup — results

| set | units | distinct keys | mean rules/unit | same set | same order | same examples | identical text (live) | identical text (logged prompts) |
|---|---|---|---|---|---|---|---|---|
| gscs rename | 122 | 24 | 1.00 | 100.0% | 100.0% | 100.0% | 100.0% | test_luna_gscs_rename: 122/122 units (366 graph trials); test_o3mini_gscs_rename: 122/122 units (366 graph trials) |
| gscs comment | 12 | 6 | 1.00 | 100.0% | 100.0% | 100.0% | 100.0% | test_luna_gscs_comment: 12/12 units (36 graph trials); test_o3mini_gscs_comment: 12/12 units (36 graph trials) |
| public5 rename | 2157 | 37 | 1.61 | 100.0% | 100.0% | 100.0% | 100.0% | test_luna_p5_rename: 100/100 units (300 graph trials) |
| public5 comment | 89 | 11 | 1.22 | 100.0% | 100.0% | 100.0% | 100.0% | test_luna_p5_comment: 89/89 units (267 graph trials) |

Edge relations in the ontology files: {"gscs": {"APPLIES_TO": 77, "DEFINED_IN": 10, "HAS_EXAMPLE": 27}, "public5": {"APPLIES_TO": 202, "DEFINED_IN": 101, "HAS_EXAMPLE": 197}}

Relations read by the retriever: APPLIES_TO (rule->language, rule->kind; one hop); DEFINED_IN (filter by standard); HAS_EXAMPLE (examples)
