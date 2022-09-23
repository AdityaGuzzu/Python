'''
In this file, we will use the urllib library and NumPy to download csv files from the web and analyse them
'''

import numpy as np
import urllib.request as url_req

#urlretrieve takes two arguments: The URL, the path,name of the file where it should be downloaded

'''
The downloaded spreadsheet has the climate data like temperature, rainfall, humidity etc of 10000 places.
We can make a prediction that rainfall in each of the places will depend linearly on temperature, rainfall, humidity
For the purpose of demonstration, we may choose those linear factors. 
Let's suppose those factors are [0.2,0.76,0.45]
'''
url_req.urlretrieve('https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv',
    'climate.txt')

climate_data = np.genfromtxt('climate.txt',delimiter=',',skip_header=1)
print(climate_data)
clim_para = [0.2,0.76,0.45]

'''
To get the prediction result of each place, 
we need to multiply the climate_data and clim_para matrices
'''
yields = climate_data @ clim_para   #matrix multiplication short hand


'''
Since yield is also an essential part of the climate data, we may like to add it to the climate_data file.
We can achieve that by the following way:
'''

new_data = np.concatenate((climate_data,yields.reshape(10000,1)),axis=1)


'''
        NOTE: Here, reshaping is necessary because yields is a (1,10000) dimensional array.
              We cannot concatenate it to the first axis of climate_data without reshaping
'''

#lets save the data back to our climate.txt file
'''
The savetxt function saves the array to a given file. 
    ---> The fmt arg specifies the precision of the float. By default its set to 10. So to manually override that, we 
         specify the precision
    ---> The deader arg provides the header with a prefixed '#' to comment it out
    ---> The comments arg overrides the pre-comment characters. In this case, the '#' will be replaced by ''
'''
np.savetxt('climate.txt',climate_data,fmt='%.2f',header='temperature,rainfall,humidity,yield',comments='')
