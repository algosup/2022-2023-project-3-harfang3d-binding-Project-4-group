

##  Harfang 3D technical specification

<hr>

<details><summary>Table of content</summary>

- [Overview](#overview)
	- [Why this project?](#why-this-project)
	- [Schedule](#schedule)
- [Software](#software)
	- [Software architecture](#software-architecture)
	- [File structure](#file-structure)
- [Risk and assumptions](#risk-and-assumptions)
- [testing](#testing)
- [Footnotes](#footnotes)

</details>

<hr>


### Overview

The goal of this project is to translate [FABGen](#FABGen) into [F#](#F#). To do so we will have to understand what is [FABGen](#FABGen) and how it works, moreover, to make it work properly we will have to use three languages which are: 
- [F#](#F#)
- [C++](#C++)
- [Python](#Python)

#### Why this project?

[FABGen](#FABGen) is a binding generator whose purpose is to replace SWIG an older binding generator to fit [Harfang 3D](#Harfang3D) goals. It is currently working with [Python](#Python), Lua, and Go. This project aims to add [F#](#F#) and Rust.

#### Schedule

The project has to be finished by the 17 of February 2023.

The project is divided into three main phases:

- week 1 to week 2 phase 1: creation of documents
- week 2 to week 4 phase 2: Exploration and understanding of [FABGen](#FABGen)
- week 4 to week 6 phase 3: Production of the product

### Software



#### Software architecture 



#### File structure

The project must have a good file structure to work properly, it is one of the main points of this project. Thus the files will be structured as it follows :

<pre>
├── lang
	├── __init__.py
	├── cpython.py
	├── go.py
	├── lua.py
	├── xml.py
	<b>└── fsharp.py (in theory)</b>
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
	<b>└── fsharp(in theory)
		├── __init__.py
		├── std.py
		└── stl.py
		</b>
├── bind.py
├── gen.py
├── license.md
└── readme.md	

</pre>


### Risks

This project has few risks, they can be defined as:
- The risk of being late and miss deadlines.
- The risk of misunderstanding FABgen's functions.
- The risk of bad file structure.

### Testing

Tests are provided by [Harfang 3D](#Harfang3D) so we won't have to create them.

### Footnotes
|word|definition|
|---|:----:|
|<span id="FABGen">FABGen</span> | FABGen is a script written in Python made to create C++ to allow users to code with multiple languages such as Python, Go, and Lua.|
|<span id="F#">F#</span> | F# is an object-oriented language which means it can associate a block of a program to a concept, F# is widely used to make multiple languages work together.|
|<span id="C++">C++</span>| C++ is a high-level programming language, as F#, C++ is an object-oriented language.|
|<span id="Python">Python</span>| Like C++, Python is a high-level language, this language is widely used inside the programming community for his simplicity to use parts of code called libraries which are made by users.|
|<span id="Harfang3D">Harfang 3D</span>| Harfang 3D is a French company based in Orléans with the objective to create a 3D engine for industrial companies and purposes less explored by his concurrence. Harfang 3D is also the name of their 3D engine. |



