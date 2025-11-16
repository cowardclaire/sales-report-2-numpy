
import numpy as np

import matplotlib.pyplot as plt
import PIL
import urllib.request

image_url = "https://ci-jshint.herokuapp.com/static/images/logo.png"
image_data = urllib.request.urlopen(image_url)
image = PIL.Image.open(image_data)
np_image = np.array(image)
type(np_image)
plt.imshow(np_image*2)
plt.show()