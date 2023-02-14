<details>
<summary style="text-decoration: underline; font-size:150%">Table of contents:</summary>

1. [FSHARP_001](#1-fsharp_001)
2. [FSHARP_002](#2-fsharp_002)

    
</details>
 
<sub> Author : [Karine VINETTE](https://www.linkedin.com/in/karine-vinette-63911b1b8/) (Quality Assurance) </sub><br>
<sub> Team : [Alexis LASSELIN](https://www.linkedin.com/in/alexis-lasselin-318649251/) (Project Leader), [Aurélien FERNANDEZ](https://www.linkedin.com/in/aurélien-fernandez-4971201b8/) (Technical Leader), [Laurent BOUQUIN](https://www.linkedin.com/in/laurent-bouquin-60911a1b8/) (Software Engineer), [Paul NOWAK](https://www.linkedin.com/in/paul-nowak-0757a61a7/) (Program Manager) </sub>

---
<h1>Test Cases</h1>


## 1. FSHARP_001
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
<sub>In this example, the C++ library contains a function called "add", which takes two integers as arguments and returns their sum. The extern "C" keyword is used to indicate that this function should be exported from the library and made available for other languages to call.
In the F# code, the DllImport attribute is used to import the "add" function from the "mylib.dll" library. The extern keyword is used to indicate that this function is implemented in an external library, and the add function is called with two integer arguments and the result is stored in the result variable. The final line of the F# code uses the printfn function to display the result of the addition.</sub>

${\color{orange}Test Case ID:}$ FSHARP_001

${\color{orange}Test Case Name:}$ F# and C++ library integration

${\color{orange}Prerequisites:}$

C++ library has been successfully compiled and linked with the F# code
F# code has been compiled without errors<br>

${\color{orange}Test Steps:}$

Run the F# code
Call the C++ library function add with the input values 3 and 4.<br>
Pass the returned value from the C++ library to a F# function that performs additional computation on it.<br>
Verify that the final output of the F# code is correct.<br>

${\color{orange}Expected Result:}$

The F# code should correctly call the C++ library function add and pass the result to another F# function that performs additional computation correctly. The final output should match the expected result.<br>

${\color{orange}Actual Result:}$

[Record the actual result of the test here]

${\color{orange}Test Pass/Fail Criteria:}$

The test is considered pass if the actual result matches the expected result.

${\color{orange}Notes:}$
[Any additional notes or comments related to the test case can be added here]

This test case is checking the overall integration of the F# code and the C++ library. It's also verifies that the data transfer between the two languages is working as expected. 


## 2. FSHARP_002

${\color{orange}Test Case ID:}$ FSHARP_002

${\color{orange}Test Case Name:}$ F# binding1

${\color{orange}Prerequisites:}$

C++ library has been compiled without errors<br>
F# code has been compiled without errors<br>

${\color{orange}Test Steps:}$

Run the Python file with going in the wright folder.<br>
Open a terminal and write 
```
python3 gen.py ./
```

${\color{orange}Expected Result:}$

The file would compiled correctly and send the answers of the code as an output.<br>
A file.cpp is created.<br>

${\color{orange}Actual Result:}$

```
Test 1 passed
Test 2 passed
Test 3 passedGet values
The before movement X= 1 and Y= 2 and Z=3
______________________________________________
Get Distance
The Distance between the first and second vector is: 3.7416573867739413
______________________________________________
Move the first vector +1 to each point
The Vector 1 was at X=0, Y=0 and Z=0 
It is now X= 1 and Y= 1 and Z=1 
______________________________________________
Get the midpoint between the two vectors
The midpoint between the first and second vector is X= 1 and Y= 1.5 and Z=2 
______________________________________________
Get the distance between the two vectors divised by a percentage
The distance between the first and second vector at 50 percent is: 1.118033988749895
And the full distanc is: 2.23606797749979
```

${\color{orange}Test Pass/Fail Criteria:}$

The test is considered pass if the actual result matches the expected result.

${\color{orange}Notes:}$
[Any additional notes or comments related to the test case can be added here]

This test case is checking the overall integration of the F# code and the C++ library. It's also verifies that the data transfer between the two languages is working as expected. 
