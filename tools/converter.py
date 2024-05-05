import csv
import numpy as np
import os

#change for linux
out_directory = "/home/vm-user/Documents/OpenPCDet/data/custom/points"
testAmt = 527


with open('/home/vm-user/Downloads/11-07_13-21-02.csv', newline='') as csvfile:
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
            testAmt -= 1
            if (testAmt <= 0):
                break;
            point_cloud_data = np.vstack((x, y, z, intensity)).T
            # np.save(out_directory + '/' + str(fileNum) + ".npy", np.vstack((x, y, z, intensity)).T)
            point_cloud_data.astype(np.float32).tofile(out_directory + '/' + str(fileNum) + ".bin")
            fileNum += 1
            timestamp = row['Timestamp']
            # point_cloud_data.clear()
            x.clear()
            y.clear()
            z.clear()
            intensity.clear()

        if(timestamp == row['Timestamp']):
            x.append(float(row['X']))
            y.append(float(row['Y']))
            z.append(float(row['Z']))
            intensity.append(float(row['Reflectivity']))

    point_cloud_data = np.vstack((x, y, z, intensity)).T
    point_cloud_data.astype(np.float32).tofile(out_directory + '/' + str(fileNum) + ".bin")