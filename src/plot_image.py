import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def rotate90(file_name):
    img = Image.open(file_name)
    img90 = img.transpose(Image.ROTATE_90)
    img90.save(file_name, 'jpeg')

def plot(file_name):
    img = Image.open(file_name)
    img.show()

plot("./images/1.jpg")