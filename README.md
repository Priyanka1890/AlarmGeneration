# Simple to AWS Lambda API

This project is about how to upload custom api to aws lambda.

It assumes that user has 
 - AWSCLI installed
 - user runs 'aws configure' to set proper parameters for aws connection
 - user has python 3.9
 - user has 'virtual env'

# Steps

Following are the steps to deploy the saved ML model as an AWS Lambda API

    - Download the project from git
    - cd 'project_dir'
    - Activate 'venv' and install from 'install.txt'
    - run 'zappa deploy/update '__Project__NAME__' (e.g. dev)


# How to interact with the API

Following is a python code snippet that shows how to call the api
```python
import json
import requests
    
if __name__ == '__main__':
        ftrs = {
          "user_id":'med4pan8976',
          "contact":"+4123454678",
          "user_lat":77.90,
          "user_lon":88.90,
          "user_device":'apple watch',
          "user_age_group": "15-23",
          "user_activity":"Running 3 METs",
          "user_heart_rate":127.11
        }
        url = 'http://127.0.0.1:5001/api'
        r = requests.post(url,json=ftrs)
        print(r.json())
```
The output should look like following

```
{'alarm': 1.0, 'confidence': 1.0, 'description': 'probability of heart problem: 1 = Yes, 0 = No'}
```