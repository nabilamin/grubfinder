# GrubFinder
Curb food indecision. A capstone project for UMGC.

## Tech Stack
- Python (v3.9)
- Docker (For local development)
- AWS Lambdas (Business logic)
- AWS DynamoDB (Database)
- Svelte (Frontend)

## Getting Started (For Contributors)

### Yelp API Key
GrubFinder relies on Yelp's API for restaurant data. In order to avoid hitting the request limit the keys that exist in production, developers are required to create their own Yelp account and API key.

- Create a yelp account.
- Go to the [create app](https://www.yelp.com/developers/v3/manage_app) page once logged in.
- Name your app whatever (i.e grubfinder_dev).
- Take note of your API Key.
- Set the environment variable on your machine with the key "YELP_KEY".

### Docker
Another tool that GrubFinder uses which we will get to in this README shortly requires Docker. Ensure that you have the [latest version of Docker](https://www.docker.com/products/docker-desktop/) installed on your machine.

### AWS CLI
To access AWS resources you need to have [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed and configred with the proper access keys.

### AWS SAM CLI
To be able to run the "backend" server locally and test your code you ned to install AWS SAM CLI. Use your favorie package manager or follow the instructions here to [install SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) on your machine.

### venv
This isn't neccessary but it'll make your IDE happy if you want autocomplete and real-time linting.

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