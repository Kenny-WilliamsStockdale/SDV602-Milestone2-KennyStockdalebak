# import pandas as pd
import model.datacontroller as dc


def merge(newFile, currentFile):
    dc.append(newFile, currentFile)


def localityData():  # piechart data
    data = dc.getData(dc.filePath)
    dictPie = {}
    for row in data:

        if row[26] in dictPie.keys():
            dictPie[row[26]] += 1
        else:
            dictPie[row[26]] = 1

    labels = list(dictPie.keys())
    values = list(dictPie.values())
    return labels, values


def sizeFish():
    data = dc.getData(dc.filePath)
    data.pop(0)
    barData = {
        '1-50': 0,
        '51-100': 0,
        '101-150': 0,
        '151-200': 0,
        '201-250': 0,
        '251+': 0
    }
    for row in data:
        size = int(row[6].split(' ')[0]) if row[6] != '' else 0

        if size in range(1, 51):
            barData['1-50'] += 1
        elif size in range(51, 101):
            barData['51-100'] += 1
        elif size in range(101, 151):
            barData['101-150'] += 1
        elif size in range(151, 201):
            barData['151-200'] += 1
        elif size in range(201, 251):
            barData['201-250'] += 1
        elif size > 251:
            barData['251+'] += 1
    labels = list(barData.keys())
    values = list(barData.values())
    return labels, values

# def sizeYear():
#     data = dc.getData(dc.filePath)
#     data.pop(0)
#     years = {}
    
    
#     barData = {
#         '1-50': 0,
#         '51-100': 0,
#         '101-150': 0,
#         '151-200': 0,
#         '201-250': 0,
#         '251+': 0
#     }
    
#     for row in data:
#         # get the years
#         if row[19] in years.keys():
#             pass
#         else:
#             years[row[19]] = []
        
#         size = int(row[6].split(' ')[0]) if row[6] != '' else 0
    
#     print(years)
#     # {'year': {ranges:count, ...} }
    
# something = 10
# if something in range(0,51):
  #  print("Here")


def locationData():
    locationData = dc.readLocation(dc.filePath)
    return locationData


if __name__ == "__main__":
    # print(localityData())
    print(locationData())
    # print(sizeFish())
    print(sizeYear())
    print("fuck you")
