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
    sys.exit("The file have not been found, please verify the location of your Program.fs")

    
    
if os.path.exists(args.path+"compiledVector2"):
    os.remove(args.path+"compiledVector2")

if os.path.exists(args.path+"compiledVector2.exe"):
    os.remove(args.path+"compiledVector2.exe")
    

# compiling the related C++ file
def compile_cpp(file_path):
    if platform == "darwin": #macOs
        subprocess.run(["g++", "-o","compiledVector2",file_path])
    elif platform == "win32": #Windows
        subprocess.run(["g++", "-shared" ,"-o","compiledVector2.exe", "-m64", file_path])

compile_cpp("../../CppToFs/Vector2/Vector2.cpp")

if os.path.exists(args.path+"FSHeader.fs"):
    os.remove(args.path+"FSHeader.fs")
else:
    pass
if platform == "darwin":
        header=open(args.path+"FSHeader.fs","w")
        imports=["module vector2\n",
                'open System.Runtime.InteropServices\n',

                '[<StructLayout(LayoutKind.Sequential)>]\n',
                'type Vector2 = val mutable X: double; val mutable Y: double new(x, y) = { X = x; Y = y}\n',
                
                '[<DllImport("compiledVector2")>]\n',
                'extern Vector2 CreateVector2(double x, double y)\n',

                '[<DllImport("compiledVector2")>]\n',
                'extern double distanceTo(Vector2 v,Vector2 v2)\n',

                '[<DllImport("compiledVector2")>]\n',
                'extern void vectorMovement(Vector2 v,double plusx, double plusy)\n',

                '[<DllImport("compiledVector2")>]\n',
                'extern Vector2 midpoint(Vector2 v,Vector2 v2)\n',

                '[<DllImport("compiledVector2")>]\n',
                'extern double percentDistance(Vector2 pos1, Vector2 pos2, double percent)\n']
        for eachImports in imports:
            header.write(eachImports)
        header.flush()

elif platform=="win32":
    if path.exists(args.path+"FSHeader.fs"):
        pass
    else:
        header.write("module vector2\n",
            'open System.Runtime.InteropServices\n',
            
            "[<StructLayout(LayoutKind.Sequential)>]\n",
            "type Vector2 = val mutable X: double; val mutable Y: double new(x, y) = { X = x; Y = y}\n",
            'printfn("test 1 passed")\n',
            
            '[<DllImport("compiledVector2.exe", CallingConvention = CallingConvention.StdCall)>]\n',
            "extern Vector2 CreateVector2(double x, double y)\n",

            '[<DllImport("compiledVector2.exe", CallingConvention = CallingConvention.StdCall)>]\n',
            "extern double distanceTo(Vector2 v,Vector2 v2)\n",

            '[<DllImport("compiledVector2.exe", CallingConvention = CallingConvention.StdCall)>]\n',
            "extern void vectorMovement(Vector2 v,double plusx, double plusy)\n",

            '[<DllImport("compiledVector2.exe", CallingConvention = CallingConvention.StdCall)>]\n',
            "extern Vector2 midpoint(Vector2 v,Vector2 v2)\n",

            '[<DllImport("compiledVector2.exe", CallingConvention = CallingConvention.StdCall)>]\n',
            "extern double percentDistance(Vector2 pos1, Vector2 pos2, double percent)\n",
            
            'printfn("test 2 passed")\n')

# reading the user's F# file and append the opening of vector2 if it does not exists
with open(args.path+"Program.fs","r+") as program:
    contents = program.readlines()
    if "open vector2\n" in contents:
        pass
    else:
        contents.insert(0, "open vector2\n")

with open(args.path+"Program.fs","r+") as program:
    program.writelines(contents)



# search for the project file to add the new FSHeader file in its items
fsproj= next(Path("./").glob("*.fsproj"))
if os.path.exists(fsproj):
    with open(fsproj, "r+") as out_file:
        lines=out_file.readlines()
        for i, line in enumerate(lines):
            if "<ItemGroup>" in line and not any("<Compile Include=\"FSHeader.fs\"/>" in line for line in lines):
                    print(line)
                    index = lines.index("  <ItemGroup>\n")
                    lines.insert(index+1,'    <Compile Include="FSHeader.fs"/>\n')
                    with open(fsproj, "w") as out_file:
                        out_file.writelines(lines)
                        out_file.flush()
                    break
            
            
else:
    sys.exit("The file have not been found, please verify the location of your project file (.fsproj)")


# run user's F# project
subprocess.run(["dotnet","run"])