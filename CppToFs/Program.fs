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

[<DllImport("compiledCPP")>]
extern void vectorMovement(Vector2 vector,double plusx, double plusy)

[<DllImport("compiledCPP")>]
extern Vector2 midpoint(Vector2 pos1, Vector2 pos2)

[<DllImport("compiledCPP", CallingConvention=CallingConvention.Cdecl)>]
extern double V2distanceTo(Vector2 pos1, Vector2 pos2);

[<DllImport("compiledCPP", CallingConvention=CallingConvention.Cdecl)>]
extern double percentDistance(Vector2 pos1, Vector2 pos2, double);


//create vector 1 and 2
let vector = CreateVector2(10.0, 0.0)
let vector2 = CreateVector2(0.0, 0.0)

// get X and Y of vectors 1 and 2
let test1= Vector2(GetX(vector),GetY(vector))
let test2= Vector2(GetX(vector2),GetY(vector2))

//get distance between two vectors
printfn"Distance"
let distance =V2distanceTo(test1,test2)
printfn $"The distance is: {distance}"

//Move vector's points 
// !!!!!!
// Test 1 is being modified by vectorMovement
// !!!!!!

printfn"______________________________________________"
printfn"Move points"
printfn $"The before movement X= {GetX(vector)} and Y= {GetY(vector)}"
let move =vectorMovement(test1, -12.0,36.0)
printfn $"after movement X= {GetX(test1)} and Y= {GetY(test1)}"

//get midpoint from vector A to B
let Midpoint: Vector2 =midpoint(test1,test2)

printfn"______________________________________________"
printfn"Get mid point"
printfn $"test1 X= {GetX(test1)} Y={GetY(test1)}"
printfn $"test2 X= {GetX(test2)} Y={GetY(test2)}"
printfn $"The mid point between test1 and test2 is: X= {GetX(Midpoint)} Y: {GetY(Midpoint)}"

//get percentage of the distance from vector A to B
let vector3 = CreateVector2(10.0, 0.0)
let test3= Vector2(GetX(vector3),GetY(vector3))
let vector4 = CreateVector2(0.0, 0.0)
let test4= Vector2(GetX(vector4),GetY(vector4))

let percentage: double =percentDistance(test3,test4, 50)

printfn"______________________________________________"
printfn"Get percentage between two vectors"
printfn $"test1 X= {GetX(test3)} Y={GetY(test3)}"
printfn $"test2 X= {GetX(test4)} Y={GetY(test4)}"
printfn $"The distance is: {distance}"
printfn $"The point at 50 percent between test1 and test2 is: {percentage}"
