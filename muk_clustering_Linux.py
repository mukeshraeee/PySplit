## ===== Aadd require packages ===============
from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import pysplit

# We ignored Daylight Saving Time during generation.  EST is UTC-5
trajgroup = pysplit.make_trajectorygroup(r'/mnt/g/pysplit/tpe_clipped/TPE*')

trajgroup.make_infile(r'/mnt/c/hysplit4/cluster/working')


traj_assignment = r'/mnt/c/hysplit4/cluster/working/CLUSLIST_4'  # CLUSLIST depend on cluster group
clusterpath_dir = r'/mnt/c/hysplit4/cluster/working'



clusgroup = pysplit.spawn_clusters(trajgroup, traj_assignment, clusterpath_dir)


#==== Plot ==========
colors = np.linspace(0, 0.95, 7)

mapcorners =  [30, 5, 130, 60]
#standard_pm = None
standard_pm = [75, 75, 20, 20]

param_dict = {'projection':'lcc', 'latlon_labelspacing':(10,30),
              'latlon_spacing':(10,15), 'latlon_fs':16, 'drawstates':True,
              'resolution':'l', 'mapcolor':'medium'}

map_params0 = pysplit.MapDesign(mapcorners, standard_pm, **param_dict)
map_params1 = pysplit.MapDesign(mapcorners, standard_pm, **param_dict,lon_labels=['bottom'])
#map_params2 = pysplit.MapDesign(mapcorners, standard_pm, **param_dict)
#map_params3 = pysplit.MapDesign(mapcorners, standard_pm, lon_labels=['bottom'], **param_dict)

fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10,10))

map0 = map_params0.make_basemap(ax=ax0)
map1 = map_params1.make_basemap(ax=ax1)

# Text on maps
x, y = map0(-135, 25)
font_params = {'horizontalalignment' : 'center',
               'verticalalignment' : 'center',
               'fontsize' : 20,
               'weight' : 'bold'}

ax0.text(x, y, 'Clusters', **font_params)
ax1.text(x, y, 'Trajectories', **font_params)

for clus, color in zip(clusgroup, colors):
    params = {'zorder' : 24,
                  'latlon' : True,
                  'c' : plt.cm.Blues(color)}

    map0.plot(*clus.path.xy, lw=(clus.trajcount/clusgroup.trajcount)*50,
                  **params)

    for traj in clus:
        map1.plot(*traj.path.xy, lw=1.5, **params)

fig.subplots_adjust(hspace=0.1)



plt.show()
