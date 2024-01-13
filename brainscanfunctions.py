import glob
from PIL import Image
import numpy as np

def load_brain_scan(directory):
    x_array = []
    y_array = []
    counts = []
    
    counter = 0
    for filename in glob.glob(directory + '/VeryMildDemented/*.jpg'): 
        im = Image.open(filename)
        im = np.asarray(im)
        x_array.append(im)
        y_array.append(0)
        counter+=1
    counts.append(counter)
    
    counter = 0
    for filename in glob.glob(directory + '/NonDemented/*.jpg'): 
        im = Image.open(filename)
        im = np.asarray(im)
        x_array.append(im)
        y_array.append(1)
        counter+=1
    counts.append(counter)
        
    counter = 0
    for filename in glob.glob(directory + '/ModerateDemented/*.jpg'): 
        im = Image.open(filename)
        im = np.asarray(im)
        x_array.append(im)
        y_array.append(2)
        counter+=1
    counts.append(counter)
    
    counter = 0
    for filename in glob.glob(directory + '/MildDemented/*.jpg'): 
        im = Image.open(filename)
        im = np.asarray(im)
        x_array.append(im)
        y_array.append(3)
        counter+=1
    counts.append(counter)
    
    x_array = np.asarray(x_array)
    y_array = np.asarray(y_array)
    return x_array, y_array, counts
