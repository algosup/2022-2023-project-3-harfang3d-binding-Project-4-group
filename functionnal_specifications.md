<details>
<summary><b id="toc">Table of Content</b></summary>


- [Harfang 3D Binding - Functional Specification](#harfang-3d-binding---functional-specification)
  - [1. Glossary](#1-glossary)
- [2. Introduction](#2-introduction)
- [3. Goal of the project](#3-goal-of-the-project)
  - [3.1. In Scope](#31-in-scope)
  - [3.2. Out Of Scope](#32-out-of-scope)
  - [3.3. Deadline](#33-deadline)
- [4. Functional Requirements](#4-functional-requirements)
  - [4.1. Assumptions](#41-assumptions)
  - [4.2. Constraints](#42-constraints)
- [5. Personas](#5-personas)
  - [5.1. Jean-Charles Magne](#51-jean-charles-magne)
  - [5.2. Hélène Ganthe](#52-helene-ganthe)
  - [5.3. Naisha Kira](#53-naisha-kira)
- [6. Use cases](#6-use-cases)
  - [6.1. Functional Analysis](#61-functional-analysis)
  - [6.2. Use Cases Analysis](#62-use-cases-analysis)
- [7. Non-Functional Requirements](#7-non-functional-requirements)
- [8. Conclusion](#9-conclusion)

</details> 

<sub> Author : [Paul NOWAK](https://www.linkedin.com/in/paul-nowak-0757a61a7/) (Program Manager) </sub>

<sub> Team : [Alexis Lasselin](https://www.linkedin.com/in/alexis-lasselin-318649251/) (Project Leader), [Aurélien Hernandez](https://www.linkedin.com/in/aurélien-fernandez-4971201b8/) (Technical Leader), [Laurent Bouquin](https://www.linkedin.com/in/laurent-bouquin-60911a1b8/) (Software Engineer), [Karine Vignette](https://www.linkedin.com/in/karine-vinette-63911b1b8/) (Quality Assurance) </sub>

---

# Harfang 3D Binding - Functional Specification

# 1. Glossary

 We recommend the reader to read this glossary in order to understand the following parts.  

 - **Harfang 3D** : The society creating different 3D real-time engine solutions. 

  - **FABGen** : A set of Python scripts to generate C++ bidning codes to different languages. 

 - **Binding** : An use of a software library for a different programming language.

 - **Engine** : A program performing a core or essential function, faciliting development and allowing real-time maintenance.

 - **Framework** : A set of tools and software components gathered to allow a faster development of softwares.  

 - **Real-Time 3D** : The method of representation of 3D images that appear to be moving in real time.

 - **HMI** : Abreviation of "**H**uman-**M**achine **I**nterface.  

 - **API** : Abreviation of "**A**pplication **P**rogramming **I**nterface.   

 # 2. Introduction

Harfang  3D is a software developpement company which is dedicated to the creation of human-machine interfaces for various sectors. Founded in 2016, its head office is in Orléans (France) and is run by a team with 15 years of experiences in the video game and industrial sector.

The society is specialized in Real-Time 3D Visualization, they create useful tools to transform the development of real-time 3D imagery in an industrial context. Indeed, their goal is to popularize their use beyond entertainment purposes.

Two developpers of the society, Emmanuel Julien and François Gutherz, want to improve the efficiency of their products. One of their popular project, FABGen, a binding generator used to bring the C++ engine to other languages like Python, Lua or Go. However, it needs to be updated for making more polyvalent and available solutions for their customers. Indeed, they were taking into account the fact that customers didn't want to learn a new language while testing their products.

By the way, the society previously used a popular tool named SWIG which can connect a lot of target languages. Though, it was too old and complex, so they replaced it with FABGen. In fact, their creation is trying to solve its predecessor's issue by implementing new features, and its still evolving. This is the company's duty to complete FABGen's functionalities for improving their creations.

# 3. Goal of the project

The goal of this project is to create a binding in the F# programming language for FABGen.

## 3.1. In Scope
Most importantly, we have to find a way to bridge FABGen with the F# programming language.

The issue is that it's not possible to bridge F# with C++. So, the client wants us to use the C language as an intermediary language between C++ and F#.

Anyway, these are the mains features that are planned for the first version of our product :
-implementation of a C API wrapping C++ objects.
-integration of the F# language with the C API.
-creation of a static library for an embedded use of F#.
-scripting of the required functions for using the native code of F#.     
  
## 3.2. Out Of Scope
Because of the time and resources constraints, we could only include these features in the future versions :
-shown desmonstration of using F# language for compiling an engine's project.
-binding with newer version of F#.
-writing a working manual for using the F# binding.
  
## 3.3. Deadline
The deadline for the V0 is in February 17th 2023.

# 4. Functional Requirements

## 4.1. Assumptions
- Several tests using FABGen with the F# binding must be done.
- The python language should also be studied for understanding FABGen.
- The C API created will go through a process of configuration to be used.
  
## 4.2. Constraints
- F# is a static language, so we need to go through the C language to create the binding.


# 5. Personas

## 5.1 Jean-Charles Magne 

### 5.1.1 Job: 
Developer working for the Research Branch of Renault. He is specialized in the F# and Python languages. 

### 5.1.2 Description: 
Jean Charles is a 43 years old man living in Tours. He has a passion for cars, likes reading Mangas and playing badminton with his friends.

He divorced 2 years ago, so he has custody of his 2 daughters of 13 years and 12 years old. Though, they live with him from Monday to Friday, his working days.

By the way, he works at the car manufacturer society Renault for 6 years at Tours. To reach his workplace, he takes the tramway each morning for 20 minutes to arrive at 8am. Then, he works until 6pm and takes the metro to home.

His job is to search for new software tools and test them in order to improve the society’s productivity. He is part of the IT department and he has to find a solution to design the HUD of a car panel.

### 5.1.3 Goals: 
Jean-Charles wants to spend more time with his daughters during the days he is with them. So, he would like to find a solution where he doesn’t have to learn a new programming language at home. 
 
## 5.2 Hélène Ganthe 

### 5.2.1 Job:  
Lead Designer of the glove making Agnelle company

### 5.2.2 Description: 
Hélène is a 31 years old woman who lives at Paris, in an apartment not far from the Agnelle company. She likes reading novels, musical comedy movies, and is fascinated by leather gloves since her youth. She often wears gloves and is a loving single mother of a 6 years old boy. 
 
Each day (except during the week-end), she takes her son to school by walking before she arrives to her workplace at 9am. Then, she leaves at 4pm before taking a coffee with a friend and picking up her kid to school before going home.

At her workplace, she is the main person in charge of designing new variations of gloves. She leads her team of designer to find new ideas, but also new tools to create concepts more often. Though, most of her team have experience in the F# programming, but they don't have time to focus on learning a new programming language.

### 5.2.3 Goals: 
Hélène wants to spend more time with her child by having more control to her creativity. Indeed, she wants a software to help her team design new gloves according to the hand size. 

## 5.3 Naisha Kira 

### 5.3.1 Job:  
Software developer.
 
### 5.3.2 Description:
Naisha is a 21 years old woman who is temporarily living in an apartment in Orleans for 2 weeks.

She originally came from Mumbai in India where she was born and spent her childhood here. Since she was 7 years old, she had a passion for programming and wants to become a software developer. She knows a few programming languages, especially F# and python.

After she has finished her high school studies, she enrolled herself to an institute of Technology in Mumbai for 2 years. She then got graduated and is now beginning to work for a indian society specialized in robotics in Bangalore.

The society is seeking for a tool to improve the design of their robot arms, and they got in contact with Harfang 3D's society. So, they sent Naisha in France by airplane with a mission to test Harfang's solutions. 

### 5.3.3 Goals: 
Naisha wishes to use her F# skills to help her society finding a software tool to improve their productivity.


# 6. Use cases

## 6.1. Functional Analysis

- UC1 (Activate the F# binding) :  
    - Lambert opens Harfang 3D
    - He creates a scene
    - He activates FABGen to change his scripting language
    - Case is closed

- UC2 (Create a new script in F#) :  
    - Marcus activates the F# binding
    - He creates a new script in his Harfang template
    - He writes in F# and save it
    - Case is closed

- UC3 (Test a scene in Harfang 3D using F#) :  
    - Linda opens a scene in Harfang 3D
    - She uses a script written in F#
    - She tests her scene 
    - Case is closed


## 6.2. Use Cases Analysis 
Here is a more detailed version of the functional analysis above :
<details>
<summary><b id="toc"><u>Use case table</u></b></summary>

| Use Case # | Addresses Business/User Requirement n° | Name          | Description                                                                             | Actor(s)  | Pre-Conditions                                                                                                                                                                                | Flow of Events                                                                                                                         | Post-Conditions                                                                                    | Exit Criteria                                                                                           |
| ---------- | -------------------------------------- | ------------- | --------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| UC 1       | U.R #1                                 | F# Binding    | Lambert wants to activate the F# binding from FABGen so he can code in F# in Harfang 3D | Developer | Lambert must be allowed to use the FABGen project to connect it with Harfang 3D. Indeed, only the authorized users will get to use FABGen and be allowed to use another programming language. | Lambert creates a scene in Harfang 3D so he can work on it. He then select the "Preferences" menu to change his programming languages. | A pop-up showing all available languages bindings will be displayed and Lambert has to select one. | The case is complete once Lambert has selected and saved the programming language.                      |
| UC 2       | U.R #2                                 | New F# Script | Marcus wants to create a new script in F# while working on his HArfang 3D scene.        | Developer | Marcus has to activate the F# binding in the engine's preferences.                                                                                                                            | Once he activated the F# binding, Marcus click on "New Scrit".                                                                         | A window from the default IDE will open automatically and allow him to write in F#.                | The case is complete once Marcus wrote his F# program and saved it, showing it in the scene's database. |
| UC 3       | U.R #3                                 | Scene testing | Linda would like to test the scene she created in Harfang 3D which is using F# scripts  | Developer | The scene Linda is working one must have F# scripts connected to the scene. They must be finished so Linda could test her scene.                                                              | Linda clicks on "Test" to activate a simulation of or scen in 3D real-time using F# languages.                                         | The objects connected to the f# scripts must have a specific behavior in the scene.                | The case is complete once Linda has validated if her F# scripts are working and save her scene.                                                 |

</details>     


# 7. Non-Functional Requirements

# 8. Conclusion
