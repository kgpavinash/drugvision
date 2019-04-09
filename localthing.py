import io
from google.cloud import vision
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"filepath\DrugVision-a4b475787d6d.json"

def detect_document(path):
    """Detects document features in an image."""
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image, image_context={"language_hints": ["en"]})
    return response.full_text_annotation.text

if __name__ == '__main__':
    print(detect_document(r"C:\Users\aprabhakar\Desktop\snakes\testDAT\notext\risperidone-figure-03.jpg"))
