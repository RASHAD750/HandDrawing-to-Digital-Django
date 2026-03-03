import os
import numpy as np
import cv2
import natsort
import xlwt
from skimage import exposure

from sceneRadianceCLAHE import RecoverCLAHE
from sceneRadianceHE import RecoverHE

np.seterr(over='ignore')
if __name__ == '__main__':
    pass
# folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/HE"
folder = "C:/Users/Aagneya/Desktop/New folder/Single-Underwater-Image-Enhancement-and-Color-Restoration-master/Underwater Image Enhancement/CLAHE/image"
# folder = "C:/Users/Administrator/Desktop/Databases/Dataset"

path = folder 
files = os.listdir(path)
files =  natsort.natsorted(files)

for i in range(len(files)):
    file = files[i]
    filepath = path + "/" + file
    prefix = file.split('.')[0]
    if os.path.isfile(filepath):
        print('********    file   ********',file)
        # img = cv2.imread('InputImages/' + file)
        img = cv2.imread(folder +"/"+ file)
        sceneRadiance = RecoverCLAHE(img)
        #cv2.imwrite('OutputImages/' + prefix + '_CLAHE.jpg', sceneRadiance)
        cv2.imwrite(folder + "/prefix" + '_CLAHE.jpg', sceneRadiance)
