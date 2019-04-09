import json
import boto3
storageFiles = []
noStorageFiles = []

s3 = boto3.resource('s3')
bucket_fom = "labeltextreformatted"
bucket_to_storage = "storagefilesbucket"
bucket_to_nostorage = "nostoragefilesbucket"
# f1 = open(r"C:\Users\aprabhakar\Desktop\snakes\testDAT\temp\storageFiles.txt", "w+")
# f2 = open(r"C:\Users\aprabhakar\Desktop\snakes\testDAT\temp\noStorageFiles.txt", "w+")
with open(r'C:\Users\aprabhakar\Desktop\snakes\testDAT\notext\predictions.jsonl') as json_file:
    data = json.load(json_file)
    # print(data[1])
    for e in data:
        # print(e['Classes'])
        # print(e['Classes'][0]['Name'])
        if e['Classes'][1]['Name'] == 'STORAGE':
            if e['Classes'][1]['Score'] >= 0.01:
                fileName = e['File']
                response = s3.meta.client.copy_object(
                    Bucket=bucket_to_storage,
                    CopySource={"Bucket": bucket_fom, "Key": fileName},
                    Key=fileName
                )
            else:
                # noStorageFiles.append(e['File'])
                fileName = e['File']
                response = s3.meta.client.copy_object(
                    Bucket=bucket_to_nostorage,
                    CopySource={"Bucket": bucket_fom, "Key": fileName},
                    Key=fileName
                )
        elif e['Classes'][1]['Name'] == 'OTHER':
            # storageFiles.append(e['File'])
            fileName = e['File']
            response = s3.meta.client.copy_object(
                Bucket=bucket_to_storage,
                CopySource={"Bucket": bucket_fom, "Key": fileName},
                Key=fileName
            )
# f1.write(str(storageFiles))
# f2.write(str(noStorageFiles))
# f1.close()
# f2.close()








