CppFile = open("./test.cpp", "r")
read = CppFile.readlines()
CppFile = open("./test.cpp", "a")


def createStruct(arrays, name):
    if not all(isinstance(x, list) for x in arrays):
        raise TypeError("Input must be an array of arrays.")
    values = ""
    for eachArray in arrays:
        values += eachArray[1]+" " + eachArray[0]+";\n"
    # CppFile.write("class "+name+"")
    CppFile.write("int main()\n{\n" +
                  "return 0;\n}\n" +
                  "class "+name+"\n{\n" +
                  "public:\n" +
                  values +
                  "};")


arrays = [["string", "int"], ["number", "float"], ["reverse", "bool"]]

createStruct(arrays, "NewStruct")
