import os

directory = r"C:\Users\aprabhakar\Desktop\snakes\testDAT\allfiles"
os.chdir(directory)

for (dirpath, dirnames, filenames) in os.walk(directory):
    print("hello")


with open(r'C:\Users\aprabhakar\Desktop\snakes\testDAT\temp\CombinedFile2.txt', 'w+', encoding="utf8") as outfile:
    for fname in filenames:
        with open(str(fname),encoding="utf8") as infile:
            for line in infile:
                outfile.write(line)
        outfile.write('\n')