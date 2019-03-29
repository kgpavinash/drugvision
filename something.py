import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'risperidone-figure-03.jpg')
#
# # Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()
#
# image = types.Image(content=content)
#
# # Performs label detection on the image file
# response = client.label_detection(image=image)
# labels = response.label_annotations


# Assuming there are not subdirectories, only image files
files = []
output = ""

for (dirpath, dirnames, filenames) in os.walk(r'\\issrv1\Departmental\KBS\Shared\World\Todd\Container Label Images'):
    for f in filenames:
        files.append(os.path.join(dirpath, f))

for file in files:
    with io.open(file, 'rb') as image_file:
        content = image_file.read()

    # print("PRINT STATEMENT: NEW IMAGE BEING PROCESSED")
    # print(file)
    # output = "PRINT STATEMENT: NEW IMAGE BEING PROCESSED\n"
    output = ""
    output = output + str(file) + "\n"

    image = types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    # print('Labels:')
    # for label in labels:
    #     print(label.description)

    resp = client.document_text_detection(image=image)
# # print('\n'.join([d.description for d in resp.text_annotations]))
    for d in resp.text_annotations:
        # print(d.description)
        output = output + str(d.description) + "\n"
        break
    realName = file.rsplit('\\', 1)[-1]
    displayName = realName.split('.', 1)[0]
    # print(realName)
    link = r"C:\Users\aprabhakar\Desktop\snakes\testDAT\stateImages\\" + str(displayName) + "9" + ".txt"
    with open(link, 'w+', encoding="utf-8") as f:
        f.write(output)
















