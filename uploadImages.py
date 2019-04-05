import os
import io
import boto3
from google.cloud import vision
import re
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\aprabhakar\Desktop\snakes\testDAT\Processed\ContainerLabelTextExtraction-5a1d34fb942b.json"
filePaths = []
fileNames = []
fileNumber = 0
i = 0
client = vision.ImageAnnotatorClient()
s3 = boto3.resource('s3')
imageName = []
isEmpty = True
# Change the path below to where images are
for (dirpath, dirnames, filenames) in os.walk(r'\\hbm001inddat001\Container Label Images'):
    for f in filenames:
        filePaths.append(os.path.join(dirpath, f))
        fileNames.append(f)
        fileNumber = fileNumber + 1

i = 101084
while i != fileNumber:
    with io.open(filePaths[i], 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    imageName = fileNames[i].split(".")
    response = client.document_text_detection(image=image)
    if len(response.full_text_annotation.text) > 0:
        isEmpty = False
        output = response.full_text_annotation.text
        s3.Object('googlevision-results', imageName[0] + '.txt').put(Body=output)
    # response = client.text_detection(image=image)
    # if len(response.full_text_annotation.text) > 0:
    #     isEmpty = False
    #     output = response.full_text_annotation.text
    #     s3.Object('googlevision-results', imageName[0] + '.txt2').put(Body=output)
    if isEmpty is True:
        s3.meta.client.upload_file(filePaths[i], 'googlevision-emptyresults', fileNames[i])
    isEmpty = True
    i = i + 1






#print(fileNames)
#print(fileNumber)


