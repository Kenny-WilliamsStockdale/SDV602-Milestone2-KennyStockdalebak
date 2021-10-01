import csv
import pandas as pd


data = []
# ------ANCHOR IMPORT DATA INTO AN ARRAY AND PRINT------

# def getData ():
#     global data
#     with open("src/data/test_data_1.csv", newline='') as csvfile:
#         rows = csv.reader(csvfile, delimiter=',')
#         data = []
#         for row in rows:
#             data.append(row)

#     # headers = data.pop(0)

#     #         data[row[0]] = row[1:]
#     # for key in data:
#     #     print (key, data[key][3])

#     return(data)


def getData(filePath):
    global data
    with open(filePath, 'r', newline="") as csvfile:
        # header = ["id","modified","language","institutionCode","collectionCode","basisOfRecord","dynamicProperties","source","catalogNumber","occurrenceRemarks","individualCount","sex","lifeStage","occurrenceStatus","associatedTaxa","eventID","samplingProtocol","eventDate","startDayOfYear","year","month","day","waterBody","country","stateProvince","county","locality","minimumDepthInMeters","maximumDepthInMeters","decimalLatitude","decimalLongitude","geodeticDatum","coordinateUncertaintyInMeters","footprintWKT","identifiedBy","typeStatus","scientificNameID","scientificName","kingdom","phylum","class","order_","family","genus","subgenus","specificEpithet","infraspecificEpithet","verbatimTaxonRank","FID"]
        dataset = csv.reader(csvfile)
        output = []
        for row in dataset:
            output.append(row)
    return output


filePath = "src/data/test_data_1.csv"

# ------ANCHOR IMPORT DATA INTO AN ARRAY AND PRINT------

# def getMerge ():
#     with open("src/data/nzpropertytitleslatest2021.csv", newline='') as csvfile:
#         rows = csv.reader(csvfile, delimiter=',')
#         merge = []
#         for row in rows:
#             merge.append(row)

#     headers = merge.pop(0)

#     for row in merge:
#         data.append(row)

#     # data[row[0]] = row[1:]
#     # for key in data:
#     #     print (key, data[key][3])

#     return(data)


def append(newFile, currentFile):
    header = ["id", "modified", "language", "institutionCode", "collectionCode", "basisOfRecord", "dynamicProperties", "source", "catalogNumber", "occurrenceRemarks", "individualCount", "sex", "lifeStage", "occurrenceStatus", "associatedTaxa", "eventID", "samplingProtocol", "eventDate", "startDayOfYear", "year", "month", "day", "waterBody", "country", "stateProvince", "county",
              "locality", "minimumDepthInMeters", "maximumDepthInMeters", "decimalLatitude", "decimalLongitude", "geodeticDatum", "coordinateUncertaintyInMeters", "footprintWKT", "identifiedBy", "typeStatus", "scientificNameID", "scientificName", "kingdom", "phylum", "class", "order_", "family", "genus", "subgenus", "specificEpithet", "infraspecificEpithet", "verbatimTaxonRank", "FID"]
    # change header!!!
    with open(currentFile, 'a', newline="") as target_csvfile:
        writer = csv.writer(target_csvfile, header)
        for row in getData(newFile):
            writer.writerow(row)


newFile = "src/data/test_data_2.csv"
currentFile = "src/data/test_data_1.csv"

# if __name__ == "__main__":
#     print(append(newFile, currentFile))

# date = "2020/12/18 32465746"
# year, month = date.split(" ")[0].split("/")[0:2]
# print(year, month)


def readLocation(filePath):
    locationData = pd.read_csv(filePath,
                               usecols=["decimalLatitude",
                                        "decimalLongitude"],
                               )
    return locationData


if __name__ == "__main__":
    print(getData(filePath))
    # print(getMerge())
    print(append(newFile, currentFile))
    print(getData(filePath))
