import os
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="The path of your Program.fs")
args = parser.parse_args()

# remove every C++ files already existing
if os.path.exists(args.path,"program.fs"):
    pass
else:
    sys.exit("The file have not been found, please verify the location of your Program.fs")

if os.path.exists(args.path,"Vector2.cpp"):
    os.remove(args.path,"Vector2.cpp")

if os.path.exists(args.path,"compiledVector2"):
    os.remove(args.path,"compiledVector2")

# Generate the C++ file for 2D vectors basic calculations 
f= open(args.path,"Vector2.cpp","x")
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
    subprocess.run(["g++", "-o",args.path,"compiledVector2",file_path])

compile_cpp(args.path,"Vector2.cpp")

# reading the user's F# file
program=open(args.path,"Program.fs","r")
lines=program.readlines()
program=open(args.path,"Program.fs","w")
done=False

# storing every functions import inside an array
imports=['open System.Runtime.InteropServices\n',
        "[<StructLayout(LayoutKind.Sequential)>]\n",
        "type Vector2 =\n",
        "    val mutable X: double\n",
        "    val mutable Y: double\n",
        "    new(x, y, z) = { X = x; Y = y}\n",
        '[<DllImport(args.path,"compiledVector2")>]\n',
        "extern Vector2 CreateVector2(double x, double y)\n",

        '[<DllImport(args.path,"compiledVector2")>]\n',
        "extern double GetX(Vector2 v)\n",

        '[<DllImport(args.path,"compiledVector2")>]\n',
        "extern double GetY(Vector2 v)\n",

        '[<DllImport(args.path,"compiledVector2")>]\n',
        "extern double distanceTo(Vector2 v,Vector2 v2)\n",

        '[<DllImport(args.path,"compiledVector2")>]\n',
        "extern void vectorMovement(Vector2 v,double plusx, double plusy)\n",

        '[<DllImport(args.path,"compiledVector2")>]\n',
        "extern Vector2 midpoint(Vector2 v,Vector2 v2)\n",

        '[<DllImport(args.path,"compiledVector2")>]\n',
        "extern double percentDistance(Vector2 pos1, Vector2 pos2, double percent)\n"]

# adding every imports inside the user's file and storing the file's original lines,
# while removing everything
i=0
exists=[]
for line in lines:
    
    exists.append(line)

    if i<len(imports) and done==False:
        program.write(imports[i])
    
    i+=1
# insert back every lines the user has written, except already added lines (ex:[<DllImport(args.path,"compiledVector2")>])
for lines in exists:
    if lines in imports:
        pass
    else:
        program.write(lines)

program.flush()
# run user's F# project
subprocess.run(["dotnet","run"])



