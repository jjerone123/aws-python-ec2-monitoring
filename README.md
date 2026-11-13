\# AWS EC2 Monitoring Automation Using Python and Boto3



\## Project Overview



This project uses Python and Boto3 to connect securely to Amazon Web Services (AWS) and check the current state of an EC2 instance.



\## Business Problem



Cloud engineers need to monitor servers to understand whether they are running or stopped. Manually checking servers through the AWS Console can be repetitive.



\## Solution



I developed a Python script that:

\- Connects to AWS using an existing IAM profile.

\- Retrieves the status of an EC2 instance.

\- Displays the instance ID and current state.

\- Uses read-only AWS API requests.



\## Technologies Used



\- Python

\- Boto3

\- Amazon EC2

\- AWS IAM

\- AWS CLI

\- Terraform



\## How to Run This Project



\### Requirements

\- Python 3

\- Boto3

\- AWS CLI configured with an IAM profile

\- IAM permission: ec2:DescribeInstances



\### Install Boto3



python -m pip install boto3



\### Run the Script



python ec2\_monitor.py



\## Example Output



=== AWS EC2 SERVER HEALTH REPORT ===

Instance: i-060bab28f5ec40f1b

Status: stopped

Result: SERVER IS STOPPED



\## Security



\- AWS credentials are not stored in the Python script.

\- Authentication uses a local AWS CLI profile.

\- The script only reads EC2 information.

\- AWS credentials must never be uploaded to GitHub.



\## Future Improvements



\- Monitor multiple EC2 instances.

\- Add error handling.

\- Generate monitoring reports.

\- Integrate Amazon CloudWatch metrics.

