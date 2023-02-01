import datetime

tripDate = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


# d1 = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")


def inputpayLoad(data):
    print(tripDate)
    body = {
        "minBatteryCrankVoltage": data[5],
        "firstAmbientTemperature": data[4],
        "tripStartDateTime": tripDate,
        "restVoltage": 8.57,
        "tripEndDateTime": tripDate,
        "tripStartLocation": {
            "latitude": data[1],
            "longitude": data[0]
        },
        "tripEndLocation": {
            "latitude": data[3],
            "longitude": data[2]
        }
    }
    return body
