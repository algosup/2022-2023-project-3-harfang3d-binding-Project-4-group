// F# code
open System.Runtime.InteropServices

[<DllImport("mylib.dll", CallingConvention=CallingConvention.Cdecl)>]

extern type Vector2 = struct
    val x: double 
    val y: double

    new (0, 0) = {x = 0; y = 0}


    
