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
        aura=parts[3]
        print("the eroor is in the line",aura)




    
