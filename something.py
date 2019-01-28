# def implicit():
#     from google.cloud import storage
#
#      # If you don't specify credentials when constructing the client, the
#      # client library will look for credentials in the environment.
#     storage_client = storage.Client.from_service_account_json(
#         'service_account.json')
#
#      # Make an authenticated API request
#     buckets = list(storage_client.list_buckets())
#     print(buckets)
#
# implicit()
#
#
# def explicit():
#     from google.cloud import storage
#
#     # Explicitly use service account credentials by specifying the private key
#     # file.
#     storage_client = storage.Client.from_service_account_json(
#         'service_account.json')
#
#     # Make an authenticated API request
#     buckets = list(storage_client.list_buckets())
#     print(buckets)
#
# explicit()

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'risperidone-figure-03.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)

print()

resp = client.document_text_detection(image=image)
# print('\n'.join([d.description for d in resp.text_annotations]))
for d in resp.text_annotations:
    print(d.description)














