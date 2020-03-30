import boto3
import uuid
#Creating the bucket name using uuid for unique bucket name
def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])
#print(create_bucket_name("test"))

#Creating the bucket
def create_bucket(bucket_prefix,s3_connection):
    session = boto3.session.Session()
    region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': region})
    print(bucket_name, region)
    return bucket_name, bucket_response

#Creating a file and Uploading a File to S3
def create_file(size,file_name,file_content):
    random_file_name = "".join([str(uuid.uuid4().hex[:6]),file_name])
    with open (random_file_name,'w') as f:
        f.write(str(file_content)*size)
    # Bucket instance to create objects in s3    
    object_response= s3_resource.Bucket(first_bucket_name).upload_file(Filename=random_file_name, Key=random_file_name)
    return random_file_nam

#Downloading a File
def download_file(bucket_name,file_name):
   # Object instance to download file 
   download_response =s3_resource.Object(bucket_name,file_name).download_file(f'/home/{file_name}')
   return download_response

#Copying an Object Between Buckets using .copy()
def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)

#Deleting an Object from the bucket using .delete()
def delete_object(bucket_name,object_name):
    return s3_resource.Object(bucket_name,object_name).delete()


#Bucket travesals 
def bucket_travesal():
    for bucket in s3_resource.buckets.all():
        print(bucket.name)

#Object travesals in a bucket
def obj_traverse(bucket_name):
    for obj in bucket_name.objects.all():
        print(obj.key)

#Deleting objects in bucket
#Note: to delete buckets the bucket shouldnt have objects in it
def delete_all_objects(bucket_name):
    res = []
    bucket=s3_resource.Bucket(bucket_name)
    for obj_version in bucket.object_versions.all():
        res.append({'Key': obj_version.object_key,
                    'VersionId': obj_version.id})
    print(res)
    bucket.delete_objects(Delete={'Objects': res})

#deleting buckets
def delete_bucket(bucket_name):
    s3_resource.Bucket(bucket_name).delete()


#Creating a boto3 resource interface to interact or establish connection with AWS S3 service
s3_resource = boto3.resource('s3')

#first_bucket_name,bucket_response=create_bucket('test',s3_resource)
#print(first_bucket_name)
#random_file_name=create_file(30,'testfile.txt','hi')
#print(random_file_name)

#print(download_file('test058def7a-c0ce-400f-84f8-f27bad9ee930','c153fctestfile.txt'))
#print(copy_to_bucket(first_bucket_name, second_bucket_name, first_file_name))
#print(delete_object('test058def7a-c0ce-400f-84f8-f27bad9ee930','c153fctestfile.txt'))

