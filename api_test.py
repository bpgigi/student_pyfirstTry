import json
import requests
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
city_name = input("请输入要查询的城市名字")
params = {
    "name":city_name,
    "count":1,
    "language":"zh"
}
geo_response = requests.get( geo_url, params=params)
geo_data = geo_response.json()
print(geo_data)
city = geo_data["results"][0]#--->全部信息，不只是city这个
print(json.dumps(city, ensure_ascii=False, indent=4))
print(f"城市：{city['name']}")
# print(city["id"])
# print(city["latitude"])
# print(city["longitude"])
latitude = city["latitude"]
longitude = city["longitude"]
print("维度：",latitude)
print("经度",longitude)

#第二次api，查天气
# weather_url = "https://api.open-meteo.com/v1/forecast"
# weather_params = {
#     "latitude": latitude,
#     "longitude": longitude,
#     "current": "temperature_2m"
# }
# weather_response = requests.get( weather_url, params=weather_params)
# weather_data = weather_response.json()
# print(weather_data)
# print(type(weather_data))
# print(json.dumps(weather_data, ensure_ascii=False, indent=4))
# temperature = weather_data["current"]["temperature_2m"]
# # print(weather_data["temperature_2m"])
# print(temperature)