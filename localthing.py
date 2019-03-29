
import  io
from PIL import Image, ImageFilter
def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_document_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    # ******* change the text_detection to document_text_detection *******
    response = client.document_text_detection(image=image, image_context={"language_hints": ["en"]})
    print (response.full_text_annotation.text)
    # [END vision_python_migration_document_text_detection]
# [END vision_fulltext_detection]

def pillows():
    im = Image.open(r"C:\Users\aprabhakar\Desktop\snakes\testDAT\images\img0005.jpg")
    im.show()
    im_sharp = im.filter(ImageFilter.SHARPEN)
    im_sharp.save('image_sharpened.jpg', 'JPEG')
if __name__ == '__main__':
    detect_document(r"C:\Users\aprabhakar\Desktop\snakes\testDAT\images\image_sharpened.jpg")
    # pillows()