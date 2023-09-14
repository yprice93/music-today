import requests


def show_chart():
    url = "https://billboard-api2.p.rapidapi.com/hot-100"

    querystring = {"date": "2019-05-11", "range": "1-10"}

    headers = {
        "X-RapidAPI-Key": "3b0bcefbc1msh02aef6a6be70fedp1806eejsn9dbd662dbcff",
        "X-RapidAPI-Host": "billboard-api2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response


