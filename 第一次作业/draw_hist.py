import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

data = np.random.normal(0, 20, 1000)
 
bins = np.arange(-100, 100, 5) 

plt.style.use('ggplot')

plt.hist(data,bins=bins,color='steelblue')

plt.show()
