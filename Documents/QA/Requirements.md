<sub> Author : [Karine VINETTE](https://www.linkedin.com/in/karine-vinette-63911b1b8/) (Quality Assurance) </sub><br>
<sub> Team : [Alexis LASSELIN](https://www.linkedin.com/in/alexis-lasselin-318649251/) (Project Leader), [Aurélien FERNANDEZ](https://www.linkedin.com/in/aurélien-fernandez-4971201b8/) (Technical Leader), [Laurent BOUQUIN](https://www.linkedin.com/in/laurent-bouquin-60911a1b8/) (Software Engineer), [Paul NOWAK](https://www.linkedin.com/in/paul-nowak-0757a61a7/) (Quality Assurance) </sub>

## Introduction

In programming, "binding" refers to the process of connecting a variable or function to a value or a set of instructions. In particular, "language binding" is the process of connecting a program written in one programming language to a library or framework written in another language. This allows the program to access the functionality of the library or framework, and can enable code reuse and interoperability between different languages. For example, a Fsharp program can use a C++ library through language binding, in order to take advantage of the performance benefits of C++ while still using the more convenient Fsharp syntax.

## Writing a binding generator

You must know C++ and the target language (Fsharp) and its feature set.<br>

<details>

  <summary>F# is a statically-typed language</summary>

In a statically-typed language, the type of a variable must be explicitly declared before the variable can be used. Once a variable is declared with a certain type, it can only hold values of that type. The compiler checks that the variable is used in a way that is consistent with its type, and can detect type errors at compile time.

In contrast, in a dynamically-typed language, the type of a variable is determined at runtime, and a variable can hold values of any type. The type check is performed at runtime, and type errors will only be detected at runtime.

</details>

<details>
  <summary>C/C++ and dynamically typed languages (eg. Python, Lua, Squirrel)</summary>
  
  For each type it binds, Fabgen creates a minimum of three functions:

- `check`: Test if an object in the target language holds a copy or reference to a C/C++ object of a specific type.
- `to_c`: Returns a reference to the C/C++ object held by an object in the target language.
- `from_c`: Return an object in the target language holding a copy or reference to a C/C++ object.

The exact signature of these functions depends on the target language API.

</details>

### C/C++ and statically typed languages (eg. Go, C#, Rust)

####  Create a mapping of elementary types

Identify the elementary types common to both languages and create a mapping between them. C types might map to a single or more types in the target language.

#### Implement a C API wrapping the C/C++ objects

Create functions to access object's members of elementary type. Implement a mechanism to access nested objects.

All sorts of strategies can be devised to address complex lifetime issues but selecting the best one to use depends on the native library being wrapped and the target language.

#### Better integration with the target language

While the wrapped API can technically everything we need to use the native library its usage will feel completely foreign to the target language. Let's consider the following sequence of instructions to add two vectors in Python using the wrapped API directly
