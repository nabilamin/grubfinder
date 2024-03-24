# Table of contents
- [Tech stack](#tech-stack)
- [Contributing to the backend](#contributing-to-the-backend)
- [Contributing to the frontend](#contributing-to-the-frontend)

# Tech stack
- **AWS Lamba** allows us to run Python code on-demand. This reduces our costs since we do not have to run a server
around the clock for our application api to work.
- **Amazon DynamoDB** provides database infrastructure and a no-SQL experience that integrates seamlessly with the other
AWS products services.
- **SvelteKit** provides a compiler and other libraries to convert declarative front-end code into optimized JavaScript.
- **SAM CLI** allows us to build and test our project locally.
- **Docker** is used by SAM CLI to emulate the AWS environment using Amazon Linux.
- **Python3** is the language being used in our AWS Lambda functions and unit tests.

# Contributing to the backend
To run the backend, you will need to use AWS SAM CLI. SAM CLI allows you to use infrastructure as code to create an AWS
environment for local development and testing. You will also need to acquire a Yelp API key to get restaurant data.

GrubFinder relies on Yelp's API for restaurant data. Developers are required to create their own Yelp account and API key.
There is no cost to use the Yelp API, but there is a maximum limit of 500 requests per month.

## 0. Prerequisite: Create Yelp Account
Navigate to https://www.yelp.com/developers

Click Sign Up

Complete the sign-up process

## 1. Get Yelp API key
Navigate to https://www.yelp.com/developers/v3/manage_app

Enter an app name, industry, email address, and description for the app

Click Create New App

For reference, you can always get back to your API key at https://www.yelp.com/developers/v3/manage_app

## 2. Set Yelp API key environment variable
Set environment variable "YELP_KEY" to your API key

## 3. Install Docker Engine
Navigate to https://docs.docker.com/engine/install/

Follow the installation instructions for your operating system

## 4. Install and configure AWS CLI
Navigate to https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

Follow the installation instructions for your operating system

Navigate to https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html

Choose a method for gathering credtial information for programmatic access and follow those instructions

## 5. Install SAM CLI
Navigate to https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html

Follow the installation instructions for your operating system

## 6. Clone the repo
In a terminal, run:
```bash
$ git clone git@github.com:nabilamin/grubfinder.git
```

## 7. Set up venv (Optional)
Setting up venv will help your IDE resolve dependencies.

In your terminal, run:

`$ python3 -m venv .venv`

`$ source .venv/bin/activate`

`$ pip3 install requests`

`$ pip3 install boto3`

## 8. Run SAM CLI
```
# navigate to the root directory
cd aws_serverless

# run sam build
sam build

# start the api
sam local start-api
```

# Contributing to the frontend
## Prerequisites
GitHub and Git on your machine are [configured to use SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

## 1. Clone the repo
In a terminal, run:
```bash
$ git clone git@github.com:nabilamin/grubfinder.git
```

## 2. Create a remote branch
Navigate to the [Grubfinder GitHub repository](https://github.com/lugenx/ecohabit/).

Click on "Branches".

Click on "New branch"

Enter a name for your branch.

Click "Create new branch"

## 3. Create a local branch
In a terminal, run:
```bash
$ git checkout -b YOUR_BRANCH_NAME
```
Replace YOUR_BRANCH_NAME with the same name from Step 2.

## 4. Set branch upstream

In a terminal, run:
```bash
$ git branch -u origin/YOUR_BRANCH_NAME
```

## 5. Do some development
Make a change to the code and commit it using:
```bash
$ git add .
$ git commit -m "Short description of changes made"
```

## 6. Push code to your remote branch
In a terminal, run:
```bash
git push
```

## 7. Submit changes for review
Navigate to the [Grubfinder GitHub repository](https://github.com/lugenx/ecohabit/).

Click on "Branches".

Click your branch name.

Click on "Contribute".

Click on "Open pull request".

Update the Title and Description with the appropriate details.

Click "Create pull request".