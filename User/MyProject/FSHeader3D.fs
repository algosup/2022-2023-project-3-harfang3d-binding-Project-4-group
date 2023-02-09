module vector3
open System.Runtime.InteropServices
[<StructLayout(LayoutKind.Sequential)>]
type Vector3 = val mutable X: double; val mutable Y:double; val mutable Z: double new(x, y, z) = { X = x; Y = y; Z=z }
[<DllImport("compiledVector")>]
extern Vector3 CreateVector3D(double x, double y, double z)
[<DllImport("compiledVector")>]
extern double distanceTo3D(Vector3 v, Vector3 v2)
[<DllImport("compiledVector")>]
extern void vectorMovement3D(Vector3 v, double plusx, double plusy, double plusz)
[<DllImport("compiledVector")>]
extern Vector3 midpoint3D(Vector3 v, Vector3 v2)
[<DllImport("compiledVector")>]
extern double percentDistance3D(Vector3 pos1, Vector3 pos2, double percent)
