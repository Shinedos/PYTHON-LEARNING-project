import pandas
import os
from sklearn.model_selection import train_test_split
import cv2

ims = os.listdir('img')
print(ims)
class loader_data(models):
    def __init__(self, path):
        self.path = path