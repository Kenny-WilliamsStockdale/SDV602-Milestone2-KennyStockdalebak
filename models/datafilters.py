# import pandas as pd
import models.importcsv as importcsv


def merge(newFile, currentFile):
        importcsv.append(newFile, currentFile)
        
        print(merge())

def localityData():
        data = importcsv.getData(importcsv.dataset)
        male = 0
        female = 0
        for row in data:
            if row['sex'] == "male":
                male += 1
            elif row['sex'] == "female":
                female += 1
        return {"Male": male, "Female": female}