<details>
<summary style="text-decoration: underline; font-size:150%">Table of contents:</summary>

1. [FSHARP_001](#1-fsharp_001)
2. [Addition](#2-addition)
3. [Loop for](#3-loop-for)
4. [If statement](#4-if-statement)
5. [Class](#5-class)
6. [Tuple](#6-tuple)
    
</details>
 
<sub> Author : [Karine VINETTE](https://www.linkedin.com/in/karine-vinette-63911b1b8/) (Quality Assurance) </sub><br>
<sub> Team : [Alexis LASSELIN](https://www.linkedin.com/in/alexis-lasselin-318649251/) (Project Leader), [Aurélien FERNANDEZ](https://www.linkedin.com/in/aurélien-fernandez-4971201b8/) (Technical Leader), [Laurent BOUQUIN](https://www.linkedin.com/in/laurent-bouquin-60911a1b8/) (Software Engineer), [Paul NOWAK](https://www.linkedin.com/in/paul-nowak-0757a61a7/) (Quality Assurance) </sub>

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

Test Case ID: FSHARP_001

Test Case Name: F# and C++ library integration

Prerequisites:

C++ library has been successfully compiled and linked with the F# code
F# code has been compiled without errors
Test Steps:

Run the F# code
Call the C++ library function add with the input values 3 and 4
Pass the returned value from the C++ library to a F# function that performs additional computation on it.
Verify that the final output of the F# code is correct.
Expected Result:
The F# code should correctly call the C++ library function add and pass the result to another F# function that performs additional computation correctly. The final output should match the expected result.

Actual Result: [Record the actual result of the test here]

Test Pass/Fail Criteria: The test is considered pass if the actual result matches the expected result.

Notes: [Any additional notes or comments related to the test case can be added here]

This test case is checking the overall integration of the F# code and the C++ library. It's also verifies that the data transfer between the two languages is working as expected. 
