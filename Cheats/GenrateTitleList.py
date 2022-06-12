import os
import json
import re
print(os.getcwd())

#Base folder
base_path=os.getcwd()
#English folder
en_base_path=base_path+'\\En'
#Chinese folder
zh_base_path=base_path+'\\Zh'


#English output file
save_en_path = base_path + '\\cheatlist_en.txt'

#Chinese output file
save_zh_path = base_path + '\\cheatlist_zh.txt'

def write_cheattitle(baselanpath,savepath,area):
        fw=open(savepath, "w", encoding="utf-8")
        file_path = os.walk(baselanpath)
        first = True
        fw.write('{"cheats":[')
        for root, dirs, files in file_path:
                try:
                        if baselanpath+'\\' in root:
                                text=files[0]
                                destitle='"title":"'+root.replace(baselanpath+'\\','')+'"'
                                cheattitle='"cheat":"'+text+'"'
                                lanarea='"area":"'+area+'"'
                                if first:
                                        first=False
                                        fw.write('{'+destitle+','+cheattitle+','+lanarea+'}')
                                else:
                                        fw.write(',{'+destitle+','+cheattitle+','+lanarea+'}')
                except:
                        print (root)

        fw.write(']}')




write_cheattitle(en_base_path,save_en_path,"En")
write_cheattitle(zh_base_path,save_zh_path,"Zh")


