
import boto3

# Connect to AWS using your existing IAM profile
session = boto3.Session(
    profile_name="terraform-trainig",
    region_name="us-east-1"
)

# Connect to EC2
ec2 = session.client("ec2")

# Find your Terraform web server
response = ec2.describe_instances(
    Filters=[
        {
            "Name": "tag:Name",
            "Values": ["Terraform-Web-Server"]
        }
    ]
)

print("=== AWS EC2 SERVER HEALTH REPORT ===")

found = False

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        found = True
        instance_id = instance["InstanceId"]
        status = instance["State"]["Name"]

        print("Instance:", instance_id)
        print("Status:", status)

        if status == "running":
            print("Result: SERVER IS RUNNING")
        elif status == "stopped":
            print("Result: SERVER IS STOPPED")
        else:
            print("Result: SERVER STATE:", status)

if not found:
    print("No matching EC2 instance found.")
