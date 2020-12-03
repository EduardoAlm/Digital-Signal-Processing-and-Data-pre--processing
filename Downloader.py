from get_data_IRIS import get_data
import mat4py

lib = mat4py.loadmat('./lib.mat')
print(lib['eq']['date'])
i = 0
date = lib['eq']['date']
lat = lib['eq']['lat']
long = lib['eq']['long']
for i in range(len(lib['eq']['date'])):
    get_data(date[i], lat[i], long[i])
