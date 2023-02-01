import os
import subprocess

if os.path.exists("Vector2.cpp"):
    os.remove("Vector2.cpp")

if os.path.exists("compiledVector2"):
    os.remove("compiledVector2")

f= open("Vector2.cpp","x")
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
f.flush()        

def compile_cpp(file_path):
    subprocess.run(["g++", "-o","compiledVector2",file_path])

compile_cpp("Vector2.cpp")


program=open("Program.fs","r")
lines=program.readlines()
program=open("Program.fs","w")
done=False

imports=['open System.Runtime.InteropServices\n',
        "[<StructLayout(LayoutKind.Sequential)>]\n",
        "type Vector2 =\n",
        "    val mutable X: double\n",
        "    val mutable Y: double\n",
        "    new(x, y, z) = { X = x; Y = y}\n",
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

        '[<DllImport("compiledVector2")>]\n',
        "extern double percentDistance(Vector2 pos1, Vector2 pos2, double percent)\n"]
i=0
exists=[]
for line in lines:
    
    exists.append(line)

    if i<len(imports) and done==False:
        program.write(imports[i])
    
    i+=1
for lines in exists:
    if lines in imports:
        pass
    else:
        program.write(lines)

program.flush()
subprocess.run(["dotnet","run"])