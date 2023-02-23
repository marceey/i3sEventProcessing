import matplotlib.pyplot as plt
import numpy as np
import utils
import tonic
from PIL import Image

#loading data
event_input = np.load("data/DVS-Lip/train/Addition/15.npy")
print(event_input)

#defining timestamps for crops
lowest_timetamp = 500000
step = 500000

#peforming temporal crop according to timestamp and step
event_input = utils.timestamp_crop(event_input, lowest_timetamp, lowest_timetamp+step)
print(event_input)

#performing spatial quadrqtic centered crop to desired size
event_input = utils.quadratic_crop_event(event_input, 256)
print(event_input)

#print scatterplot
utils.scatterplot_event(event_input)
print(event_input)

#create black and white image
bw_image = utils.blackwhite_image(event_input)

#apply face landmark function to locate mouth
utils.face_landmarks(bw_image)


#some experiments with tonic library

#event_input = np.delete(event_input, 2, 1)
#i = [0, 1, 3, 2]
#event_input = event_input[:,i]
#print(event_input)
#image = tonic.transforms.ToImage(event_input)
#print(image)

#tonic.utils.plot_event_grid(event_input, axis_array=(1, 5))

#data_tonic = np.zeros(event_input.shape[0], dtype={"names":("x", "y", "p", "t"), "formats":("i8","i8","i8","i8")})
#data_tonic["x"]=event_input[:,0]
#data_tonic["y"]=event_input[:,1]
#data_tonic["p"]=event_input[:,2]
#data_tonic["t"]=event_input[:,3]
#
#transform = tonic.transforms.ToImage(
#    sensor_size=(640, 480, 2)
#)
#
#image = transform(data_tonic)
#plt.imshow(image[1]-image[0])
#plt.axis(False)
#plt.show()