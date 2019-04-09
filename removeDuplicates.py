with open(r'C:\Users\aprabhakar\Desktop\snakes\sorter\CombinedFile.txt',encoding="utf8") as result:
    uniqlines = set(result.readlines())
    with open(r'C:\Users\aprabhakar\Desktop\snakes\sorter\CleanCombinedFile.txt', 'w+',encoding="utf8") as rmdup:
        rmdup.writelines(set(uniqlines))