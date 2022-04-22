import decouple
import requests
import json

API_TOKEN = decouple.config("CLIMATEMPO_TOKEN")
DEFAULT_URL = "http://apiadvisor.climatempo.com.br/api/v1/"


def get_id_by_city_and_state(city="Sapucaia do Sul", state="RS"):
    # create the request url for the city
    url_parameters = f"locale/city?name={city}&state={state}&token={API_TOKEN}"
    url_full = DEFAULT_URL + url_parameters

    response = requests.get(url_full)  # get the response
    reponse_dict = json.loads(response.text)[0]  # convert to a dictonary

    return reponse_dict["id"]


def get_weather_by_id(id=5195):

    climate_url = f"weather/locale/{id}/current?token={API_TOKEN}"
    full_url = DEFAULT_URL + climate_url

    response = requests.get(full_url)
    data_raw = json.loads(response.text)
    data = data_raw["data"]
    temperature = data["temperature"]
    humidity = data["humidity"]
    condition = data["condition"]
    date = data["date"]

    return temperature, humidity, condition, date


def register_city(city="Sapucaia do Sul", state="RS"):
    URL_MANAGER = "http://apiadvisor.climatempo.com.br/api-manager/"
    URL_USER = f"user-token/{API_TOKEN}/locales"

    id = get_id_by_city_and_state(city, state)
    url_full_register = URL_MANAGER + URL_USER
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = f"localeId[]={id}"

    response = requests.put(url_full_register,
                            headers=headers, data=payload)

    print(response)
    print(response.text)


if __name__ == "__main__":

    # register_city()

    id = 5195  # get_id_by_city_and_state("Sapucaia do Sul")
    data_raw = get_weather_by_id(id)

    print(data_raw)
