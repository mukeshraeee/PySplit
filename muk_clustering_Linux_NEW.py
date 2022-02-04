## ===== Aadd require packages ===============
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pysplit
from mpl_toolkits.basemap import Basemap
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

# We ignored Daylight Saving Time during generation.  EST is UTC-5
win = pysplit.make_trajectorygroup(r'/mnt/g/pysplit/winter/TPE*')
win.make_infile(r'/mnt/g/pysplit/winter')
#win.make_infile(r'/mnt/c/hysplit4/cluster/working')
#====== Load Cluster daat========
traj_assignment = r'/mnt/g/pysplit/winter/CLUSLIST_4'  # CLUSLIST depend on cluster group
clusterpath_dir = r'/mnt/g/pysplit/winter'
clusgroup = pysplit.spawn_clusters(win, traj_assignment, clusterpath_dir)

#==== Now plot============
colors = np.linspace(0, 1, 6)

mapcorners =  [30, 5, 130, 60]
#standard_pm = None
standard_pm = [75, 75, 20, 20]

param_dict = {'projection':'lcc', 'latlon_labelspacing':(10,30),
              'latlon_spacing':(10,15), 'latlon_fs':16, 'drawstates':True,
              'resolution':'l', 'mapcolor':'medium'}

map_params0 = pysplit.MapDesign(mapcorners, standard_pm, **param_dict)
map_params1 = pysplit.MapDesign(mapcorners, standard_pm, **param_dict,lon_labels=['bottom'])

fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10,10))

map0 = map_params0.make_basemap(ax=ax0)
#map1 = map_params1.make_basemap(ax=ax1)
#m = Basemap(projection='lcc',width=12000000,height=9000000,lat_1=25,lat_2=25,lat_0=25,lon_0=90,llcrnrlon=40,llcrnrlat=0,urcrnrlon=150,urcrnrlat=60,resolution='h')

# Text on maps
#lons = 85
#lats = 35
#x, y = map0(85,35)
#x,y = map_params0(lons,lats)

font_params = {'horizontalalignment' : 'center',
               'verticalalignment' : 'center',
               'fontsize' : 20,
               'weight' : 'bold'}


#ax0.annotate('TPE', xy=(x, y), xycoords='data', xytext=(x, y), textcoords='data')

#plt.text(x, y, 'TPE')

bbox = dict(boxstyle="round", fc="0.8")

ax0.annotate('40 %', xy=(0.5, 0.5), bbox=bbox, xycoords='axes fraction',zorder=100)
#ax0.text(x, y, 'Clusters', **font_params)
#ax1.text(x, y, 'Trajectories', **font_params)
#ax0.plot(x, y, 'r', markersize=300)

#ax1.plot(lons, lats, marker='o', markersize=300)

#ax0.text(x, y, 'Trajectories', **font_params)
#ax0.plot(x, y, 'bo',markersize=20)
#ax0.map_params0(x, y, 'bo',markersize=20)

#ax0.annotate(text='Hi', xy=(lats,lons), xycoords='data')

#m.plot(x, y, marker = 'o',alpha=0.5, markersize=10, color='black', label="Tuva")



for clus, color in zip(clusgroup, colors):
    params = {'zorder' : 24,'latlon' : True,'c' : plt.cm.Blues(color)}
    map0.plot(*clus.path.xy, lw=(clus.trajcount/clusgroup.trajcount)*10,**params)

# for traj in clus:
#        map1.plot(*traj.path.xy, lw=1.5, **params)

fig.subplots_adjust(hspace=0.1)



plt.show()
