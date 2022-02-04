import pysplit

working_dir = "C:\\hysplit4\\working"
storage_dir = "G:\\pysplit\\autumn_qoms"
meteo_dir   = "G:\\datas\\GDAS_Data\\2017"

basename = 'qoms' ## 30.772517° N, 90.962450° E

years = [2017]
months = [9,10,11]
hours = [0,6,12,18]
altitudes = [100]
location =  (28.36,86.95) #(30.772517, 90.962450)             #(35,85)
runtime = -168 # 7 days

pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 1),
                          get_reverse=True,
                          get_clipped=True)

