import subprocess
output=subprocess.run(["python","test_programm.py"],capture_output=True,text=True)
print(output.stderr)
print(output.stdout)
print("return code:",output.returncode)
eroor=output.stderr
print("orrisis detected")
print(eroor)
if "ERROR" in eroor:
    print("orasis detected an eroor")
    
lastline=eroor.splitlines()[-1]
eroor_type=lastline.split(":")[0]
print("eroor type is",eroor_type)


lines=eroor.splitlines()
for line in lines:
    if "line" in line:
        parts=line.split()
        print(parts)
        print(parts[3])
        line_number = int(parts[3].strip(":,."))
        print("the eroor is in the line",line_number)

        f=open("test_programm.py",'r')
        lines=f.readlines()
        broken_code=lines[line_number-1]
        print("the eroor is",broken_code)

if eroor_type=="TypeError":
    print("an eroor was performed with incompatible data type")



    
