import mat4py
import numpy as np
from stft import stft_function
import imagesc as imagesc


lib = mat4py.loadmat('./FFC.mat')
sigma = 0.000001
x = lib['x']
z = lib['z']
a = 499
b = 505
x = np.transpose(x[a:b])+sigma*np.random.randn(np.size(np.transpose(z[a:b])))
tf = stft_function(x, 10)
fig = imagesc.fast(abs(tf))
status = imagesc.savefig(fig, './figs/result.png')
print(status)
