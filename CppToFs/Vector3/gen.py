import os
import subprocess
import sys
from sys import platform
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="The path of your directory")
args = parser.parse_args()

if os.path.exists(args.path+"Program.fs"):
    pass
else:
    sys.exit("The file have not been found, please verify the location of your Program.fs")

if os.path.exists(args.path+"Vector3.cpp"):
    os.remove(args.path+"Vector3.cpp")

if os.path.exists(args.path+"compiledVector3"):
    os.remove(args.path+"compiledVector3")

#Create Vector3.cpp file who define the Vector3 class and the functions
f= open(args.path+"Vector3.cpp","x")
f.write("#include <math.h>\n"+
    "#include <iostream>\n"+
    "using namespace std;\n"+
        "int main() \n"+
    "{\n"+
    "   return 0;\n"+
    "}\n"+
    "class Vector3\n"+
    "{\n"+
    "public:\n"+
        "double X;\n"+
        "double Y;\n"+
        "double Z;\n"+
        "Vector3(double x, double y, double z) : X(x), Y(y), Z(z) {}\n"+
    "};\n"+

    'extern "C" Vector3* CreateVector3(double x, double y, double z)\n'+
    "{\n"+
        "return new Vector3(x, y, z);\n"+
    "}\n"+
    'extern "C" double GetX(Vector3 *v)\n'+
    "{\n"+
        "return v->X;\n"+
    "}\n"+

    'extern "C" double GetY(Vector3 *v)\n'+
    "{\n"+
        "return v->Y;\n"+
    "}\n"+

    'extern "C" double GetZ(Vector3 *v)\n'+
    "{\n"+
        "return v->Z;\n"+
    "}\n"+

    'extern "C" double distanceTo(Vector3 *pos1, Vector3 *pos2)\n'+
    "{\n"+
        "return sqrt((pos1->Y - pos2->Y) * (pos1->Y - pos2->Y) + (pos1->X - pos2->X) * (pos1->X - pos2->X) + (pos1->Z - pos2->Z) * (pos1->Z - pos2->Z));\n"+
    "}\n"+

    'extern "C" void vectorMovement(Vector3* vector, double plusx, double plusy, double plusz)\n'+
    "{\n"+
        "vector->X += plusx;\n"+
        "vector->Y += plusy;\n"+
        "vector->Z += plusz;\n"+
        "return;\n"+
    "}\n"+
    'extern "C" Vector3 *midpoint(Vector3* pos1, Vector3* pos2)\n'+
    "{\n"+
        "double mx = (pos1->X + pos2->X) / 2; \n"+
        "double my = (pos1->Y + pos2->Y) / 2; \n"+
        "double mz = (pos1->Z + pos2->Z) / 2; \n"+
        
        "return CreateVector3(mx, my, mz);\n"+
    "}\n"+

    'extern "C" double percentDistance(Vector3* pos,Vector3* pos2, double percentOfDistance) {\n'+
            "return distanceTo(pos,pos2)/ (100 / percentOfDistance);\n"+
        "}")
f.flush()        

# Compile Vector3.cpp
def compile_cpp(file_path):
    if platform == "darwin": #macOs
        subprocess.run(["g++", "-o","compiledVector3",file_path])
    elif platform == "win32": #Windows
        subprocess.run(["g++", "-shared" ,"-o","compiledVector3.exe", "-m64", file_path])

compile_cpp(args.path+"Vector3.cpp")


importsMac=['open System.Runtime.InteropServices\n',
        "[<StructLayout(LayoutKind.Sequential)>]\n",
        "type Vector3 =val mutable X: double; val mutable Y: double; val mutable Z: double new(x, y, z) = { X = x; Y = y; Z = z }\n",
        '[<DllImport("compiledVector3")>]\n',
        "extern Vector3 CreateVector3(double x, double y, double z)\n",

        '[<DllImport("compiledVector3")>]\n',
        "extern double GetX(Vector3 v)\n",

        '[<DllImport("compiledVector3")>]\n',
        "extern double GetY(Vector3 v)\n",

        '[<DllImport("compiledVector3")>]\n',
        "extern double GetZ(Vector3 v)\n",

        '[<DllImport("compiledVector3")>]\n',
        "extern double distanceTo(Vector3 v,Vector3 v2)\n",

        '[<DllImport("compiledVector3")>]\n',
        "extern void vectorMovement(Vector3 v,double plusx, double plusy, double plusz)\n",

        '[<DllImport("compiledVector3")>]\n',
        "extern Vector3 midpoint(Vector3 v,Vector3 v2)\n",

        '[<DllImport("compiledVector3")>]\n',
        "extern double percentDistance(Vector3 pos1, Vector3 pos2, double percent)\n"]

importsWindows=['open System.Runtime.InteropServices\n',
        "[<StructLayout(LayoutKind.Sequential)>]\n",
        "type Vector3 = val mutable X: double; val mutable Y: double; val mutable Z: double new(x, y, z) = { X = x; Y = y; Z = z }\n",
        'printfn("Test 1 passed")\n',
        '[<DllImport("compiledVector3.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern Vector3 CreateVector3(double x, double y, double z)\n",

        '[<DllImport("compiledVector3.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern double GetX(Vector3 v)\n",

        '[<DllImport("compiledVector3.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern double GetY(Vector3 v)\n",

        '[<DllImport("compiledVector3.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern double GetZ(Vector3 v)\n",

        '[<DllImport("compiledVector3.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern double distanceTo(Vector3 v,Vector3 v2)\n",

        '[<DllImport("compiledVector3.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern void vectorMovement(Vector3 v,double plusx, double plusy, double plusz)\n",

        '[<DllImport("compiledVector3.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern Vector3 midpoint(Vector3 v,Vector3 v2)\n",

        '[<DllImport("compiledVector3.exe", CallingConvention = CallingConvention.StdCall)>]\n',
        "extern double percentDistance(Vector3 pos1, Vector3 pos2, double percent)\n",
        'printfn("Test 2 passed")\n'
        ]

# Edit Program.fs file to add the imports
program=open(args.path+"Program.fs","r")
FileLength=program.readlines()
program=open(args.path+"Program.fs","w")

# Depending on the OS, the imports are different, we need to add the DLL imports to the Program.fs file
if platform == "darwin": # mac

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
    
elif platform == "win32": # windows
    exists=[]
    for line in FileLength: 
        exists.append(line) 

    # Delete every line inside the program
    program.truncate()
    program=open(args.path+"Program.fs","a")

    # Write every imports into the file
    for eachImport in importsWindows:
        program.write(eachImport)

    # insert back every lines the user has written, except already added lines (ex:[<DllImport("compiledVector2")>])
    for lines in exists:
        if lines in importsWindows:
            pass
        else:
            program.write(lines)

program.flush()
# Run the updated Program.fs file
subprocess.run(["dotnet","run"])