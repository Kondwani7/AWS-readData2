from __future__ import print_function
import json
import urllib
import pandas as pd

def lambda_handler(event, context):
    #get bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']
    #get the key name
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'],encoding='utf-8')

    try:
        #fetch the file from the s3 bucket
        response = s3.get_object(Bucket=bucket, Key=key)
        #deserialise the file
        text = response['Body'].read().decode()
        data = json.loads(text)
        #view the data's content
        print(data)
        #parse and view the data
        users = data['users']
        for record in users:
            print(record['name'])
        #pandas dataframe
        df = pd.DataFrame(data=users)
        print(df)
        return 'Done'
    
    except Exception as e:
        print(e)
        raise e
