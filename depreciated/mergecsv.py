# import csv
# data = []
# def append(newFile, currentFile):
#         header = ["id","modified","language","institutionCode","collectionCode","basisOfRecord","dynamicProperties","source","catalogNumber","occurrenceRemarks","individualCount","sex","lifeStage","occurrenceStatus","associatedTaxa","eventID","samplingProtocol","eventDate","startDayOfYear","year","month","day","waterBody","country","stateProvince","county","locality","minimumDepthInMeters","maximumDepthInMeters","decimalLatitude","decimalLongitude","geodeticDatum","coordinateUncertaintyInMeters","footprintWKT","identifiedBy","typeStatus","scientificNameID","scientificName","kingdom","phylum","class","order_","family","genus","subgenus","specificEpithet","infraspecificEpithet","verbatimTaxonRank","FID"]
#         # change header!!!
#         with open(currentFile, 'a', newline="") as csvfile:
#             writer = csv.writer(csvfile, header,extrasaction='ignore')
#             for row in getData(newFile):
#                 writer.writerow(row)
    
# newFile = "src/data/nzpropertytitleslatest2021.csv"
# currentFile = "src/data/nzpropertytitles201920.csv"

# # if __name__ == "__main__":
# #     print(append(newFile, currentFile))

# def getMerge ():
#     with open("src/data/test_data_2.csv", newline='') as csvfile:
#         rows = csv.reader(csvfile, delimiter=',')
#         merge = []
#         for row in rows:
#             merge.append(row)

#     # headers = merge.pop(0)
    
#     for row in merge:
#         data.append(row)

#     # data[row[0]] = row[1:]    
#     # for key in data:
#     #     print (key, data[key][3])
    
#     return(data)


# if __name__ == "__main__":

#     print(getMerge())