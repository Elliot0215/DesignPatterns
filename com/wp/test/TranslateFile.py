from com.wp.test.TranslateApi import *

def translateFile():
    t = MyTranslate(YouDaoInterface())
    with open("D:\\Desktop\\123\\chinese.txt","r",encoding="utf-8") as fr:
        for line in fr.readlines():
            line = line.replace("。", ".")
            print(t.translate(line))
            saveFile(t.translate(line))
        fr.close()

def saveFile(context):
    with open("D:\\Desktop\\123\\english.txt","a+",encoding="utf-8") as fw:
        fw.write(context + "\n")
        fw.close()

if __name__ == '__main__':
    translateFile()


