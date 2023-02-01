import os
import subprocess
from sys import platform

if os.path.exists("Vector3.cpp"):
    os.remove("Vector3.cpp")

if os.path.exists("compiledVector3"):
    os.remove("compiledVector3")

if os.path.exists("compiledVector3.dll"):
    os.remove("compiledVector3.dll")

f= open("Vector3.cpp","x")
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

def compile_cpp(file_path):
    if platform == "darwin":
        subprocess.run(["g++", "-o","compiledVector3",file_path])
    elif platform == "win32":
        subprocess.run(["g++", "-shared" ,"-o","compiledVector3.dll",file_path])

compile_cpp("Vector3.cpp")


program=open("Program.fs","r")
lines=program.readlines()
program=open("Program.fs","w")
done=False

importsMac=['open System.Runtime.InteropServices\n',
        "[<StructLayout(LayoutKind.Sequential)>]\n",
        "type Vector3 =\n",
        "    val mutable X: double\n",
        "    val mutable Y: double\n",
        "    val mutable Z: double\n",
        "    new(x, y, z) = { X = x; Y = y; Z = z }\n",
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
        "type Vector3 =\n",
        "    val mutable X: double\n",
        "    val mutable Y: double\n",
        "    val mutable Z: double\n",
        "    new(x, y, z) = { X = x; Y = y; Z = z }\n",
        '[<DllImport("compiledVector3.dll")>]\n',
        "extern Vector3 CreateVector3(double x, double y, double z)\n",

        '[<DllImport("compiledVector3.dll")>]\n',
        "extern double GetX(Vector3 v)\n",

        '[<DllImport("compiledVector3.dll")>]\n',
        "extern double GetY(Vector3 v)\n",

        '[<DllImport("compiledVector3.dll")>]\n',
        "extern double GetZ(Vector3 v)\n",

        '[<DllImport("compiledVector3.dll")>]\n',
        "extern double distanceTo(Vector3 v,Vector3 v2)\n",

        '[<DllImport("compiledVector3.dll")>]\n',
        "extern void vectorMovement(Vector3 v,double plusx, double plusy, double plusz)\n",

        '[<DllImport("compiledVector3.dll")>]\n',
        "extern Vector3 midpoint(Vector3 v,Vector3 v2)\n",

        '[<DllImport("compiledVector3.dll")>]\n',
        "extern double percentDistance(Vector3 pos1, Vector3 pos2, double percent)\n"]

if platform == "darwin":
    i=0
    exists=[]
    for line in lines:
        
        exists.append(line)

        if i<len(importsMac) and done==False:
            program.write(importsMac[i])
        
        i+=1
    for lines in exists:
        if lines in importsMac:
            pass
        else:
            program.write(lines)
elif platform == "win32":
    i=0
    exists=[]
    for line in lines:
        
        exists.append(line)

        if i<len(importsWindows) and done==False:
            program.write(importsWindows[i])
        
        i+=1
    for lines in exists:
        if lines in importsWindows:
            pass
        else:
            program.write(lines)

program.flush()
subprocess.run(["dotnet","run"])