import boto3
s3 = boto3.resource('s3')

keys = []
bucket = s3.Bucket("labeltextreformatted")
for obj in bucket.objects.all():
    key = obj.key
    bucket.download_file(key,r"C:\Users\aprabhakar\Desktop\snakes\testDAT\allfiles\\"+key)
    keys.append(key)

print(keys)



