# 2022-2023-project-3-harfang3d-binding-Project-4-group

<br>

## Project team

[![LASSELIN Alexis](https://avatars.githubusercontent.com/u/114481578?s=81)](https://github.com/AlexisLasselin)
[![PAUL NOWAK](https://avatars.githubusercontent.com/u/91249965?s=81)](https://github.com/PaulNowak36)
[![AURÉLIEN FERNANDEZ](https://avatars.githubusercontent.com/u/71769656?s=81)](https://github.com/aurelienfernandez)
[![LAURENT BOUQUIN](https://avatars.githubusercontent.com/u/71769489?s=81)](https://github.com/laurentbouquin)
[![KARINE VINETTE](https://avatars.githubusercontent.com/u/71769675?s=81)](https://github.com/KarineVinette)
<br>

**Team members (From left to right)** <br>

[Alexis Lasselin](https://www.linkedin.com/in/alexis-lasselin-318649251/)(Project Manager); [Paul Nowak](https://www.linkedin.com/in/paul-nowak-0757a61a7/)(Program Manager); [Aurélien Fernandez](https://www.linkedin.com/in/aur%C3%A9lien-fernandez-4971201b8/)(Tech Lead); [Laurent Bouquin](https://www.linkedin.com/in/laurent-bouquin-60911a1b8/)(Software Engineer) and [Karine Vinette](https://www.linkedin.com/in/karine-vinette-63911b1b8/)(QA) <br>

## Client

For this project, we are working with the company [Harfang3D](https://www.harfang3d.com/), a French company, based on Orléans and created in 2016, that develops a 3D engine for the industry. The engine is open source and is available on [GitHub](https://github.com/harfang3d).
<br>

## Goal of the project

Our goal for this project is to ad a binding for the language [F#](https://fsharp.org/) to [FABGen](https://github.com/ejulien/FABGen), a [C++](https://en.wikipedia.org/wiki/C%2B%2B) binding generator for [Harfang3D](https://www.harfang3d.com/), written in remplacement of the [SWIG](http://www.swig.org/) binding generator. <br>

<br>

## Changes during the project

During the project we had multiple meetings with the client, since the first meeting we received a new goal: to bind the file vector.h to f#, to achieve that goal, we decided to inspire ourselves from FABgen's structure.
Firstly there is the original file, vector.h, he wasn't modified at all, then you have vectors.cpp, it is a cpp file that is using every functions defined in vector.h. Then you have the main file, Hub.py, it is inspired by FABgen's bind.py, it is a python file that you call to generate a compiled version of your desired C++ file and add multiple lines in your program to be able to call the functions in the compiled file.

## How it works

To use the functions in vector.h you will need to perform few steps:

First you have to go in the folder called "User', as it name indicate, it is a folder created to give users a place to create their F# projects. Then you will have to create your project, to create it you will need to use this command: 
<br>
```dotnet new console -lang F# -n "Your_project_name"```

then go inside your project's folder usind cd:
<br>
```cd "Your_project_name"```

Finally you will have to execute this line inside your terminal:
<br>
```python3 "path to Hub.py (in the root of the project)" -gen vectors --path "path to your directory or ./ if you are already inside it"```


## Documents

[Functional Specifications](Documents/Functional-Specifications.md) <br>
[Technical Specifications](Documents/Technical-Specifications.md) <br>
[Test Plan](Documents/QA/Test-plan.md) <br>
[Project's planner](https://github.com/orgs/algosup/projects/4/views/1) <br>
[Critical path](https://docs.google.com/spreadsheets/d/1LDPr-LcLIMsKmaVQhj4lGdEyIJRwftaApHXx4YnH4_M/edit?usp=sharing) <br>
[Communication plan](Documents/communication-plan.md) <br>
[KPI's evaluation](https://docs.google.com/spreadsheets/d/1W16BV-xJHv1o4vF_B-yCt-Q5-HjRdeBla_S-Vu_Vd5k/edit?usp=sharing)<br>
[Project's research](Documents/Research) <br>
