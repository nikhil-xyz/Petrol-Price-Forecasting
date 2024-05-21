# Petrol Price Forecasting ML Project

### Clone the Repository
```
=======
## Clone the Repository
```
https://github.com/nikhil-xyz/Petrol-Price-Forecasting.git
```

### Create a Conda environment and activating it
```
conda create -n venv python=3.8 -y
conda activate venv
```

### Execute the command
```
streamlit run app.py
```

<<<<<<< HEAD
### Streamlit Exposed port
8501

### AWS-CICD-Deployment-with-Github-Actions

#### 1. Login to AWS console.

#### 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

    ## 4. Create EC2 machine (Ubuntu) 

###  Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
###  Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


###  Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
=======
## Streamlit Exposed port
8501
