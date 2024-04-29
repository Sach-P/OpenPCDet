import csv
import numpy as np
import os

#change for linux
out_directory = r"C:\Users\sachp\sdmay24-31\OpenPCDet\data\livoxnpy\points"


with open(r'C:\Users\sachp\sdmay24-31\OpenPCDet\tools\small.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    timestamp = 0
    x = []
    y = []
    z = []
    intensity = []
    fileNum = 0
    for row in reader:
        if(timestamp == 0):
            timestamp = row['Timestamp']
        if(timestamp != row['Timestamp']):
            np.save(out_directory + '\\' + str(fileNum) + ".npy", np.vstack((x, y, z, intensity)).T)
            fileNum += 1
            timestamp = row['Timestamp']
            x.clear()
            y.clear()
            z.clear()
            intensity.clear()
        if(timestamp == row['Timestamp']):
            x.append(row['X'])
            y.append(row['Y'])
            z.append(row['Z'])
            intensity.append(row['Reflectivity'])

    np.save(out_directory + '\\' + str(fileNum) + ".npy", np.vstack((x, y, z, intensity)).T)

        