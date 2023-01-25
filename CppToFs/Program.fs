open System.Runtime.InteropServices

type MyClassHandle = nativeint
[<DllImport("compiledCPP", CallingConvention=CallingConvention.Cdecl)>]
extern  MyClassHandle MyClass_Create()
[<DllImport("compiledCPP", CallingConvention=CallingConvention.Cdecl)>]
extern  void MyClass_setValue(nativeint myClass, int newValue)

let myClass = MyClass_Create()
let test = MyClass_setValue(myClass, 42)

printfn $"The value is: {test}"
