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
    url = 'https://mvcstybohd.execute-api.eu-west-2.amazonaws.com/dev/api'
    r = requests.post(url,json=ftrs)
    print(r.json())