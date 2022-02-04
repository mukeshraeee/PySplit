#===== This code generate number of trajectories ==============
import sys
import os
import pysplit

working_dir = "C:\\hysplit4\\working"
storage_dir = "G:\\pysplit\\jeevan\\aut"
meteo_dir   = "G:\\datas\\GDAS_Data\\2020"

basename = 'ktm'

years = [2020]
months = [9,10,11]
hours = [10]
altitudes = [500]
location = (27.68, 85.32)
runtime = -168


#years = [2020]
#months = [1,2,3,4,5,6,7,8,9,10,11,12]
#hours = [0,6]
#altitudes = [100]
#location = (35,85)
#runtime = -168 # 7 days



pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 1), get_reverse=True, get_clipped=True)



