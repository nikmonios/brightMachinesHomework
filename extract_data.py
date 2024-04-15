import requests


url = "0.0.0.0:8989/extract"

part_id = "ABC-123-example"
start_date = "01-01-2020, 15:45:00"
end_date = "12-01-2022, 16:00:00"
limit=10

querystring_1 = {"part_id":part_id, "start_date":start_date , "end_date":end_date}
querystring_2 = {"part_id":part_id, "limit":limit}

payload=""
headers=""

response_1 = requests.request("GET", url, data=payload, headers=headers, params=querystring_1)

print(response_1.text)

response_2 = requests.request("GET", url, data=payload, headers=headers, params=querystring_2)

print(response_2.text)