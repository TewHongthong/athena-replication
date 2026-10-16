# src/geometry.js

- source repo: LCdev1234/Cube-Matcher
- repo url: https://github.com/LCdev1234/Cube-Matcher
- license: MIT
- created_at: 2026-08-05T23:30:41Z
- file path: src/geometry.js
- commit: 4ed30b070c9bb773f67c707dc33c746dbc2a38c2

```javascript
//Point class (x, y, z coordinates)
export class Point {
    constructor(x, y, z, depth = 0) {
        this.x = x
        this.y = y
        this.z = z
        this.depth = depth
    }

    substract(point){
        return new Point(this.x - point.x, this.y - point.y, this.z - point.z)
    }

    add(point){
        return new Point(this.x + point.x, this.y + point.y, this.z + point.z)
    }

    cross(point){
        return new Point(
            this.y * point.z - this.z * point.y,
            this.z * point.x - this.x * point.z,
            this.x * point.y - this.y * point.x
        )
    }

    normalize() {
        const length = Math.sqrt(
            this.x * this.x + this.y * this.y + this.z * this.z
        )
        return new Point(this.x / length, this.y / length, this.z / length)
    }

    dot(point){
        return this.x * point.x + this.y * point.y + this.z * point.z
    }
}

export class Orientation {
    constructor(x, y, z) {
        this.x = x
        this.y = y
        this.z = z
    }
}

export class Face3d {
    constructor(points, color, texture = "", flipX=false){
        this.points = points
        this.color = color
        this.texture = texture
        this.flipX = flipX
    }

    substract(tx, ty, tz){
        let transformed_face = []

        let big_x = -10000000
        let big_y = -10000000
        let big_z = -10000000
        for(let point of this.points){
            let x = point.x
            let y = point.y
            let z = point.z

            if(big_x < x) big_x = x
            if(big_y < y) big_y = y
            if(big_z < z) big_z = z
        }
        for(let point of this.points){
            let x = point.x
            let y = point.y
            let z = point.z

            if(x == big_x){
                x -= tx
            }
            if(y == big_y){
                y -= ty
            }
            if(z == big_z){
                z -= tz
            }

            transformed_face.push(new Point(x, y, z, point.depth))
        }
        return(new Face3d(transformed_face, this.color, this.texture, this.flipX))
    }

    transform(tx, ty, tz){
        let transformed_face = []
        for(let point of this.points){
            let x = point.x
            let y = point.y
            let z = point.z

            //Point Rotation
            let rx = tx * Math.PI / 180
            let ry = ty * Math.PI / 180
            let rz = tz * Math.PI / 180
            let last_x = x;
            let last_y = y;
            let last_z = z;
            x = last_x*Math.cos(rz) - last_y*Math.sin(rz) + 0
            y = last_x*Math.sin(rz) + last_y*Math.cos(rz) + 0
            z = last_z

            last_x = x;
            last_y = y;
            last_z = z;
            x = last_x*Math.cos(ry) + 0 + last_z*Math.sin(ry)
            y = last_y
            z = -last_x*Math.sin(ry) + 0 + last_z*Math.cos(ry)

            last_x = x;
            last_y = y;
            last_z = z;
            x = x
            y = 0 + last_y*Math.cos(rx) - last_z*Math.sin(rx)
            z = 0 + last_y*Math.sin(rx) + last_z*Math.cos(rx)

            //Add points
            transformed_face.push(new Point(x, y, z, point.depth))
        }
        return(new Face3d(transformed_face, this.color, this.texture, this.flipX))
    }
    translation(tx, ty, tz){
        let transformed_face = []
        for(let point of this.points){
            let x = point.x
            let y = point.y
            let z = point.z

            x += tx
            y += ty
            z += tz

            //Add points
            transformed_face.push(new Point(x, y, z, point.depth))
        }
        return(new Face3d(transformed_face, this.color, this.texture, this.flipX))
    }
    projection(size = 1){
        let transformed_face = []
        for(let point of this.points){
            let x = point.x
            let y = point.y
            let z = point.z

            //Perspective Projection
            let last_x = x
            let last_y = y
            let last_z = z
            const distance = 500
            const fov = distance * size
            const depth = last_z + distance
            x = last_x * fov / depth
            y = last_y * fov / depth

            //Add points
            transformed_face.push(new Point(x, y, z, depth))
        }
        return(new Face3d(transformed_face, this.color, this.texture, this.flipX))
    }
    selfTransform(dx, dy, dz, tx, ty, tz){
        let transformed_face = []
        for(let point of this.points){
            let x = point.x - dx
            let y = point.y - dy
            let z = point.z - dz

            //Point Rotation
            let rx = tx * Math.PI / 180
            let ry = ty * Math.PI / 180
            let rz = tz * Math.PI / 180
            let last_x = x;
            let last_y = y;
            let last_z = z;
            x = last_x*Math.cos(rz) - last_y*Math.sin(rz) + 0
            y = last_x*Math.sin(rz) + last_y*Math.cos(rz) + 0
            z = last_z

            last_x = x;
            last_y = y;
            last_z = z;
            x = last_x*Math.cos(ry) + 0 + last_z*Math.sin(ry)
            y = last_y
            z = -last_x*Math.sin(ry) + 0 + last_z*Math.cos(ry)

            last_x = x;
            last_y = y;
            last_z = z;
            x = x
            y = 0 + last_y*Math.cos(rx) - last_z*Math.sin(rx)
            z = 0 + last_y*Math.sin(rx) + last_z*Math.cos(rx)

            //Add points
            transformed_face.push(new Point(x + dx, y + dy, z + dz, point.depth))
        }
        return(new Face3d(transformed_face, this.color, this.texture, this.flipX))
    }
}

export class Object3d {
    constructor(faces){
        this.faces = faces
    }

    add_faces(...faces){
        for(let face of faces){
            this.faces.push(face)
        }
    }
}

export class Collisions {

    static CheckTriangle(point, ta, tb, tc){
        let radius = 10
        let nearest = this.NearestPointTriangle(point, ta, tb, tc)
        let distance = Math.sqrt(Math.pow((nearest.x - point.x),2) + Math.pow((nearest.y - point.y), 2) + Math.pow((nearest.z - point.z), 2))
        let col_distance = radius - distance
        let col_direction
        let ab = tb.substract(ta)
        let ac = tc.substract(ta)

        let normal = ab.cross(ac)
        normal = normal.normalize()
        if(distance != 0){
            col_direction = new Point((point.x - nearest.x) / distance, (point.y - nearest.y) / distance, (point.z - nearest.z) / distance)
        }else{
            col_direction = normal
        }
        return({collision: distance < radius, distance: col_distance, direction: col_direction, normals: normal})
    }

    static NearestPointTriangle(p, a, b, c){
        const ab = b.substract(a)
        const ac = c.substract(a)
        const ap = p.substract(a)

        const d1 = ab.dot(ap)
        const d2 = ac.dot(ap)

        // #1: región del vértice A
        if (d1 <= 0 && d2 <= 0) {
            return a
        }

        const bp = p.substract(b)
        const d3 = ab.dot(bp)
        const d4 = ac.dot(bp)

        // #2: región del vértice B
        if (d3 >= 0 && d4 <= d3) {
            return b
        }

        const cp = p.substract(c)
        const d5 = ab.dot(cp)
        const d6 = ac.dot(cp)

        // #3: región del vértice C
        if (d6 >= 0 && d5 <= d6) {
            return c
        }

        // #4: región de la arista AB
        const vc = d1 * d4 - d3 * d2

        if (vc <= 0 && d1 >= 0 && d3 <= 0) {
            const v = d1 / (d1 - d3)

            return new Point(
                a.x + v * ab.x,
                a.y + v * ab.y,
                a.z + v * ab.z
            )
        }

        // #5: región de la arista AC
        const vb = d5 * d2 - d1 * d6

        if (vb <= 0 && d2 >= 0 && d6 <= 0) {
            const v = d2 / (d2 - d6)

            return new Point(
                a.x + v * ac.x,
                a.y + v * ac.y,
                a.z + v * ac.z
            )
        }

        // #6: región de la arista BC
        const va = d3 * d6 - d5 * d4

        if (va <= 0 && (d4 - d3) >= 0 && (d5 - d6) >= 0) {
            const v = (d4 - d3) / ((d4 - d3) + (d5 - d6))

            return new Point(
                b.x + v * (c.x - b.x),
                b.y + v * (c.y - b.y),
                b.z + v * (c.z - b.z)
            )
        }

        // #0: región interior del triángulo
        const denom = 1 / (va + vb + vc)
        const v = vb * denom
        const w = vc * denom

        return new Point(
            a.x + v * ab.x + w * ac.x,
            a.y + v * ab.y + w * ac.y,
            a.z + v * ab.z + w * ac.z
        )
    }
}```
