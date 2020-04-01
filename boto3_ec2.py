import boto3

def create_key_pair(keyname,filename):
    # create a file to store the key locally
    with open(filename,'w') as outfile:
        # call the boto ec2 function to create a key pair
        key_pair = ec2_resource.create_key_pair(KeyName=keyname) 
        # capture the key and store it in a file
        KeyPairOut = str(key_pair.key_material)
        print(KeyPairOut)
        outfile.write(KeyPairOut)
    return KeyPairOut

def create_ec2_instance(ec2_resource):
    #Create a session from your credintials using Session object
    session = boto3.session.Session()
    region = session.region_name
    # call the boto ec2 function to create a instance 
    instance_response= ec2_resource.create_instances(ImageId='ami-09a7fe78668f1e2c0',InstanceType='t2.micro',MinCount=1,MaxCount=1,IamInstanceProfile={'Arn':"arn:aws:iam::889876724334:instance-profile/ec2s3role"},KeyName="Cloudwatch")
    return instance_response

#Create boto3 resource interface and then pass the name of aws service to connect to
ec2_resource = boto3.resource('ec2')
#print(create_ec2_instance(ec2_resource))
#print(create_key_pair('ec2-keypair','ec2-keypair.pem'))

response = ec2_resource.meta.client.describe_instances()
print(response)
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        specificinstance = ec2_resource.Instance(instance["InstanceId"])
        print(specificinstance)
#Check which instances are running
instances = ec2_resource.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)
for status in ec2_resource.meta.client.describe_instance_status()['InstanceStatuses']:
    print(status)
