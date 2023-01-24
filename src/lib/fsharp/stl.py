import lang.fsharp



type FsharpStringConverter() =
    inherit FsharpTypeConverterCommon()
    let cType = "*C.char"
    let fsharpType = "string"

    override this.GetTypeGlue(gen:string, moduleName:string) = ""
    override this.GetTypeApi(moduleName:string) = ""

    override this.ToC_Call(inVar:string, outVarP:string, isPointer:bool) =
        if isPointer then
            sprintf "let %s1 = C.CString(%s)\n%s = &%s1" outVarP.Replace("&", "_") inVar outVarP.Replace("&", "_") outVarP.Replace("&", "_")
        else
            sprintf "let %s, finalizer = wrapString(%s)\nGC.KeepAlive(finalizer) %s" outVarP.Replace("&", "_") inVar outVarP.Replace("&", "_")

    override this.FromC_Call(outVar:string, expr:string, ownership:string) =
        sprintf "C.FsharpString(%s)" outVar

let gen = new FsharpTypeConverter()
gen.BindType(FsharpStringConverter())


type FsharpStdFunctionConverter(typ:string) =
    inherit FsharpTypeConverterCommon()

    override this.GetTypeGlue(gen:string, moduleName:string) = ""

let bind_function_T (gen:FsharpTypeConverter) (typ:string) (bound_name:string option) = 
    gen.BindType(FsharpStdFunctionConverter(typ))

type FsharpSliceToStdVectorConverter(typ:string, T_conv:GoTypeConverter) = 
    inherit FsharpTypeConverterCommon()
    let nativeType = sprintf "std::vector<%s>" T_conv.ctype
    do  base.New(typ, nativeType, None, nativeType)
    let T_conv = T_conv

    override this.GetTypeGlue(gen:string, moduleName:string) = ""
    override this.ToC_Call(inVar:string, outVarP:string, isPointer:bool) = ""
    override this.FromC_Call(outVar:string, expr:string, ownership:string) = ""

