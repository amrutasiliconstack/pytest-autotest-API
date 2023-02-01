import requests
from utilities.getApiKey import *
from utilities.configurations import *
from utilities.invalid_TestData import *

body1 = {"minBatteryCrankVoltage": 7.57,
         "firstAmbientTemperature": 16,
         "tripStartDateTime": "2023-01-24T00:20:20Z",
         "restVoltage": 5.57,
         "tripEndDateTime": "2023-01-24T00:20:20Z",
         "tripStartLocation": {
             "latitude": 0.0,
             "longitude": 0
         },
         "tripEndLocation": {
             "latitude": 0,
             "longitude": 0
         }
         }


def getUrl():
    return getConfig()['API']['endpoint'] + '/da-stage/vehicles/autotest-example-vehicle-id/trips'


def test_tripApi_withInvalidPayload():
    response = requests.post(getUrl(), json=body, headers=getApiKey())
    assert response.status_code == 400
    assert response.json()['message'] == "Unable to process the request"
    assert response.json()['status'] == "failure"
    print(response.status_code)
    print(response.json())


def test_tripApi_Missing_minBatteryCrankVoltage():
    response = requests.post(getUrl(), json=removeAttr(body1, 'minBatteryCrankVoltage'), headers=getApiKey())
    assert response.status_code == 422
    assert response.json()['message'] == "The field minBatteryCrankVoltage cannot be empty."
    assert response.json()['status'] == "failure"
    print(response.status_code)
    print(response.json())


def test_tripApi_Missing_tripEndDateTime():
    response = requests.post(getUrl(), json=removeAttr(body1, 'tripEndDateTime'), headers=getApiKey())
    assert response.status_code == 422
    assert response.json()['message'] == "Trip Start Time/Trip End Time cannot be null"
    assert response.json()['status'] == "failure"
    print(response.status_code)
    print(response.json())


def test_tripApi_Missing_tripStartDateTime():
    response = requests.post(getUrl(), json=removeAttr(body1, 'tripStartDateTime'), headers=getApiKey())
    assert response.status_code == 422
    assert response.json()['message'] == "Trip Start Time/Trip End Time cannot be null"
    assert response.json()['status'] == "failure"
    print(response.status_code)
    print(response.json())


def test_tripApi_Missing_tripEndLocation():
    response = requests.post(getUrl(), json=removeAttr(body1, 'tripEndLocation'), headers=getApiKey())
    assert response.status_code == 422
    assert response.json()['message'] == "The provided lat/lng must be in range of (+/-) 90 and (+/-) 180 respectively"
    assert response.json()['status'] == "failure"
    print(response.status_code)
    print(response.json())


def test_tripApi_Missing_tripStartLocation():
    response = requests.post(getUrl(), json=removeAttr(body1, 'tripStartLocation'), headers=getApiKey())
    assert response.status_code == 422
    assert response.json()['message'] == "The provided lat/lng must be in range of (+/-) 90 and (+/-) 180 respectively"
    assert response.json()['status'] == "failure"
    print(response.status_code)
    print(response.json())
