import csv


def readCsv():
    with open('utilities/FailSafe_TestData.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        # print(csvReader)
        # print(list(csvReader))
        aList = list(csvReader)          # convert tuple to list
    return aList
