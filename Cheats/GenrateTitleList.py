import os
import re
print(os.getcwd())

base_path=os.getcwd()
file_path=os.walk(base_path)
save_path = base_path+'\\cheatlist.txt'
fw = open(save_path, "w")

def write_cheattitle(path):
        for root, dirs, files in path:
                if base_path+'\\' in root:
                        print(root.replace(base_path+'\\','')+':'+files[0])
                        fw.write(root.replace(base_path+'\\','')+':'+files[0]+"\n")
write_cheattitle(file_path)
