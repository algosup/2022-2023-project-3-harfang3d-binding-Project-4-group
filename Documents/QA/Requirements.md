# Writing a binding generator

You must know C++ and the target language (Python, Lua, Rust, etc...) and its feature set.<br>

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