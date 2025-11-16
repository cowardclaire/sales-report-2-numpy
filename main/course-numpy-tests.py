
import numpy as np

import matplotlib.pyplot as plt
import PIL
import urllib.request

image_url_rgb = "https://codeinstitute.s3.amazonaws.com/predictive_analytics/jupyter_notebook_images/Numpy_rainbow.png"
image_rgb = PIL.Image.open(urllib.request.urlopen(image_url_rgb))
#plt.imread(image_url_rgb) is depricated
np_image_rgb = np.array(image_rgb)
print(f"* Array shape: {np_image_rgb.shape} ===> 3 channels (RGB)")
arr = np.random.randint(low=0,high=255,size=(300,500,3))
plt.imshow(arr)
plt.show()