<sub> Author : [Karine VINETTE](https://www.linkedin.com/in/karine-vinette-63911b1b8/) (Quality Assurance) </sub><br>
<sub> Team : [Alexis Lasselin](https://www.linkedin.com/in/alexis-lasselin-318649251/) (Project Leader), [Aurélien Hernandez](https://www.linkedin.com/in/aurélien-fernandez-4971201b8/) (Technical Leader), [Laurent Bouquin](https://www.linkedin.com/in/laurent-bouquin-60911a1b8/) (Software Engineer), [Paul NOWAK](https://www.linkedin.com/in/paul-nowak-0757a61a7/) (Quality Assurance) </sub>

## Comparing to others binded languages :

We can compare making a binding for **Fsharp** with making a binding for **Go** because they are both statically typed languages.

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



