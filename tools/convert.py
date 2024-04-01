import laspy
import numpy as np
import os

#change for linux
in_directory = r"C:\Users\sachp\sdmay24-31\OpenPCDet\data\livoxlas"
out_director = r"C:\Users\sachp\sdmay24-31\OpenPCDet\data\livoxnpy\points"

for file_name in os.listdir(in_directory):
    if(file_name.endswith('.las')):
        las = laspy.read(os.path.join(in_directory, file_name))

        x = las.x
        y = las.y
        z = las.z
        intensity = las.intensity

        np.save(out_director + '\\' + file_name[:file_name.index('.')] + ".npy", np.vstack((x, y, z)).T)