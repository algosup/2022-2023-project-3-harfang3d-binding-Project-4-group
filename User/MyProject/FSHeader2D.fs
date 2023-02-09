module vector2
open System.Runtime.InteropServices
[<StructLayout(LayoutKind.Sequential)>]
type Vector2 = val mutable X: double; val mutable Y: double new(x, y) = { X = x; Y = y}
[<DllImport("compiledVector")>]
extern Vector2 CreateVector2D(double x, double y)
[<DllImport("compiledVector")>]
extern double distanceTo2D(Vector2 v,Vector2 v2)
[<DllImport("compiledVector")>]
extern void vectorMovement2D(Vector2 v,double plusx, double plusy)
[<DllImport("compiledVector")>]
extern Vector2 midpoint2D(Vector2 v,Vector2 v2)
[<DllImport("compiledVector")>]
extern double percentDistance2D(Vector2 pos1, Vector2 pos2, double percent)
