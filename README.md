# fetch-and-run

This is a docker image and it's supposed to run in aws Batch/ECS environment. It will download a Python script from aws s3 to local and run it.

Currently in the docker image, `boto3` and `psycopg2` are installed.

Please populate the following environment variables before run the container.

`BUCKET_NAME`: where to download the .py script.

`SCRIPT_PATH_NAME`: the name of the .py script to run.

`SCRIPT_LIBS`: supporting .py or .json or any other file needed to be downloaded. They will be download into the same folder with the main python script.

`SCRIPT_ARGS`: args will be pass into the python script. they should look like this: `--parameter-name value --another value2`

# how to use

this repo linked to docker hub, and you can use this docker image by ref:
`bigsword/fetch-and-run`
