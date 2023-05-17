# Steps to deploy the entire stack into an AWS account with SAM CLI

## Prerequisites
- **Make sure you have aws and sam cli's installed**
- **Make sure you have admin access(to deploy all resources) to the aws account**
- **Clone this repository and change directory into it**

## To deploy with default parameters, issue the following set of commands:**
    - sam build
    - sam deploy --resolve-image-repos

## Deployment with input parameters:
    You can override the enviroment(stage) and apitoken value by using the following parameters in 
    the deploy command:

    - sam deploy --resolve-image-repos --parameter-overrides DeployStage=dev SecretToken=mysecrettoken
    

# testcase folder has commands to use if you want to test the endpoints deployed locally with docker