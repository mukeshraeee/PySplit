import sys
import os
import pysplit

working_dir = "C:\\hysplit4\\working"
storage_dir = "G:\\pysplit\\linda\\lumbini"
meteo_dir   = "G:\\datas\\GDAS_Data\\2017"

basename = 'lumbini'

years = [2017]
months = [11,12]
hours = [10]
altitudes = [500]
location = (27.29, 83.59)
runtime = -168


pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 1), get_reverse=True, get_clipped=True)



