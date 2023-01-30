open System.Runtime.InteropServices

[<StructLayout(LayoutKind.Sequential)>]
type Vector2 =
    val mutable X: double
    val mutable Y: double
    new(x, y) = { X = x; Y = y }

[<StructLayout(LayoutKind.Sequential)>]
type Vector3 =
    val mutable X: double
    val mutable Y: double
    val mutable Z: double
    new(x, y, z) = { X = x; Y = y; Z = z }

//import all functions 
[<DllImport("compiledCPP")>]
extern Vector2 CreateVector2(double x, double y)

[<DllImport("compiledCPP")>]
extern double GetX(Vector2 v)

[<DllImport("compiledCPP")>]
extern double GetY(Vector2 v)

// [<DllImport("compiledCPP")>]
// extern double vectorMovement(Vector2 vector,double plusx, double plusy)

// [<DllImport("compiledCPP")>]
// extern double midpoint(Vector2 pos1, Vector2 pos2)

[<DllImport("compiledCPP", CallingConvention=CallingConvention.Cdecl)>]
extern double V2distanceTo(Vector2 pos1, Vector2 pos2);


//create vector 1 and 2
let vector = CreateVector2(-2.0, 1.0)
let vector2 = CreateVector2(12.0, 8.0)

// get X and Y of vectors 1 and 2
let test1= Vector2(GetX(vector),GetY(vector))
let test2= Vector2(GetX(vector2),GetY(vector2))

//get distance between points
let result =V2distanceTo(test1,test2)



printfn $"The distance is: {result}"
