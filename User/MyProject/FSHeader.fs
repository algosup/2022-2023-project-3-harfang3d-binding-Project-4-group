module vector2
open System.Runtime.InteropServices
[<StructLayout(LayoutKind.Sequential)>]
type Vector2 = val mutable X: double; val mutable Y: double new(x, y) = { X = x; Y = y}
[<DllImport("compiledVector2")>]
extern Vector2 CreateVector2(double x, double y)
[<DllImport("compiledVector2")>]
extern double distanceTo(Vector2 v,Vector2 v2)
[<DllImport("compiledVector2")>]
extern void vectorMovement(Vector2 v,double plusx, double plusy)
[<DllImport("compiledVector2")>]
extern Vector2 midpoint(Vector2 v,Vector2 v2)
[<DllImport("compiledVector2")>]
extern double percentDistance(Vector2 pos1, Vector2 pos2, double percent)
