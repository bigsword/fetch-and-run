import sys
import os
import runpy
import uuid
import boto3
import psycopg2

"""this script will download certain .py file from s3 and try to execute them locally.
    the .py file is provided by environment variable.
    the .py file parameter is provided by environment variable.
    supporting lib/file will be provided by environment variable.
"""


def fetch_and_run(bucket :str, key :str, libs :list) -> None:
    # Create a folder that no one else will use.
    # in case there are two Batch jobs run.
    random = uuid.uuid4().hex
    tmp_folder = f'/tmp/{random}'
    #tmp_folder = f'c:/temp/{random}'
    os.mkdir(tmp_folder)
    os.chdir(tmp_folder)
    # in case the script need to import module in the same folder.
    sys.path.insert(0, tmp_folder)

    script_name = ''.join(key.split('/')[-1:])

    path_name = f'{tmp_folder}/{script_name}'

    s3 = boto3.client('s3')
    s3.download_file(bucket, key, path_name)

    print(f'>>>fetch_and_run-->downloaded the script {script_name} to {tmp_folder}.')

    if args:
        print(f'    the args have {len(args.split(" ")) // 2} parameters.')

    # download all the libs as well.
    if libs:
        lib_files = libs.split(',')
        for lib in lib_files:
            lib = lib.strip()
            lib_name = ''.join(lib.split('/')[-1:])

            print(f'>>>to download {lib}')
            
            s3.download_file(bucket, lib, f'{tmp_folder}/{lib_name}')

    runpy.run_path(path_name, run_name='__main__')

    print('>>>fetch_and_run-->the .py script had been executed.')



if __name__ == '__main__':
    bucket = os.environ['BUCKET_NAME']
    script = os.environ['SCRIPT_PATH_NAME']
    libs   = os.environ.get('SCRIPT_LIBS')
    args   = os.environ.get('SCRIPT_ARGS') 

    #before extend sys.argv, may need to parse the current one.

    sys.argv.extend(args.split(' '))
    #print(sys.argv)

    fetch_and_run(bucket=bucket, key=script, libs=libs)
