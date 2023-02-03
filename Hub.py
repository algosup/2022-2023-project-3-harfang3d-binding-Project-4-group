import argparse
import subprocess

# This file serve as a hub for every gen.py written for F#,
# depending on the argument you will use to call this file,
# it will execute a specific file with its own functions.

# To have more informations about how to use this file,
# type "python3 Hub.py -h" in your terminal.
parser = argparse.ArgumentParser(
                    prog = 'Hub.py',
                    description = 'This script serve as a hub for every generator written for f#,'+
                                    'depending on the argument you will use to call this file'+
                                    'it will execute a specific file with its own functions.')


def call(gen:str, path:str):
    match gen:
        case "v2":
            subprocess.run(["python3","./CppToFs/Vector2/gen.py", path])
        case "v3":
            print("not yet")

generators = {'v2',
                'v3'}

parser.add_argument('-gen', "--generator", help="Choose which generator you want to call for your program", type=str, required=True)
parser.add_argument("path", default="./", type=str, help="The path of your Program.fs")
args = parser.parse_args()

if args.generator in generators:
    call(args.generator,args.path)
else:
    print("unknown generator has been entered,\nplease enter one of the following:\n- vector2,\n- vector3")
