import os
import sys
from pathlib import Path
from sys import platform
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="The path of your directory")
args = parser.parse_args()

# Check if every needed files exists and replace compiled files that are already existing
if os.path.exists(args.path+"Program.fs"):
    pass
else:
    sys.exit(
        "The file have not been found, please verify the location of your Program.fs")


if os.path.exists(args.path+"compiledVectors"):
    os.remove(args.path+"compiledVectors")

if os.path.exists(args.path+"compiledVectors.exe"):
    os.remove(args.path+"compiledVectors.exe")


# compiling the related C++ file
def compile_cpp(file_path):
    if platform == "darwin":  # macOs
        subprocess.run(["g++", "-o", "compiledVectors", file_path])
    elif platform == "win32":  # Windows
        subprocess.run(
            ["g++", "-shared", "-o", "compiledVectors.exe", "-m64", file_path])


compile_cpp("../../CppToFs/Vectors/Vectors.cpp")

if os.path.exists(args.path+"FSHeader2D.fs"):
    os.remove(args.path+"FSHeader2D.fs")
else:
    pass
if os.path.exists(args.path+"FSHeader3D.fs"):
    os.remove(args.path+"FSHeader3D.fs")
else:
    pass

if platform == "darwin":
    Header2D = open(args.path+"FSHeader2D.fs", "w")
    imports2D = ["module vector2\n",
                'open System.Runtime.InteropServices\n',

                '[<StructLayout(LayoutKind.Sequential)>]\n',
                'type Vector2 = val mutable X: double; val mutable Y: double new(x, y) = { X = x; Y = y}\n',

                '[<DllImport("compiledVectors")>]\n',
                'extern Vector2 CreateVector2D(double x, double y)\n',

                '[<DllImport("compiledVectors")>]\n',
                'extern double distanceTo2D(Vector2 v,Vector2 v2)\n',

                '[<DllImport("compiledVectors")>]\n',
                'extern void vectorMovement2D(Vector2 v,double plusx, double plusy)\n',

                '[<DllImport("compiledVectors")>]\n',
                'extern Vector2 midpoint2D(Vector2 v,Vector2 v2)\n',

                '[<DllImport("compiledVectors")>]\n',
                'extern double percentDistance2D(Vector2 pos1, Vector2 pos2, double percent)\n']
    for eachimports in imports2D:
        Header2D.write(eachimports)
        Header2D.flush()

    Header3D = open(args.path+"FSHeader3D.fs", "w")
    imports3D = ["module vector3\n",
                'open System.Runtime.InteropServices\n',

                '[<StructLayout(LayoutKind.Sequential)>]\n',
                'type Vector3 = val mutable X: double; val mutable Y:double; val mutable Z: double new(x, y, z) = { X = x; Y = y; Z=z }\n',

                '[<DllImport("compiledVectors")>]\n',
                'extern Vector3 CreateVector3D(double x, double y, double z)\n',

                '[<DllImport("compiledVectors")>]\n',
                'extern double distanceTo3D(Vector3 v, Vector3 v2)\n',

                '[<DllImport("compiledVectors")>]\n',
                'extern void vectorMovement3D(Vector3 v, double plusx, double plusy, double plusz)\n',

                '[<DllImport("compiledVectors")>]\n',
                'extern Vector3 midpoint3D(Vector3 v, Vector3 v2)\n',

                '[<DllImport("compiledVectors")>]\n',
                'extern double percentDistance3D(Vector3 pos1, Vector3 pos2, double percent)\n']
    for eachimports in imports3D:
        Header3D.write(eachimports)
    Header3D.flush()

