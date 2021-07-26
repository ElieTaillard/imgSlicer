import os
from pathlib import Path
from chopImg import chopImg

############ CONSTANTS ############################
CURRENT_PATH = Path().absolute()
INPUT_PATH = os.path.join(CURRENT_PATH, "Input")
OUTPUT_PATH = os.path.join(CURRENT_PATH, "Output")

NUMBER_OF_CHOPS = 4
###################################################


################################
#            Main              #
################################

dirsIN = os.listdir(INPUT_PATH)

for filename in dirsIN:
    if filename.endswith(".png"):
        chopImg(os.path.join(INPUT_PATH, filename),
                NUMBER_OF_CHOPS, OUTPUT_PATH)
    else:
        continue
