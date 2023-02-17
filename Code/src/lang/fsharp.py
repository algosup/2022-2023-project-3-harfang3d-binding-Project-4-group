# FABGen - The Fabulous binding Generator for CPython and Fsharp


import gen



class DummyTypeConverter(gen.TypeConverter):
	def __init__(self, type, to_c_storage_type=None, bound_name=None, from_c_storage_type=None, needs_c_storage_class=False):
		super().__init__(type, to_c_storage_type, bound_name, from_c_storage_type, needs_c_storage_class)

	def get_type_api(self, module_name):
		return ''

	def to_c_call(self, in_var, out_var_p):
		return ''

	def from_c_call(self, out_var, expr, ownership):
		return ''

	def check_call(self, in_var):
		return ''

	def get_type_glue(self, gen, module_name):
		return ''


class DummyExternTypeConverter(gen.TypeConverter):
	def __init__(self, type, to_c_storage_type=None, bound_name=None, module=None):
		super().__init__(type, to_c_storage_type, bound_name, None, None)

		self.module = module  # store module

	def get_type_api(self, module_name):
		return ''

	def to_c_call(self, in_var, out_var_p):
		return ''

	def from_c_call(self, out_var, expr, ownership):
		return ''

	def check_call(self, in_var):
		return ''

	def get_type_glue(self, gen, module_name):
		return ''

class FSharpGenerator(gen.FABGen):
	default_ptr_converter = DummyTypeConverter
	default_class_converter = DummyTypeConverter
	default_extern_converter = DummyExternTypeConverter

	def __init__(self):
		super().__init__()
		self.check_self_type_in_ops = True
		self.fsharp = ''

	def get_language(self):
		return "FSharp"

	def output_includes(self):
		pass

	def start(self, module_name):
		super().start(module_name)



