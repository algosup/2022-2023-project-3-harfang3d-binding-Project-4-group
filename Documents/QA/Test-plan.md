<details>
<summary style="text-decoration: underline; font-size:150%">Table of contents:</summary>

1. [Hello-World](#1-hello-world)
2. [Addition](#2-addition)
3. [Loop for](#3-loop-for)
4. [If statement](#4-if-statement)
5. [Class](#5-class)
6. [Tuple](#6-tuple)
    
</details>
 
<sub> Author : [Karine VINETTE](https://www.linkedin.com/in/karine-vinette-63911b1b8/) (Quality Assurance) </sub><br>
<sub> Team : [Alexis LASSELIN](https://www.linkedin.com/in/alexis-lasselin-318649251/) (Project Leader), [Aurélien FERNANDEZ](https://www.linkedin.com/in/aurélien-fernandez-4971201b8/) (Technical Leader), [Laurent BOUQUIN](https://www.linkedin.com/in/laurent-bouquin-60911a1b8/) (Software Engineer), [Paul NOWAK](https://www.linkedin.com/in/paul-nowak-0757a61a7/) (Quality Assurance) </sub>

---

<h1>Testing Plan</h1>

#### Scope : ALGOSUP is asked to write a **binding generator in Fsharp** to diversify the use of languages for their game engine "Harfang 3D".
#### Date of the delivery : 17th february 2023.



## 1. Hello-World
```
printfn "Hello from F#"
```

## 2. Addition
Fsharp:
```
let sum (x: int, y: int) = x + y
    printfn "sum = %d" (sum (1, 2))
```
To C++:
```
#include <iostream>

int sum(int x, int y) {
    return x + y;
}

int main() {
    int result = sum(1, 2);
    std::cout << "sum = " << result << std::endl;
    return 0;
}
```

## 3. Loop for
```
let list1 = [ 1; 5; 100; 450; 788 ]
for i in list1 do
   printfn "%d" i
```

## 4. If statement
```
printfn "What is your age? "
let ageString = System.Console.ReadLine()
let age = System.Int32.Parse(ageString)

if age < 10 then
    printfn "You are only %d years old and already learning F#? Wow!" age
else printfn "Work harder"
```

## 5. Class
```
type Person(firstName:string, lastName:string) =
    let mutable age = 0
    member this.FirstName = firstName
    member this.LastName = lastName
    member this.Age with get() = age and set(value) = age <- value
    member this.FullName = sprintf "%s %s" firstName lastName
    
let person = Person("John", "Doe")
printfn "%s %s" person.FirstName person.LastName
```

## 6. Tuple
```
let averageFour (a, b, c, d) =
   let sum = a + b + c + d
   sum / 4.0

let avg:float = averageFour (4.0, 5.1, 8.0, 12.0)
printfn "Avg of four numbers: %f" avg
```





