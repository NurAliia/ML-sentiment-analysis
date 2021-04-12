import json
import pandas as pd
import requests

"""Setting the headers to send and accept json responses
"""
header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

"""Reading test batch
"""

df = pd.read_csv('../data/test.csv', encoding="utf-8-sig").fillna(0);
df = df.head()

"""Converting Pandas Dataframe to json
"""
data = df.to_json(orient='records')

print(json.loads(data))

"""POST <url>/predict
"""
resp = requests.post("http://eprusarw1669.saratov.epam.com:8080/predict", data = json.dumps(data), headers= header)

print(resp.status_code)

"""The final response we get is as follows:
"""
print(resp)