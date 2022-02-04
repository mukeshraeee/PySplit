import sys
import os
import pysplit

working_dir = "C:\\hysplit4\\working"
storage_dir = "G:\\pysplit\\langtang_2nd_paper\\aut_f"
meteo_dir   = "G:\\datas\\GDAS_Data\\2017"

basename = 'lang'

years = [2017]
months = [9,10,11]
hours = [10]
altitudes = [500]
location = (28.21, 85.61)
runtime = 168




pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 1), get_reverse=True, get_clipped=True)

