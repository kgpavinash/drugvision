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
    # response = client2.label_detection(image=image)
    # labels = response.label_annotations
    # print('Labels:')
    # for label in labels:
    #     print(label.description)
    response = client2.document_text_detection(image=image)
    for page in response.full_text_annotation.pages:
        #print(page)
        for block in page.blocks:
            # print('\nBlock confidence: {}\n'.format(block.confidence))
            # print(block)
            for paragraph in block.paragraphs:
                # print('Paragraph confidence: {}'.format(
                #     paragraph.confidence))
                #print(paragraph.words)
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    # print(word)
                    # print('Word text: {} (confidence: {})'.format(
                    #      word_text, word.confidence))
                    # for symbol in word.symbols:
                    #      print('\tSymbol: {} (confidence: {})'.format(
                    #          symbol.text, symbol.confidence))


# resp = client2.document_text_detection(image=image)
# output = ""
# for d in resp.text_annotations:
#     # print(d.description)
#     output = output + str(d) + "\n"
#     #break
# print(output)






