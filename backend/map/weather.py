import requests,json

def weather_data():

    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": "CWB-55776BC5-C606-4670-B4CE-AB7AFFA809C4",
    }

    response = requests.get(url, params=params)
    print(response.status_code)

    if response.status_code == 200:
        #print(response.text)測試有沒有抓到資料
        data = json.loads(response.text)
        for location_data in data["records"]["location"]:
            locations = location_data["locationName"]

            weather_elements = location_data["weatherElement"]
            start_time = weather_elements[0]["time"][0]["startTime"]
            end_time = weather_elements[0]["time"][0]["endTime"]
            weather_state = weather_elements[0]["time"][0]["parameter"]["parameterName"]
            rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
            min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
            comfort = weather_elements[3]["time"][0]["parameter"]["parameterName"]
            max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]
        
            print(f"Location: {locations}")
            print(start_time)
            print(end_time)
            print(weather_state)
            print(rain_prob)
            print(min_tem)
            print(comfort)
            print(max_tem)
            
        
    else:
        print("No data!")
        
  
weather_data()