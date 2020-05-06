from com.wp.test.TranslateApi import *
import os

filepath = os.path.abspath(os.path.join(os.getcwd(), "../../.."))

def translateFile():
    t = MyTranslate(YouDaoInterface())
    with open(filepath + "/files/chinese.txt","r",encoding="utf-8") as fr:
        for line in fr.readlines():
            line = line.replace("。", ".")
            print(t.translate(line))
            saveFile(t.translate(line))
        fr.close()

def saveFile(context):
    with open(filepath + "/files/english.txt","a+",encoding="utf-8") as fw:
        fw.write(context + "\n")
        fw.close()

if __name__ == '__main__':
    translateFile()


