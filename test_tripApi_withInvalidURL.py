import requests
from utilities.getApiKey import *
from utilities.configurations import *

body = {"minBatteryCrankVoltage": 7.57,
        "firstAmbientTemperature": 16,
        "tripStartDateTime": "2023-01-24T00:20:20Z",
        "restVoltage": 5.57,
        "tripEndDateTime": "2023-01-24T00:20:20Z",
        "tripStartLocation": {
            "latitude": 0,
            "longitude": 0
        },
        "tripEndLocation": {
            "latitude": 0,
            "longitude": 0
        }
        }


def getInvalidUrl1():
    return getConfig()['API']['endpoint'] + '/da-stage/vehicles/autotest-example-vehicle-id/trip'


def getInvalidUrl2():
    return getConfig()['API']['endpoint'] + '/vehicles/autotest-example-vehicle-id/trips'


#  invalid url
def test_tripApi_withInvalidURL1():
    response = requests.post(getInvalidUrl1(), json=body, headers=getApiKey())
    assert response.status_code == 403
    assert response.json()['message'] == "Missing Authentication Token"
    assert response.headers['Content-Type'] == 'application/json'
    print(response.status_code)
    print(response.json())


def test_tripApi_withInvalidURL2():
    response = requests.post(getInvalidUrl2(), json=body, headers=getApiKey())
    assert response.status_code == 403
    assert response.json()['message'] == "Forbidden"
    assert response.headers['Content-Type'] == 'application/json'
    print(response.status_code)
    print(response.json())
