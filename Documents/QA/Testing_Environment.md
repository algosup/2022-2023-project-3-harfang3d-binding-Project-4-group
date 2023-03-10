<details>
<summary style="text-decoration: underline; font-size:150%">Table of contents:</summary>

1. [Comparing to others binded languages](#1-comparing-to-others-binded-languages)	
2. [Let's perform a test run of FABGen](#2-lets-perform-a-test)
3. [Binding Example](#3-binding-example)
4. [How to compile the files](#4-how-to-compile-the-files)

    
</details>

<sub> Author : [Karine VINETTE](https://www.linkedin.com/in/karine-vinette-63911b1b8/) (Quality Assurance) </sub><br>
<sub> Team : [Alexis LASSELIN](https://www.linkedin.com/in/alexis-lasselin-318649251/) (Project Leader), [Aurélien FERNANDEZ](https://www.linkedin.com/in/aurélien-fernandez-4971201b8/) (Technical Leader), [Laurent BOUQUIN](https://www.linkedin.com/in/laurent-bouquin-60911a1b8/) (Software Engineer), [Paul NOWAK](https://www.linkedin.com/in/paul-nowak-0757a61a7/) (Program Manager) </sub>

_____________
<a id="1-comparing-to-others-binded-languages"></a>
$\Large{\color{orange}{1. \ Comparing \ to \ others \ binded \ languages}}$

We can compare making a binding for **Fsharp** with making a binding for **Go** because they are both statically typed languages.

<a id="2-lets-perform-a-test"></a>
$\Large{\color{orange}{2. \ Let's \ perform \ a \ test \ run \ of \ FABGen.}}$

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

<a id="3-binding-example"></a>
$\Large{\color{orange}{3. \ Binding \ Example }}$

```
// C++ library
#include <iostream>

extern "C" int add(int a, int b) {
    return a + b;
}

// F# code
open System.Runtime.InteropServices

[<DllImport("mylib.dll", CallingConvention=CallingConvention.Cdecl)>]
extern int add(int a, int b)

let result = add(3, 4)
printfn "3 + 4 = %d" result
```
**Comments :**<br>
In this example, the C++ library contains a function called "add", which takes two integers as arguments and returns their sum. The extern "C" keyword is used to indicate that this function should be exported from the library and made available for other languages to call.
In the F# code, the DllImport attribute is used to import the "add" function from the "mylib.dll" library. The extern keyword is used to indicate that this function is implemented in an external library, and the add function is called with two integer arguments and the result is stored in the result variable. The final line of the F# code uses the printfn function to display the result of the addition.

[External Functions](https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/functions/external-functions)<br/>
[vector.cpp](https://github.com/jackdalton/vector-cpp/blob/master/src/vector.h)


<a id="4-how-to-compile-the-files"></a>
$\Large{\color{orange}{4. \ How \ to \ compile \ the \ files \ ? }}$

Fsharp files : ```dotnet run ```

Python files : macos ```python3 file.py ./```, windows ```python file.py ./```

C++ files : ```g++ -shared -o file.dll file.cpp```

