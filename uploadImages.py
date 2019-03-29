from google.cloud import storage  # pip install --upgrade google-cloud-storage (if missing)
import os
# There may be an issue with Credentials. May need path to the JSON file
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\aprabhakar\Desktop\snakes\testDAT\DrugVision-a4b475787d6d.json"
filePaths = []
fileNames = []
fileNumber = 0
i = 0
client = storage.Client()
bucket = client.get_bucket('drugimages')  # Change to relevant Bucket Name.
# Change the path below to where images are
for (dirpath, dirnames, filenames) in os.walk(r'C:\Users\aprabhakar\Desktop\snakes\testDAT\justimages'):
    for f in filenames:
        filePaths.append(os.path.join(dirpath, f))
        fileNames.append(f)
        fileNumber = fileNumber + 1

while i != fileNumber:
    blob = bucket.blob(fileNames[i])
    blob.upload_from_filename(filePaths[i])
    i = i + 1


print(fileNames)
print(fileNumber)


