// F# code
open System.Runtime.InteropServices

[<DllImport("mylib.dll", CallingConvention=CallingConvention.Cdecl)>]

extern type Vector2 = struct
    val x: double 
    val y: double

    new (inx, iny) = {x = inx; y = iny}

    let distanceTo (pos: Vector2): double =
        let distance = sqrt((pos.y - y) * (pos.y - y) + (pos.x - x) * (pos.x - x));
        distance


    