elif platform == "win32":
    if os.path.exists(args.path+"FSHeader2D.fs"):
        pass
    else:
        Header2D = open(args.path+"FSHeader2D.fs", "w")
        imports2D = ["module vector2\n",
                'open System.Runtime.InteropServices\n',

                '[<StructLayout(LayoutKind.Sequential)>]\n',
                'type Vector2 = val mutable X: double; val mutable Y: double new(x, y) = { X = x; Y = y}\n',

                '[<DllImport("compiledVectors.exe")>]\n',
                'extern Vector2 CreateVector2D(double x, double y)\n',

                '[<DllImport("compiledVectors.exe")>]\n',
                'extern double distanceTo2D(Vector2 v,Vector2 v2)\n',

                '[<DllImport("compiledVectors.exe")>]\n',
                'extern void vectorMovement2D(Vector2 v,double plusx, double plusy)\n',

                '[<DllImport("compiledVectors.exe")>]\n',
                'extern Vector2 midpoint2D(Vector2 v,Vector2 v2)\n',

                '[<DllImport("compiledVectors.exe")>]\n',
                'extern double percentDistance2D(Vector2 pos1, Vector2 pos2, double percent)\n']
        for eachimports in imports2D:
            Header2D.write(eachimports)
            Header2D.flush()
        Header3D = open(args.path+"FSHeader3D.fs", "w")
        imports3D = ["module vector3\n",
                'open System.Runtime.InteropServices\n',

                '[<StructLayout(LayoutKind.Sequential)>]\n',
                'type Vector3 = val mutable X: double; val mutable Y:double; val mutable Z: double new(x, y, z) = { X = x; Y = y; Z=z }\n',

                '[<DllImport("compiledVectors.exe")>]\n',
                'extern Vector3 CreateVector3D(double x, double y, double z)\n',

                '[<DllImport("compiledVectors.exe")>]\n',
                'extern double distanceTo3D(Vector3 v, Vector3 v2)\n',

                '[<DllImport("compiledVectors.exe")>]\n',
                'extern void vectorMovement3D(Vector3 v, double plusx, double plusy, double plusz)\n',

                '[<DllImport("compiledVectors.exe")>]\n',
                'extern Vector3 midpoint3D(Vector3 v, Vector3 v2)\n',

                '[<DllImport("compiledVectors.exe")>]\n',
                'extern double percentDistance3D(Vector3 pos1, Vector3 pos2, double percent)\n']
        for eachimports in imports3D:
            Header3D.write(eachimports)
        Header3D.flush()

# reading the user's F# file and append the opening of vector2 if it does not exists
with open(args.path+"Program.fs", "r+") as program:
    contents = program.readlines()
    if "open vector2\n" in contents:
        pass
    else:
        contents.insert(0, "open vector2\n")
    if "open vector3\n" in contents:
        pass
    else:
        contents.insert(0, "open vector3\n")

with open(args.path+"Program.fs", "r+") as program:
    program.writelines(contents)


# search for the project file to add the new FSHeader2D file in its items
fsproj = next(Path("./").glob("*.fsproj"))
if os.path.exists(fsproj):
    with open(fsproj, "r+") as out_file:
        lines = out_file.readlines()
        for i, line in enumerate(lines):
            if "<ItemGroup>" in line and not any("<Compile Include=\"FSHeader2D.fs\"/>" in line for line in lines):
                index = lines.index("  <ItemGroup>\n")
                lines.insert(
                   index+1, '    <Compile Include="FSHeader2D.fs"/>\n')

            if "<ItemGroup>" in line and not any("<Compile Include=\"FSHeader3D.fs\"/>" in line for line in lines):
                index = lines.index("  <ItemGroup>\n")
                lines.insert(
                   index+1, '    <Compile Include="FSHeader3D.fs"/>\n')

            if any("<Compile Include=\"FSHeader2D.fs\"/>" in line for line in lines) and any("<Compile Include=\"FSHeader3D.fs\"/>" in line for line in lines):
                with open(fsproj, "w") as out_file:
                   out_file.writelines(lines)
                   out_file.flush()
                break


else:
    sys.exit(
        "The file have not been found, please verify the location of your project file (.fsproj)")


# run user's F# project
subprocess.run(["dotnet", "run"])
