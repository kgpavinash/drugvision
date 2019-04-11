import os
import re

directory = r"C:\Users\aprabhakar\Desktop\snakes\sorter"
os.chdir(directory)

f = open("predictions2.jsonl")
for line in f:
    print(line)
    getOther = re.search("STORAGE(.[^}]*)", line)
    break

print(getOther[0])
getOtherScore = re.search("\d+\.\d+", getOther[0])
print(getOtherScore[0])
# ans = re.findall("\d+\.\d+", getOther[0])
# print(ans[0])


f.close()

# OTHER(.[^}]*)