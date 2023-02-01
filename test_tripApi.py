import pytest
import requests
from payload import *
from testdata import *
from utilities.configurations import *
from utilities.getApiKey import *


def getUrl():
    return getConfig()['API']['endpoint'] + '/da-stage/vehicles/autotest-example-vehicle-Amruta/trips'


#  trip api
def tripApi(body):
    # print(inputpayLoad(body))
    response = requests.post(getUrl(), json=inputpayLoad(body), headers=getApiKey())
    assert response.status_code == 202
    assert response.json()['message'] == "Accepted"
    assert response.json()['status'] == "success"
    assert response.headers['Content-Type'] == 'application/json'
    print('-Correlation-Id    ' + response.headers['X-IA-Correlation-Id'])
    print(response.status_code)
    print(response.json())


# Run test case for different data
#@pytest.mark.skip(reason="skip this")
def test_tripApi():
    csvReader = readCsv()
    for row in csvReader[1:]:  # [1:] skipping first element/row
        tripApi(row)
