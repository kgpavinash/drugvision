from google.cloud import storage
from google.cloud.vision import types
from google.cloud import vision
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\aprabhakar\Desktop\QRCode\ContainerLabelTextExtraction-5a1d34fb942b.json"
client0 = storage.Client()
client1 = vision.ImageAnnotatorClient()
bucket = client0.get_bucket('containerlabelimages')
blobs = bucket.list_blobs()
imageName = []

for blob in blobs:
    imageName = blob.name.split(".")
    downloaded_blob = blob.download_as_string()
    image = types.Image(content=downloaded_blob)
    response = client1.document_text_detection(image=image)
    for d in response.text_annotations:
        # print(d.description)
        output = str(d.description)
        thePath = r"C:\Users\aprabhakar\Desktop\snakes\testDAT\Processed\\" + imageName[0] + ".txt"
        with open(thePath, 'w+', encoding="utf-8") as f:
            f.write(output)
        break
    response = client1.text_detection(image=image)
    for d in response.text_annotations:
        output = str(d.description)
        thePath = r"C:\Users\aprabhakar\Desktop\snakes\testDAT\Processed\\" + imageName[0] + ".txt2"
        with open(thePath, 'w+', encoding="utf-8") as f:
            f.write(output)
        break

