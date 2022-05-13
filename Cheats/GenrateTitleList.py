import os
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


def write_cheattitle(baselanpath,savepath):
        fw=open(savepath, "w", encoding="utf-8")
        file_path = os.walk(baselanpath)
        for root, dirs, files in file_path:
                if baselanpath+'\\' in root:
                        text=files[0]
                        print(root.replace(baselanpath+'\\','')+':'+text)
                        t=root.replace(baselanpath+'\\','')+':'+text+"\n"
                        fw.write(t)



write_cheattitle(en_base_path,save_en_path)
write_cheattitle(zh_base_path,save_zh_path)


