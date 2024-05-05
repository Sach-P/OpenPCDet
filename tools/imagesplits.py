

trainFile = "/home/vm-user/Documents/OpenPCDet/data/custom/ImageSets/train.txt"
valFile = "/home/vm-user/Documents/OpenPCDet/data/custom/ImageSets/val.txt"
#
# with open(trainFile, 'w') as file:
#     for num in range(385):
#         file.write(str(num) + '\n')


with open(valFile, 'w') as file:
    for i in range(385, 527):
        file.write(str(i) + '\n')