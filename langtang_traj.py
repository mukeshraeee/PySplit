"""
=============================================
Basic Scatter Plotting and Advanced MapDesign
=============================================

In ``basic_plotting_example.py``, we learned how to quickly initialize
matplotlib Basemaps with the ``MapDesign`` class and how to plot ``Trajectory``
paths and color according to a single value.  Here, we'll get into more
advanced usage of ``MapDesign`` and learn a couple of ways to scatter plot our
along-trajectory data.

For this example we'll initialize only the February trajectories created in 
``reversetraj_clippedtraj_gen.py``.

"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition

import pysplit

trajgroup0  = pysplit.make_trajectorygroup(r'/mnt/h/pysplit/langtang_traj/*winter*')
trajgroup1  = pysplit.make_trajectorygroup(r'/mnt/h/pysplit/langtang_traj/*spring*')

fig, (ax0,ax1) = plt.subplots(nrows=2,figsize=(12,12))

mapcorners =  [10, -5, 150, 60]
standard_pm = [75, 75, 20, 20]

param_dict = {'projection':'lcc', 'latlon_labelspacing':(10,30),
              'latlon_spacing':(10,15), 'latlon_fs':10, 'drawstates':True,
              'resolution':'l', 'mapcolor':'medium'}


map_params0 = pysplit.MapDesign(mapcorners, standard_pm, lon_labels=[],**param_dict)
map_params1 = pysplit.MapDesign(mapcorners, standard_pm, lon_labels=[],**param_dict)

scattermap0 = map_params0.make_basemap(ax=ax0)
scattermap1 = map_params1.make_basemap(ax=ax1)
"""
Plotting ``Trajectory`` data
----------------------------
This is at present the best way to approximate a color-graded line.
Here, we'll scatter plot along-trajectory pressure data.

Scatter plotting can be performed in a couple ways.  The first is to use the
standard ``basemap.scatter()``, and the second is to use
pysplit.traj_scatter()``.  Both are shown in the example below,
and achieve exactly the same result- the top and bottom maps should be
identical.

There are also different ways of acquiring the ``Trajectory`` coordinates,
which can be mixed and matched with the method of scatter plotting.
"""

#===== Subplot ======

# Need to find minimum and maximum pressure first to ensure consistent color
# scaling across all trajectories!
min_pressure = 1000.0
max_pressure = 0.0

for traj in trajgroup0:
    if traj.data.Pressure.max() > max_pressure:
        max_pressure = traj.data.Pressure.max()
    if traj.data.Pressure.min() < min_pressure:
        min_pressure = traj.data.Pressure.min()

for traj in trajgroup1:
    if traj.data.Pressure.max() > max_pressure:
        max_pressure = traj.data.Pressure.max()
    if traj.data.Pressure.min() < min_pressure:
        min_pressure = traj.data.Pressure.min()

# To cut down on crowding, let's plot every other trajectory
for traj in trajgroup0[::5]:
   map0 = scattermap0.scatter(*traj.path.xy,c=traj.data.Pressure.astype(np.float64).values,
    						 cmap=plt.cm.Blues, vmin=min_pressure,
    						 vmax=max_pressure, zorder=24, latlon=True,
    						 edgecolor='none')

for traj in trajgroup1[::5]:
    map1 = scattermap1.scatter(*traj.path.xy,c=traj.data.Pressure.astype(np.float64).values,
                                                 cmap=plt.cm.Blues, vmin=min_pressure,
                                                 vmax=max_pressure, zorder=24, latlon=True,
                                                 edgecolor='none')

#for traj1 in trajgroup[::2]:
# mappable1 = pysplit.traj_scatter(traj1.data.Pressure.astype(np.float64).values,
#                                    traj1.data.geometry.apply(lambda p: p.x).values,
#                                    traj1.data.geometry.apply(lambda p: p.y).values,
#                                    scattermap1, colormap=plt.cm.Blues,
#                                    vmin=min_pressure, vmax=max_pressure,
#                                    suppress_printmsg=True)

#plt.colorbar(map0,ax =ax0)
#plt.colorbar(map1,ax =ax1)
#plt.colorbar(map2,ax =ax2)
#plt.colorbar(map3,ax =ax3,orientation="horizontal")
#plt.colorbar(map, ax=ax3)
cbar=plt.colorbar(map1, ax=[ax0,ax1],pad=0.1) #, orientation="horizontal",pad=0.1)
cbar.set_label('Pressure', rotation=-270, fontsize=10)


#cax, cbar = pysplit.make_cax_cbar(datamap.ax.get_figure(),[0.2, 0.175, 0.6, 0.03],map3, cbar_label='pressure') #'Moisture Flux ((m/s/)(g/kg))')


#cbar= fig.colorbar(ax, ax=ax[:,:], location = 'right')
#cbar.set_label('Pressure', rotation=-270, fontsize=10)

"""
Another Look at ``pysplit.traj_scatter()``
-------------------------------------------

A potential advantage of this method is that is can streamline the
application of various normalizations.  Here's a BoundaryNorm dividing our
along-trajectory pressures up into six levels.

Later examples will show other usages of ``pysplit.traj_scatter()``,
colorbar generation, and how to plot ``Trajectory.uptake()`` data.
"""

#map_params2 = pysplit.MapDesign(mapcorners, standard_pm, **param_dict)
#boundarymap = map_params2.make_basemap()

#for traj in trajgroup[::2]:    
#    mappable2 = pysplit.traj_scatter(traj.data.Pressure.astype(np.float64).values,
#                                    *traj.path.xy, hymap=boundarymap,
#                                    colormap=plt.cm.Blues, vmin=min_pressure,
#                                    vmax=max_pressure, suppress_printmsg=True,
#                                    cnormalize='boundary', levels=10)


#plt.colorbar(mappable2)
plt.show()

