

#  Harfang 3D technical specification

<hr>

<details><summary>Table of content</summary>

- [Overview](#overview)
	- [Why this project?](#why-this-project)
- [Software](#software)
	- [Software workflow](#software-workflow)
	- [File structure](#file-structure)
- [Risk and constraints](#risks-and-constraints)
	- [Risks](#risks)
	- [Assumptions](#assumptions)
	- [Constraints](#constraints)
- [testing](#testing)
- [Footnotes](#footnotes)

</details>

<hr>


## Overview

The goal of this project is to update [FABGen](#FABGen) to add [F#](#F#) [bindings](#Bindings) To do so we will have to understand what [FABGen](#FABGen) is and how it works, moreover, to make it work properly we will have to use three languages which are: 
- [F#](#F#)
- [C++](#C++)
- [Python](#Python)

### Why this project?

[FABGen](#FABGen) is a binding generator whose purpose is to replace SWIG an older binding generator to fit [Harfang 3D](#Harfang3D) goals. It is currently working with [Python](#Python), Lua, and Go. This project aims to add [F#](#F#).


## Software


### Software workflow
<img src="./Images/Schema.png" width="400" height="550" />

As you can see above, the user will enter his F# code, then our algorithm will translate the functions in C++, if these functions can't be translated, it will do it in python and then in c++. The remaining code, which is in C++, will finally be send to [Harfang 3D](#Harfang3D).


### File structure

For this project we wanted to use FABgen's original file structure. 

Files named "fsharp" and bold files are what we will have to create during the project.

<pre>
├── lang
	├── __init__.py
	├── cpython.py
	├── go.py
	├── lua.py
	├── xml.py
	<b>└── fsharp.py</b>
├── lib
	├── cpython
	│	├── __init__.py
	│	├── std.py
	│	└── stl.py
	├── lua
	│	├── __init__.py
	│	├── std.py
	│	└── stl.py
	├── xml
	│	├── __init__.py
	│	├── std.py
	│	└── stl.py
	<b>└── fsharp
		├── __init__.py
		├── std.py
		└── stl.py
		</b>
├── bind.py
├── gen.py
├── license.md
└── readme.md	

</pre>


## Risks and constraints

### Risks

This project has few risks, they can be defined as:

The risk of misunderstanding [FABGen](#FABGen)'s functions
In the situation where we misunderstood FABgen's function we might produce function that shouldn't be part of our [bindings](#Bindings), this will lead to a slowdown of our project and result of being late with our deadlines.


The risk of having a non-organised file structure can lead to bugs or being a problem for updating [FABGen](#FABGen) with a file structure different than their own.


The risk of having defective tests, this will end up by having a defective product or having a slowdown during the project.


The risk of [FABGen](#FABGen)'s code not being able to run on our machines.



### Constraints

The project has some constraints, which are:

- F# is a statically typed language, so we need to go through the C language to create the binding.
- F# is also different types compared to C++ or Python, to face this problem we can convert types directly to C++ types.

## Testing

Tests are provided by [Harfang 3D](#Harfang3D) so we won't have to create them, but we will have to adapt them by changing them to [F#](#F#) tests.

## Footnotes
|word|definition|
|-----|:----:|
|<span id="FABGen">FABGen</span>   | FABGen is a script written in Python made to create C++ to allow users to code with multiple languages such as Python, Go, and Lua.|
|<span id="Bindings">Bindings</span>   | Bindings refer to the way in which two languages can access and use functionalities of another language. It allows the exchange of data and their functionalities, enabling them to work together.|
|<img src="./Images/Fsharp_logo.png" width="30" height="30" /> <span id="F#">F#</span>| F# is an object-oriented language which means it can associate a block of a program to a concept, F# is widely used to make multiple languages work together.|
|<img src="./Images/CppLogo.png" width="30" height="30" /><span id="C++">C++</span>| C++ is a high-level programming language, as F#, C++ is an object-oriented language.|
|<img src="./Images/PythonLogo.png" width="30" height="30" /><span id="Python">Python</span>| Like C++, Python is a high-level language, this language is widely used inside the programming community for his simplicity to use parts of code called libraries which are made by users.|
|<img src="./Images/HarfangLogo.png" width="30" height="30" /><span id="Harfang3D">Harfang 3D</span>| Harfang 3D is a French company based in Orléans with the objective to create a 3D engine for industrial companies and purposes less explored by his concurrence. Harfang 3D is also the name of their 3D engine. |



###### [all icons used are made by professionals and are available on Flaticon](https://www.flaticon.com/)
