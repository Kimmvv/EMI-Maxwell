# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:32:44 2020

@author: Kim
"""


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sys import exit
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

dir_path = '.' # Set path to directory
sep = ","

model = "Noise"

full = pd.read_csv(os.path.join(dir_path,'1.45_Mean_imp_FS.csv'), index_col=0,sep=sep)
#cen = pd.read_csv(os.path.join(dir_path,'Mean_imp_ThickA_cen.csv'), index_col=0,sep=sep)
#sl_ = pd.read_csv(os.path.join(dir_path,'Mean_imp_ThickA_skewed.csv'), index_col=0,sep=sep)
#sh_ = pd.read_csv(os.path.join(dir_path,'Mean_imp_ThickA_skew_high.csv'), index_col=0,sep=sep)
#cfg = full.columns #Get Cfg names from column
col = ['HCP_1.0_0.1', 'HCP_1.0_0.3', 'HCP_1.0_0.5',
       'HCP_2.5_0.1', 'HCP_2.5_0.3', 'HCP_2.5_0.5',
       'HCP_4.0_0.1', 'HCP_4.0_0.3', 'HCP_4.0_0.5',
       
       'VCP_1.0_0.1', 'VCP_1.0_0.3', 'VCP_1.0_0.5',
       'VCP_2.5_0.1', 'VCP_2.5_0.3', 'VCP_2.5_0.5',
       'VCP_4.0_0.1', 'VCP_4.0_0.3', 'VCP_4.0_0.5',
       
       'PRP_1.0_0.1', 'PRP_1.0_0.3', 'PRP_1.0_0.5',
       'PRP_2.5_0.1', 'PRP_2.5_0.3', 'PRP_2.5_0.5',
       'PRP_4.0_0.1', 'PRP_4.0_0.3', 'PRP_4.0_0.5',]

df = pd.DataFrame(columns=col)
cfg = df.columns

param = [0,1,2,3,4]
par_name = ['ECA', 'ThickA', 'ECB', 'ThickB', 'ECC']
idx = ['full','cen','sl','sh']

fig = plt.figure(figsize = (15,10))
spec = gridspec.GridSpec(ncols=6, nrows=1, wspace = 0.35)
axs = []

for ipar in param:
    par = ipar #0=ECA, 1=ThickA, 2=ECB, 3=ThickB, 4=ECC
    
    f =  full.iloc[par,:].values
    #c =  cen.iloc[par,:].values
    #sl = sl_.iloc[par,:].values
    #sh = sh_.iloc[par,:].values
    
    ECA_imp = pd.DataFrame([f],columns = cfg, index = idx) #only use the full range (f) for this plot
    mean = ECA_imp.mean() #Mean of each column
    
    
    p_val = 8      #Values to plot seperately
    o_val = 27-p_val #Values to aggregate into "others"
    # sum of p_val & o_val must be 27
    
    if p_val + o_val != 27:
        print("Values are not equal 27")
        exit(0)
    
    
    most_imp = np.argsort(-np.asarray(mean))[:p_val] # The # most important feats - based on mean imp over all 4 restriction patterns
    other = cfg[np.argsort(-np.asarray(mean))[-o_val:]] #Other bin
    
    #Re-sort the most imp feats based on the order they appear originally so the coil pos are next to each other 
    most_imp_sort = np.sort(most_imp) 
    
    #Full
    f_other_val = f[np.argsort(-np.asarray(mean))[-o_val:]].sum()
    full_val = f[most_imp_sort]
    full_val= np.append(full_val,f_other_val)
    print(most_imp_sort)
    #Centered
    #c_other_val = c[np.argsort(-np.asarray(mean))[-o_val:]].sum()
    #c_val = c[most_imp_sort]
    #c_val= np.append(c_val,c_other_val)
    
    #Skew low
    #sl_other_val = sl[np.argsort(-np.asarray(mean))[-o_val:]].sum()
    #sl_val = sl[most_imp_sort]
    #sl_val= np.append(sl_val,sl_other_val)
    
    #Skew high
    #sh_other_val = sh[np.argsort(-np.asarray(mean))[-o_val:]].sum()
    #sh_val = sh[most_imp_sort]
    #sh_val= np.append(sh_val,sh_other_val)
    
    #Labels
    label = list(cfg[most_imp_sort])
    label.append('others')
    
    ##################################################################################
    #                       Custom colourmap                    
    ##################################################################################
    from matplotlib import cm
    from matplotlib.colors import ListedColormap, LinearSegmentedColormap
    
    blue = cm.get_cmap('Blues',9)
    red = cm.get_cmap('Reds',9)
    green = cm.get_cmap('Greens',9)
    
    low, mid, high = 7,5,2
    white = (1.0, 1.0, 1.0, 1.0)
    hatches = [ "" , "//" , "O" , "" , "//" , "O" ,"" , "//" , "O" ,"" , "//" , "O" ,"" , "//" , "O" ,"" , "//" , "O" ,"" , "//" , "O" ,"" , "//" , "O","" , "//" , "O","" ]
    clr = [blue(low),blue(low),blue(low),blue(mid),blue(mid),blue(mid),blue(high),blue(high),blue(high),
           green(low),green(low),green(low),green(mid),green(mid),green(mid),green(high),green(high),green(high),
           red(low),red(low),red(low),red(mid),red(mid),red(mid),red(high),red(high),red(high),
           white]
   
    
    newcolor =  []
    for i in most_imp_sort:
        newcolor.append(clr[i])
    newcolor.append(white) #Other category is always white
    
    newhatches = []
    for j in most_imp_sort:
        newhatches.append(hatches[j])
    newhatches.append("")
    
    cmap = ListedColormap(newcolor,N=p_val)
    
    
    ############################# With hatches ######################################
    #fig1, f1_axes = plt.subplots(ncols=5, nrows=1, constrained_layout=True)
    
    #vals = [sh_val,sl_val,c_val,full_val]
    vals = [full_val]
    size = 0.3
    #radius = [1+size*2,1+size,1,1-size]
    radius = [1+size*2]
    
    axs.append(fig.add_subplot(spec[0, ipar]))
    
    for ival,ir in zip(vals,radius):
        piechart = axs[-1].pie(ival, radius = ir, wedgeprops=dict(width=1.6, edgecolor='k'), colors=newcolor)
        for i in range(len(piechart[0])):
            piechart[0][i].set_hatch(newhatches[(i)%len(newhatches)])
    
    #axs[-1].text(-0.1,0.0,par_name[ipar])
    #ax.legend(loc='upper left', labels=label,prop={'size': 12}, bbox_to_anchor=(-0.1, 1), bbox_transform=fig.transFigure)
    axs[-1].set_title(par_name[ipar],y=1.15)
    #plt.show()

#axs.append(fig.add_subplot(spec[0, 5]))
patches = []
conf = list(cfg)
conf.append('others')
for ic,icfg,ih in zip(clr,conf,hatches):
    patches.append(mpatches.Patch(facecolor=ic, hatch=ih, label=icfg, edgecolor='k'))
    
plt.legend(handles=patches,ncol=7, bbox_to_anchor=(1.25, -0.2))#,prop={'size': 12}, bbox_transform = fig.transFigure)    
fig.suptitle('Feature importance for full parameter range'.format(model), fontsize = 18, x = 0.45, y = 0.66)
plt.show()    

'''
df = full

obstype = df.columns
xtext = df.index
colors = ["b","y","r","k","m"]


fig = plt.figure()
for i in np.arange(5):
    labelstr=xtext[i]
    plt.plot(obstype,df.iloc[i,:],label=labelstr, color = colors[i])
plt.xlabel("Instrument Setup")
plt.ylabel("Importance")
plt.title("Feature importances")
plt.ylim(0,1)
plt.legend()
plt.grid()
plt.xticks(rotation=90)
#fig.savefig(os.path.join(dir_path,str(np.round(thick[j],2))+'_Bhor_mean_imp.png'))
plt.show() 


d = df.iloc[1,:].sort_values(ascending=False)
d.cumsum()

plt.plot(d.cumsum())
plt.plot([0, 26], [0.9, 0.9], 'k-', lw=2)
plt.grid()
plt.xticks(rotation=90)
plt.show() 


d = df.iloc[1,:].sort_values(ascending=False)
d.cumsum()

tot = 4+9+13+17+3

s = 1+2+6+10+0

v = 0+1+4+3+0
'''


