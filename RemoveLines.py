# import pandas as pd
#
# df = pd.read_csv(r'C:\Users\aprabhakar\Desktop\snakes\sorter\CleanCombinedFileEdited.txt', skipfooter = 200000)
# df.to_csv(r'C:\Users\aprabhakar\Desktop\snakes\sorter\lastlines.txt')

with open(r'C:\Users\aprabhakar\Desktop\snakes\sorter\CleanCombinedFileEdited.txt',encoding="utf8") as f1:
    lines = f1.readlines()

with open(r'C:\Users\aprabhakar\Desktop\snakes\sorter\lastlines.txt', 'w+',encoding="utf8") as f2:
    f2.writelines(lines[:-244781])