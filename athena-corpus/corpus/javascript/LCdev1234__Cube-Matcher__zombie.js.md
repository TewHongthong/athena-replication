# src/zombie.js

- source repo: LCdev1234/Cube-Matcher
- repo url: https://github.com/LCdev1234/Cube-Matcher
- license: MIT
- created_at: 2026-08-05T23:30:41Z
- file path: src/zombie.js
- commit: 4ed30b070c9bb773f67c707dc33c746dbc2a38c2

```javascript
import {Point, Orientation, Face3d, Object3d, Collisions} from "./geometry"
import Phaser from 'phaser'

export default class Zombie{

    static all = new Set()
    static falling = new Set()
    static maximum_zombies = 3

    constructor(face, column){
        this.anim = 0
        this.can_steps = false
        this.steps = 0
        this.x = 0
        this.y = 200
        this.z = 0
        this.y_speed = 0
        this.up = false
        this.first_up = false
        this.normal_face = face
        if(face == 0){
            this.face = "z"
            this.other_face = "x"
        }else{
            this.face = "x"
            this.other_face = "z"
        }
        this.last_face = face
        this.column = column
        this.base = []
        
        if(face == 0) {
            this.base = [
                new Point(0, 0, -15),
                new Point(0, -30, -15),
                new Point(0, -30, +15),
                new Point(0, 0, +15)
            ]
            this.z = -60 + column*60
            this.extra = {x: 95, z: 0}
        }else {
            this.base = [
                new Point(-15, 0, 0),
                new Point(-15, -30, 0),
                new Point(15, -30, 0),
                new Point(15, 0, 0)
            ]
            this.x = -60 + column*60
            this.extra = {x: 0, z: -95}
        }
        this.object =
           new Object3d([
                new Face3d(
                    [
                        this.base[0].add(new Point(this.x, this.y, this.z)),
                        this.base[1].add(new Point(this.x, this.y, this.z)),
                        this.base[2].add(new Point(this.x, this.y, this.z)),
                        this.base[3].add(new Point(this.x, this.y, this.z))
                    ],
                    1,
                    "zombie0"
                )
            ])
        this.hand = undefined
        Zombie.all.add(this)
    }

    update(fps_ratio, rotations, actual_rotations, rotation, player, walk_sound){
        if(!this.can_steps) this.can_steps = true
        let a_texture = "zombie"
        let is_anim = false

        let ghost_rotation = false
        for(let rotation of rotations){
            if(rotation.axis == this.face){
                if(rotation.index == this.column && !this.up){
                    if(Math.abs(actual_rotations[rotation.axis][rotation.index]) > 5) this.face = 3
                }
            }
            if(rotation.axis == this.other_face){
                if(this.face == "x"){
                    if(rotation.index == 0){
                        ghost_rotation = true
                    }
                }else if(this.face == "z"){
                    if(rotation.index == 2){
                        ghost_rotation = true
                    }
                }
            }
        }

        if(!this.up) if(this[this.face] != -60 + this.column*60) this[this.face] += Math.sign((-60 + this.column*60) - this[this.face]) * 1 * fps_ratio
        
        if(this.face != 3){
            if(!ghost_rotation) {
                if(this.y > 90) this.y -= 10 * fps_ratio
                else if(this.y > -65) {
                    let last_steps = this.steps
                    this.steps = Math.max(0, this.steps - 0.7*fps_ratio)
                    this.y -= last_steps - this.steps
                    if(last_steps - this.steps > 0) {
                        if(!walk_sound.isPlaying) walk_sound.play()
                        is_anim = true
                    }
                }
            }
            if(this.y < -65){
                is_anim = true
                a_texture = "zombie_body"
                if(this.hand == undefined){
                    let x = this.x + this.extra["x"]
                    let z = this.z + this.extra["z"]
                    this.hand = new Object3d([
                        new Face3d(
                            [
                                this.base[0].add(new Point(x, this.y, z)),
                                this.base[1].add(new Point(x, this.y, z)),
                                this.base[2].add(new Point(x, this.y, z)),
                                this.base[3].add(new Point(x, this.y, z))
                            ],
                            1,
                            "zombie_hands"
                        )
                    ])
                }
                this.y -= 0.6 * fps_ratio
                if(this.y < -90){
                    this.y = -90
                    this.hand = undefined
                    this.up = true
                    a_texture = "zombie_atack"
                    if(!this.first_up){
                        this.base = [
                            new Point(-15, 0, 0),
                            new Point(-15, -30, 0),
                            new Point(15, -30, 0),
                            new Point(15, 0, 0)
                        ]
                        this.x += this.extra.x * 0.9
                        this.z += this.extra.z * 0.9
                    }
                    this.first_up = true

                    player.active = false
                    
                }
            }
            if(is_anim) this.anim += 0.3 * fps_ratio
            this.anim %= 10
        }else{
            if(this.y > 200) {
                Zombie.all.delete(this)
                Zombie.falling.delete(this)
            }else if(this.y > -90 && !Zombie.falling.has(this)) Zombie.falling.add(this)
            this.y_speed += 0.4 * fps_ratio
            this.y += this.y_speed
            this.hand = undefined
        }
        if(this.up){
            if(!player.dead){
                if(!walk_sound.isPlaying) walk_sound.play()
                let angle_to_player = Math.atan2(player.z - (this.z), player.x - (this.x))
                let distance_to_player = Math.hypot(player.x - (this.x), player.z - (this.z))
                this.x += 1.5 * Math.cos(angle_to_player) * fps_ratio
                this.z += 1.5 * Math.sin(angle_to_player) * fps_ratio
                if(Math.cos(angle_to_player) > 0){
                    this.object.faces[0].flipX = false
                }else{
                    this.object.faces[0].flipX = true
                }
                if(distance_to_player < 10){
                    player.dead = true
                }
            }
        }

        let x = this.x + this.extra["x"]
        let z = this.z + this.extra["z"]
        let y = this.y
        if(this.up){
            x = (this.x) * Math.cos(-rotation.y * Math.PI / 180) - (this.z) * Math.sin(-rotation.y * Math.PI / 180)
            z = (this.x) * Math.sin(-rotation.y * Math.PI / 180) + (this.z) * Math.cos(-rotation.y * Math.PI / 180)
        }else if(ghost_rotation){
            if(this.face == "x"){
                x = (this.x) * Math.cos(actual_rotations.z[0] * Math.PI / 180) - (this.y) * Math.sin(actual_rotations.z[0] * Math.PI / 180)
                y = (this.x) * Math.sin(actual_rotations.z[0] * Math.PI / 180) + (this.y) * Math.cos(actual_rotations.z[0] * Math.PI / 180)
            }else if(this.face == "z"){
                z = (this.z) * Math.cos(-actual_rotations.x[2] * Math.PI / 180) - (this.y) * Math.sin(-actual_rotations.x[2] * Math.PI / 180)
                y = (this.z) * Math.sin(-actual_rotations.x[2] * Math.PI / 180) + (this.y) * Math.cos(-actual_rotations.x[2] * Math.PI / 180)
            }
            if(this.hand != undefined){
                this.face = 3
            }
        }

        this.object.faces[0].texture = a_texture + Math.floor(this.anim)
        this.object.faces[0].points = 
        [
            this.base[0].add(new Point(x, y, z)),
            this.base[1].add(new Point(x, y, z)),
            this.base[2].add(new Point(x, y, z)),
            this.base[3].add(new Point(x, y, z))
        ]
    }

    change_place(rotations, actual_rotations){
        for(let rotation of rotations){
            if(rotation.axis == this.other_face){
                let x = this.x
                let y = this.y
                let z = this.z
                if(this.face == "x"){
                    x = (this.x) * Math.cos(actual_rotations.z[0] * Math.PI / 180) - (this.y) * Math.sin(actual_rotations.z[0] * Math.PI / 180)
                    y = (this.x) * Math.sin(actual_rotations.z[0] * Math.PI / 180) + (this.y) * Math.cos(actual_rotations.z[0] * Math.PI / 180)
                }else if(this.face == "z"){
                    z = (this.z) * Math.cos(-actual_rotations.x[2] * Math.PI / 180) - (this.y) * Math.sin(-actual_rotations.x[2] * Math.PI / 180)
                    y = (this.z) * Math.sin(-actual_rotations.x[2] * Math.PI / 180) + (this.y) * Math.cos(-actual_rotations.x[2] * Math.PI / 180)
                }
                this.x = x
                this.y = y
                this.z = z
                this.column = Math.min(Math.max(0, Math.floor((this[this.face] + 90) /60)), 2)
            }
        }
    }

    add_steps(steps = 10){
        if(this.can_steps) this.steps += steps
        let total_zombies = Zombie.maximum_zombies-(Zombie.all.size-Zombie.falling.size)
        for(let i = 0; i < total_zombies; i++){
            const avaible = Zombie.avaible_columns()
            const position = avaible[Math.floor(Math.random() * avaible.length)]
            new Zombie(position.face, position.column)
        }
    }

    static avaible_columns(){
        let unavaible = new Set()
        for(let zombie of Zombie.all){
            if(!Zombie.falling.has(zombie)) unavaible.add(zombie.normal_face + "-" + zombie.column)
        }

        let avaible = []
        for(let i = 0; i < 2; i++){
            for(let n = 0; n < 3; n++){
                if(!unavaible.has(i + "-" + n)){
                    avaible.push({face: i, column: n})
                }
            }
        }
        return avaible
    }

    static reset(){
        Zombie.all.clear()
        Zombie.falling.clear()
    }

    static setMaximumZombies(maximum){
        Zombie.maximum_zombies = maximum
    }
}```
