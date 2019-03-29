from google.cloud import storage
from google.cloud.vision import types
from google.cloud import vision

client1 = storage.Client()
bucket = client1.get_bucket('drugdata')

theblob = bucket.get_blob("tp-1.png")
theblobdownload = theblob.download_as_string()
client2 = vision.ImageAnnotatorClient()
image = types.Image(content=theblobdownload)
response = client2.document_text_detection(image=image)

# for page in response.full_text_annotation.pages:
#     print(page)

# for page in response.text_annotations:
#     print(page)
paragraph_words = ""
paragraph_all = []

for page in response.full_text_annotation.pages:
    # print(page)
    for block in page.blocks:
        # print('\nBlock confidence: {}\n'.format(block.confidence))
        # print(block)
        for paragraph in block.paragraphs:
            # print('Paragraph confidence: {}'.format(
            #     paragraph.confidence))
            # print(paragraph.words)
            for word in paragraph.words:
                word_text = ''.join([
                    symbol.text for symbol in word.symbols
                ])
                # print('Word text: {} (confidence: {})'.format(
                #      word_text, word.confidence))
                paragraph_words = paragraph_words + word_text
                # for symbol in word.symbols:
                #      print('\tSymbol: {} (confidence: {})'.format(
                #          symbol.text, symbol.confidence))
            paragraph_all.append(paragraph_words)
            paragraph_words = ""

print(paragraph_all)

