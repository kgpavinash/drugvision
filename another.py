from google.cloud import storage
from google.cloud.vision import types
from google.cloud import vision

client1 = storage.Client()
bucket = client1.get_bucket('drugdata')
blobs = bucket.list_blobs()
for blob in blobs:
    downloaded_blob = blob.download_as_string()
    client2 = vision.ImageAnnotatorClient()
    image = types.Image(content=downloaded_blob)
    response = client2.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')
    for label in labels:
        print(label.description)
