import lang.fsharp

def bind_std(gen):
	class FsharpConstCharPtrConverter(lang.fsharp.FsharpConverter):
		def __init__(self):
			lang.fsharp.FsharpConverter.__init__(self, 'const char*', 'string', 'C.string')
		def convert(self, gen, value):
			return '"%s"' % value
		def convert_back(self, gen, value):
			return value
	gen.BindType(FsharpConstCharPtrConverter())
	
	class FsharpBasicTypeConverter(lang.fsharp.FsharpConverter):
		def __init__(self, type, c_type, fs_type, to_c_storage_type=None, bound_name=None, from_c_storage_type=None, needs_c_storage_class=False):
			super().__init__(type, to_c_storage_type, bound_name, from_c_storage_type, needs_c_storage_class)
			self.fs_to_c_type = c_type
			self.fs_type = fs_type
		def convert(self, gen, value):
			return value
		def convert_back(self, gen, value):
			return value

	gen.BindType(FsharpBasicTypeConverter("char", "C.char", "char"))

	gen.BindType(FsharpBasicTypeConverter("unsigned char", "C.uchar", "uchar"))
	gen.BindType(FsharpBasicTypeConverter("uint8_t", "C.uchar", "uint8"))
	
	gen.BindType(FsharpBasicTypeConverter("short", "C.short", "int16"))
	gen.BindType(FsharpBasicTypeConverter("int16_t", "C.short", "int16"))
	gen.BindType(FsharpBasicTypeConverter("char16_t", "C.short", "int16"))

	gen.BindType(FsharpBasicTypeConverter("uint16_t", "C.ushort", "uint16"))
	gen.BindType(FsharpBasicTypeConverter("unsigned short", "C.ushort ", "uint16"))

	gen.BindType(FsharpBasicTypeConverter("int32", "C.int32_t", "int32"))
	gen.BindType(FsharpBasicTypeConverter("int", "C.int32_t", "int32"))
	gen.BindType(FsharpBasicTypeConverter("int32_t", "C.int32_t", "int32"))
	gen.BindType(FsharpBasicTypeConverter("char32_t", "C.int32_t", "int32"))
	gen.BindType(FsharpBasicTypeConverter("size_t", "C.size_t", "int32"))

	gen.BindType(FsharpBasicTypeConverter("uint32_t", "C.uint32_t", "uint32"))
	gen.BindType(FsharpBasicTypeConverter("unsigned int32_t", "C.uint32_t", "uint32"))
	gen.BindType(FsharpBasicTypeConverter("unsigned int", "C.uint32_t", "uint32"))

	gen.BindType(FsharpBasicTypeConverter("int64_t", "C.int64_t", "int64"))
	gen.BindType(FsharpBasicTypeConverter("long", "C.int64_t", "int64"))

	gen.BindType(FsharpBasicTypeConverter("float32", "C.float", "float32"))
	gen.BindType(FsharpBasicTypeConverter("float", "C.float", "float32"))

	gen.BindType(FsharpBasicTypeConverter("intptr_t", "C.intptr_t", "uintptr"))

	gen.BindType(FsharpBasicTypeConverter("unsigned long", "C.uint64_t", "uint64"))
	gen.BindType(FsharpBasicTypeConverter("uint64_t", "C.uint64_t ", "uint64"))
	gen.BindType(FsharpBasicTypeConverter("double", "C.double", "float64"))