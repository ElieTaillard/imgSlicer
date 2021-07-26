import os
from PIL import Image
import uuid


def chopImg(infile, numChop, outputPath):

    img = Image.open(infile)
    width, height = img.size
    chopsize = int(width/numChop)

    # Save Chops of original image
    for x0 in range(0, width, chopsize):
        for y0 in range(0, height, chopsize):
            box = (x0, y0,
                   x0+chopsize if x0+chopsize < width else width - 1,
                   y0+chopsize if y0+chopsize < height else height - 1)
            path = os.path.join(outputPath, str(uuid.uuid4())+".png")
            img.crop(box).save(path)
