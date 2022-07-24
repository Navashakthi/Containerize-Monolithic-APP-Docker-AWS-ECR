# Deploying a Monolithic service on AWS 

Step by step process of deploying a Monolithic Application ( Python Flask APP ) to a Docker container on AWS
### > Monolithic Architecture : 

The term Monolith means composed all in one piece. The Monolithic application describes a single-tiered software application in which different components combined into a single program from a single platform

It is an architecture where the software components are inter-dependent and tightly coupled.

## Project Use-Case
Invoice-INFO-APP is an application built to get invoice data such as
-- Total invoices of the month
-- Invoices Pending payment
-- Invoices with payment processed

## Requirements

- Python 3.9 : https://www.python.org/downloads/

- Docker : https://docs.docker.com/get-docker/

- AWS CLI : https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

- Visual Studio Code : https://code.visualstudio.com/download

- Python Libraries : requests, Flask == 2.0.3, Jinja2 == 3.1.1

Install all requirements, create an AWS account ( a free tier account is sufficient for this project ), login with credentials, create a user with necessary IAM permissions and download the credentials.csv file.
​https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html

## Project Structure:
The python flask App files and dependents are present in this folder structure
- data : Folder contains JSON file with invoice data
- app.py : Flask app to get invoice data
- requirements.txt
- Dockerfile
- .dockerignore

## Configure and Containerize the Application in Local Machine
- Check if docker is successfully installed in the system with : docker --version
Docker version 20.10.16, build aa7e414
- In the Invoice-Info-APP directory run the following commands:
  - docker build -t invoiceapp
  - docker run -p 5000:5000 invoiceapp
  This creates the docker build and run in the local machine.

## Configure and Containerize the Application in AWS
- Open AWS Account with User account
  - Navigate to the Amazon ECR console.
  - On the repository page, select *Create Repository* 
- Open the command prompt and check for AWS CLI installed with : aws --version
aws-cli/2.7.18 Python/3.9.11 Windows/10 exe/AMD64 prompt/off
- Configure AWS profile with the commands:
  -aws configure
  -aws configure set region us-west-1 --profile invoiceuser
  -aws configure list-profiles
  -setx AWS_PROFILE invoiceuser
  For more details on CLI configuration check - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-precedence







