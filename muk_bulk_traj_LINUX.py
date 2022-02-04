#===== This code generate number of trajectories ==============
#import sys
#import os
import pysplit

hysplit_working  = '/mnt/c/hysplit4/working'
output_dir       = '/mnt/g/pysplit/TRAJFILE'
meteo_dir        = '/mnt/g/datas/GDAS_Data/2019'

basename = 'ABC'

#years = [2017]
#months = [2]
#hours = [10]
#altitudes = [500]
#location = (42.82, -75.54)
#runtime = -120


#years = [2017]
#months = [1,2,3,4,5,6,7,8,9,10,11,12]
#hours = [0,6]
#altitudes = [100]
#location = (35,85)
#runtime = -168 # 7 days



#pysplit.generate_bulktraj(basename, hysplit_working, output_dir, meteo_dir,
#                          years, months, hours, altitudes, location, runtime,
#                          monthslice=slice(0, 32, 1), get_reverse=True, get_clipped=True)



years = [2019]
months = [7]
hours = [0,6,12,18]
altitudes = [100]
location = (35,85)
runtime = -168 # 7 days

pysplit.generate_bulktraj(basename, hysplit_working, output_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 1))
                          #get_reverse=True,
                          #get_clipped=True)

