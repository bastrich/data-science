import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas.plotting import scatter_matrix

plt.style.use('ggplot')
#%% matplotlib inline

data = pd.read_csv('data/crx_data_train_x.csv', header=None, na_values='?')

scatter_matrix(data, alpha=0.05, figsize=(10, 10))


plt.show()