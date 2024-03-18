# Table of contents
Tech stack
How to contribute to the backend
How to contribute to the frontend

# Tech stack
- **AWS Lamba** allows us to run Python code on-demand. This reduces our costs since we do not have to run a server
around the clock for our application api to work.
- **Amazon DynamoDB** provides database infrastructure and a no-SQL experience that integrates seamlessly with the other
AWS products services.
- **SvelteKit** provides a compiler and other libraries to convert declarative front-end code into optimized JavaScript.
- **SAM CLI** allows us to build and test our project locally.
- **Docker** is used by SAM CLI to emulate the AWS environment using Amazon Linux.
- **Python3** is the language being used in our AWS Lambda functions and unit tests.

# How to contribute to the backend 
To run the backend, you will need to use AWS SAM CLI. SAM CLI allows you to use infrastructure as code to create an AWS
environment for local development and testing. You will also need to acquire a Yelp API key to get restaurant data.

Step 1

Step 2

Step 3

### Yelp API Key
GrubFinder relies on Yelp's API for restaurant data. Developers are required to create their own Yelp account and API key.
There is no cost to use the Yelp API, but there is a maximum limit of 500 requests per month.

- Create a yelp account.
- Go to the [create app](https://www.yelp.com/developers/v3/manage_app) page once logged in.
- Name your app whatever (i.e grubfinder_dev).
- Take note of your API Key.
- Set the environment variable on your machine with the key "YELP_KEY".

### Docker
Ensure that you have the
[latest version of Docker](https://www.docker.com/products/docker-desktop/) installed on your machine.

### AWS CLI
To access AWS resources you need to have 
[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed and configred with
the proper access keys.

### AWS SAM CLI
To be able to run the "backend" server locally and test your code you need to
[install SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
on your machine.

### venv
This isn't necessary, but it'll make your IDE happy if you want autocomplete and real-time linting.

```
# cd into the root direcotry of the app

# create venv directory
python3 -m venv .venv

# activate the venv environment
source .venv/bin/activate

# install the dependencies for the project
pip3 install requests
pip3 install boto3

# ensure that your IDE is using the venv for dependencies
```

### Running the "backend" locally.
```
# navigate to the root directory
cd path/to/grubfinder/root/directory

# run sam build
sam build

# start the api
sam local start-api
```

# How to contribute to the frontend 
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