
## Let's perform a test run of FABGen.

Install CPython 3.x
Fork the original git repository of FABGen (https://github.com/ejulien/FABGen)
Clone it locally
Install requirements from the FABGen repository by running pip install -r requirements.txt
We'll generate the Lua binding for the following hypothetical API (we're only interested in the generator output at this point):

```
class FloatValue {
public:
	FloatValue();
	FloatValue(float value);
	~FloatValue();

	float Get() const;
	void Set(float value);
};
```
FloatValue operator+(const FloatValue &a, const FloatValue &b);
The FABGen script to feed the generator with is written in Python and will look like this:
```
import lib

def bind(gen):
	gen.start('float_value')

	lib.bind_defaults(gen)  # bind default types (int, float, etc...)

	float_value = gen.begin_class('FloatValue')  # begin type definition
	gen.bind_constructor(float_value, ['?float value'])  # declare constructor

	gen.bind_method(float_value, 'Get', 'float', [])  # declare getter method
	gen.bind_method(float_value, 'Set', 'void', ['float value'])  # declare setter method

	gen.bind_arithmetic_ops_overloads(float_value, ['+'], [('FloatValue', ['const FloatValue &b'], [])])  # bind arithmetic operator

	gen.end_class(float_value)

	gen.finalize()
  ```
To generate the Lua and CPython bindings for this library run: 
```
{FABGen}\bind.py --lua --cpython --out {FABGen} test_bind.py
```
... or, on OS X or Linux:
```
python3 {FABGen}/bind.py --lua --cpython --out {FABGen} test_bind.py
```



