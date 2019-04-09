import boto3
s3 = boto3.resource('s3')

# bucket_fom = "thesourcebucket01"
# bucket_to = "thedestbucket01"

# fileName = "noStorageFiles.txt"
# response = s3.meta.client.copy_object(
#     Bucket=bucket_to,
#     CopySource={"Bucket":bucket_fom, "Key": fileName},
#     Key=fileName
# )
# print(response)
data = ""
keys = []
bucket = s3.Bucket("labeltextreformatted")
for obj in bucket.objects.all():
    key = obj.key
    # print(key)
    body = obj.get()['Body'].read().decode('utf-8')
    data = data + '\n' + body
    # print(body)
    keys.append(key)

# print(data)
s3.Object('thedestbucket01', 'CombinedFile.txt').put(Body=data)
# print(keys)
# f1 = open(r"C:\Users\aprabhakar\Desktop\snakes\testDAT\temp\storageFiles.txt", "w+")
# f1.write(str(data))