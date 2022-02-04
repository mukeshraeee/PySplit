 #===== This code generate number of trajectories ==============
#import sys
#import os

import pysplit

working_dir = "C:\\hysplit4\\working"
storage_dir = "G:\\pysplit\\dipesh"
meteo_dir   = "G:\\datas\\GDAS_Data\\2016"

basename = 'kry'

years = [2016]
months = [1,2,3,4,5,6,7,8,9,10,11,12]
hours = [0,6,12,18]
altitudes = [1650]
location = (42.6,77)
runtime = -168 # 7 days 

pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 1))
                          #get_reverse=True,
                          #get_clipped=True)

