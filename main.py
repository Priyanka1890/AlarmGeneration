# Import libraries

import pandas as pd
from flask import Flask, request, jsonify


FACTOR = 1.5
app = Flask(__name__)



def alarm(age_group:str, activity:str, heart_rate:float, device:str):

    df = None
    if "apple" in device:
        df = pd.read_csv("apple_data_alarm.csv")
    else:
        df = pd.read_csv("fitbit_data_alarm.csv")
    mu = df[(df["age_group"] == age_group) & (df["activity"] == activity)]["mu"].tolist()[0]
    std = df[(df["age_group"] == age_group) & (df["activity"] == activity)]["std"].tolist()[0]
    high = mu +  (FACTOR * std)
    low = mu - (FACTOR * std)
    if low <= heart_rate <= high:
        return 0.
    else:
        return 1.



@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    # sample pay load {
    #   "user_id":med4pan8976,
    #   "contact":+4123454678,
    #   "user_lat":77.90,
    #   "user_lon":88.90,
    #   "user_device":"apple watch"
    #   "user_age_group":"15-23",
    #   "user_activity":"Running",
    #   "user_heart_rate":87.11
    #   }
    data = request.get_json(force=True)
    op = alarm(age_group=data.get("user_age_group"), activity=data.get("user_activity"), heart_rate=data.get("user_heart_rate"), device=data.get("user_device"))
    return {
        'alarm':op ,
        'description':'probability of heart problem: 1 = Yes, 0 = No', 'confidence':1.0
    }


if __name__ == '__main__':
    app.run(port=5001, debug=True)
