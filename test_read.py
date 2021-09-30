import pandas as pd
import model.importcsv as csv
df = pd.read_csv(csv.newFile)

# print(df.head(5))

data = csv.getData(csv.filePath)
data.pop(0)

# print(data)
total = 0
count = 0
test = []

for row in data:
    test.append(row[6])

# print(test)

for size in test:
    count += 1
    # print(size.split(' ')[0])
    total += int(size.split(' ')[0]) if size != '' else 0
    

print(total/count)