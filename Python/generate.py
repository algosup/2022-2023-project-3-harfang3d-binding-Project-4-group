
import subprocess

code = r'''
#include <stdio.h>
int main() {
  for(int i=0;i<5;i++) {
    printf("Testing %d\n",i);
  }
  return 0;
}
'''

f_cpp = "test.cpp"
with open(f_cpp,'w') as FOUT:
    FOUT.write(code)

# Compile the program
f_exec = "./myprogram"
compile_cmd = "gcc {} -o {}".format(f_cpp, f_exec)
subprocess.call(compile_cmd, shell=True)

# Run the program
p = subprocess.Popen(f_exec, shell=True,
                     stdin=subprocess.PIPE, 
                     stdout=subprocess.PIPE)

# Step through the output 
for line in p.stdout:
    print(line)