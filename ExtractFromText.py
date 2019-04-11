import os
import re

directory = r"C:\Users\aprabhakar\Desktop\snakes\sorter"
os.chdir(directory)

f = open("FinalText.txt", encoding="utf8")
f2 = open("Excellines.txt", "w+", encoding="utf8")
f3 = open("lastlines.txt", encoding="utf8")
for line, line2 in zip(f,f3):
    getLine = re.search("Line(.[^,]*)", line)
    getLineNumber = re.search("\d+", getLine[0])
    getOther = re.search("OTHER(.[^}]*)", line)
    getStorage = re.search("STORAGE(.[^}]*)", line)
    getOtherScore = re.search("\d+\.\d+", getOther[0])
    getStorageScore = re.search("\d+\.\d+", getStorage[0])
    # getRealData = line.split(",")[-1]
    # excelLine = getLineNumber[0] + '\t' + getOtherScore[0] + '\t' + getStorageScore[0] + '\t' + getRealData + '\t\n'
    # print(excelLine)
    # print(getRealData)
    excelLine = getLineNumber[0] + '\t' + getOtherScore[0] + '\t' + getStorageScore[0] + '\t' + line2
    f2.write(excelLine)
    # f2.write(getLineNumber[0])
    # f2.write('\t')
    # f2.write(getOtherScore[0])
    # f2.write('\t')
    # f2.write(getStorageScore[0])


f.close()
f2.close()

# OTHER(.[^}]*)