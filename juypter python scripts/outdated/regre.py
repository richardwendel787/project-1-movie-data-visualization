import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np
def line_plot(x, y):
    # Function that takes in 2 panda series x, y and plots a linear regression line
    slope, inter, rval, pval, stderr = st.linregress(x, y)
    print(f'The r-squared is : {rval ** 2}')
    x_line = np.arange(x.min(), x.max()+1, 1)
    y_line = (slope * x_line) + inter
    plt.plot(x_line, y_line, 'r',
             label='y = {0:.3f}x + {1:.3f}'.format(slope, inter))
    # Using legned label to annotate because it can use best location
    plt.legend(loc='best')