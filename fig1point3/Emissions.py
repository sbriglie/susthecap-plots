import numpy as np
import matplotlib.pyplot as  plt
#from matplotlib.patches import Polygon

C0='#1f77b4'
C1='#ff7f0e'
C2='#2ca02c'
C3='#d62728'
C4='#9467bd'
C5='#8c564b'
C6='#e377c2'

category_names = ['Scope 1 (direct)', 'Scope 2 (indirect, e.g. electricity)', 'Travel (business)', 'Travel (commuting)', 'Food', 'Computers, supplies', 'Waste treatment']
category_colors = [C0, C1, C2, C2, C2, C2, C2]
category_hatch = [None,None,None,'.O','--','//','*','x']

rawdata = {'CERN': [4.4, 2.0, 1.0, 1.1, 0.2, 0, 0.4],
        'MPIA': [ 1.4, 2.4, 8.5, 0.4, 0.1, 0.4, 0],
           'ETHZ DPHYS': [ 0.76, 0.15, 3.2, 0.18, 0, 0.34, 0],
           'Nikhef': [ 0.68, 0.0, 3.34, 0.67, 0, 0, 0],
#        'EU household member': [ 0, 2.6, 3.5, 2.2, 3.1, 0]
}



labels = list(rawdata.keys())
data = np.array(list(rawdata.values()))
data_cum = data.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(13.2, 5))

ax.invert_yaxis()
ax.xaxis.set_visible(True)
ax.set_xlim(0, np.sum(data, axis=1).max())
ax.set_xlabel("GHG emissions (tCO$_{2}$e)")

ax.set_title("Average annual GHG emissions per researcher",loc="left")
for i, (colname, color, hatch) in enumerate(zip(category_names, category_colors, category_hatch)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    rects = ax.barh(labels, widths, left=starts, height=0.5,
                    label=colname, color=color, hatch=hatch,edgecolor = 'k')
    
ax.barh("Per capita `budget' to 2050", 1.7, height = 0.5, color='k', edgecolor='k')
ax.barh(' ', 2.3, height = 0.53, xy=(0,3.74), color='k', alpha=0.5, edgecolor=None)
ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left', fontsize='small')
fig.supxlabel('2019 data, save MPIA (2018), and ETHZ business travel (average 2016-2018).  Scope 3 estimates incomplete.  Total emissions assigned to individual researcher as follows: each individual emissions category was divided by the nominal number of users for that resource, be it total number of employees, or researchers, or Users (CERN). This is distinct from procedure in [8] where all emissions were equally divided amongst researchers only.', fontsize=12,  wrap=True)
ax.annotate(r'\}', fontsize=100, xy=(0.88,0.54), xycoords='figure fraction', zorder=100)
ax.annotate('Scope 3', fontsize = 14, xy=(0.94,0.54), xycoords='figure fraction', rotation=90, ha='left', zorder=100)
fig.set_zorder(1)
plt.tight_layout()
plt.savefig("ComparativeEmissions.pdf")
plt.close
