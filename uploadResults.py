import boto3
import os

filePaths = []
fileNames = []
fileNumber = 0
i = 0
s3 = boto3.resource('s3')
# Change the path below to where images are
for (dirpath, dirnames, filenames) in os.walk(r'C:\Users\aprabhakar\Desktop\snakes\testDAT\Processed'):
    for f in filenames:
        filePaths.append(os.path.join(dirpath, f))
        fileNames.append(f)
        fileNumber = fileNumber + 1

while i != fileNumber:
    s3.meta.client.upload_file(filePaths[i], 'googlevision-results', fileNames[i])
    i = i + 1


print(fileNames)
print(fileNumber)