import os
from pathlib import Path
from chopImg import chopImg
from PIL import Image
import uuid

############ CONSTANTS ############################
CURRENT_PATH = Path().absolute()
INPUT_PATH = os.path.join(CURRENT_PATH, "Input")
OUTPUT_PATH = os.path.join(CURRENT_PATH, "Output")
###################################################


################################
#            Main              #
################################

dirsIN = os.listdir(INPUT_PATH)

for filename in dirsIN:
    if filename.endswith(".png"):
        img = Image.open(os.path.join(INPUT_PATH,filename))
        arrayImg = chopImg(img)

        for img in arrayImg:
            path = os.path.join(OUTPUT_PATH, str(uuid.uuid4())+".png")
            img.save(path)
    else:
        continue
