import os
import sys
import sys 
from sys import platform
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="The path of your directory")
args = parser.parse_args()

# remove every C++ files already existing
if os.path.exists(args.path+"Program.fs"):
    pass
else:
    sys.exit("The file have not been found, please verify the location of your Program.fs")

if os.path.exists(args.path+"Vector2.cpp"):
    os.remove(args.path+"Vector2.cpp")

if os.path.exists(args.path+"compiledVector2"):
    os.remove(args.path+"compiledVector2")

if os.path.exists(args.path+"compiledVector2.exe"):
    os.remove(args.path+"compiledVector2.exe")

# Generate the C++ file for 2D vectors basic calculations 
f= open(args.path+"Vector2.cpp","x")
f.write("#include <math.h>\n"+
    "#include <iostream>\n"+
    "using namespace std;\n"+
        "int main() \n"+
    "{\n"+
    "   return 0;\n"+
    "}\n"+
    "class Vector2\n"+
    "{\n"+
    "public:\n"+
        "double X;\n"+
        "double Y;\n"+
        "Vector2(double x, double y) : X(x), Y(y){}\n"+
    "};\n"+

    'extern "C" Vector2* CreateVector2(double x, double y)\n'+
    "{\n"+
        "return new Vector2(x, y);\n"+
    "}\n"+
    'extern "C" double GetX(Vector2 *v)\n'+
    "{\n"+
        "return v->X;\n"+
    "}\n"+

    'extern "C" double GetY(Vector2 *v)\n'+
    "{\n"+
        "return v->Y;\n"+
    "}\n"+

    'extern "C" double distanceTo(Vector2 *pos1, Vector2 *pos2)\n'+
    "{\n"+
        "return sqrt((pos1->Y - pos2->Y) * (pos1->Y - pos2->Y) + (pos1->X - pos2->X) * (pos1->X - pos2->X));\n"+
    "}\n"+

    'extern "C" void vectorMovement(Vector2* vector, double plusx, double plusy)\n'+
    "{\n"+
        "vector->X += plusx;\n"+
        "vector->Y += plusy;\n"+
        "return;\n"+
    "}\n"+
    'extern "C" Vector2 *midpoint(Vector2* pos1, Vector2* pos2)\n'+
    "{\n"+
        "double mx = (pos1->X + pos2->X) / 2; \n"+
        "double my = (pos1->Y + pos2->Y) / 2; \n"+
        
        "return CreateVector2(mx, my);\n"+
    "}\n"+

    'extern "C" double percentDistance(Vector2* pos,Vector2* pos2, double percentOfDistance) {\n'+
            "return distanceTo(pos,pos2)/ (100 / percentOfDistance);\n"+
        "}")

# flush is telling to the computer's memory to write the file right now,
# instead of waiting the end of the script to do it.
f.flush()        

# compiling the C++ file
def compile_cpp(file_path):
    if platform == "darwin": #macOs
        subprocess.run(["g++", "-o","compiledVector3",file_path])
    elif platform == "win32": #Windows
        subprocess.run(["g++", "-shared" ,"-o","compiledVector2.exe", "-m64", file_path])

compile_cpp(args.path+"Vector2.cpp")


# storing every functions import inside an array
importsMac=['open System.Runtime.InteropServices\n',
        "[<StructLayout(LayoutKind.Sequential)>]\n",
        "type Vector2 = val mutable X: double; val mutable Y: double new(x, y, z) = { X = x; Y = y}\n",
        '[<DllImport("compiledVector2")>]\n',
        "extern Vector2 CreateVector2(double x, double y)\n",

        '[<DllImport("compiledVector2")>]\n',
        "extern double GetX(Vector2 v)\n",

        '[<DllImport("compiledVector2")>]\n',
        "extern double GetY(Vector2 v)\n",

        '[<DllImport("compiledVector2")>]\n',
        "extern double distanceTo(Vector2 v,Vector2 v2)\n",

        '[<DllImport("compiledVector2")>]\n',
        "extern void vectorMovement(Vector2 v,double plusx, double plusy)\n",

        '[<DllImport("compiledVector2")>]\n',
        "extern Vector2 midpoint(Vector2 v,Vector2 v2)\n",

        '[<DllImport("compiledVector2>]\n',
        "extern double percentDistance(Vector2 pos1, Vector2 pos2, double percent)\n"]

importsWindows=['open System.Runtime.InteropServices\n',
        "[<StructLayout(LayoutKind.Sequential)>]\n",
        "type Vector2 = val mutable X: double; val mutable Y: double new(x, y, z) = { X = x; Y = y}\n",
        'printfn("test 1 passed")\n',
        '[<DllImport("compiledVector2.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern Vector2 CreateVector2(double x, double y)\n",

        '[<DllImport("compiledVector2.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern double GetX(Vector2 v)\n",

        '[<DllImport("compiledVector2.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern double GetY(Vector2 v)\n",

        '[<DllImport("compiledVector2.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern double distanceTo(Vector2 v,Vector2 v2)\n",

        '[<DllImport("compiledVector2.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern void vectorMovement(Vector2 v,double plusx, double plusy)\n",

        '[<DllImport("compiledVector2.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern Vector2 midpoint(Vector2 v,Vector2 v2)\n",

        '[<DllImport("compiledVector2.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern double percentDistance(Vector2 pos1, Vector2 pos2, double percent)\n",
        'printfn("test 2 passed")\n'
        ]
# reading the user's F# file
program=open(args.path+"Program.fs","r")
FileLength=program.readlines()
program=open(args.path+"Program.fs","w")

# if the user is on macOs, add macOs imports
if platform == "darwin":
    # Copy every lines of the original file into an array
    exists=[]
    for line in FileLength: 
        exists.append(line) 

    # Delete every line inside the program
    program.truncate()
    program=open(args.path+"Program.fs","a")

    # Write every imports into the file
    for eachImport in importsMac:
        program.write(eachImport)

    # insert back every lines the user has written, except already added lines (ex:[<DllImport("compiledVector2")>])
    for lines in exists:
        if lines in importsMac:
            pass
        else:
            program.write(lines)

elif platform == "win32":
    exists=[]
    for line in FileLength:
        exists.append(line)

    program.truncate()
    program=open(args.path+"Program.fs","a")

    for eachImport in importsWindows:
        program.write(eachImport)

    for lines in exists:
        if lines in importsWindows:
            pass
        else:
            program.write(lines)

program.flush()
# run user's F# project
subprocess.run(["dotnet","run"])