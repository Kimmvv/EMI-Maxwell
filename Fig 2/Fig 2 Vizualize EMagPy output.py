import pandas as pd
import os
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
os.getcwd()

df = pd.read_csv('EMImatrix_FSA.csv', index_col=0, sep=',')

        ### 3 rows & 3 columns ###

titles = [['HCP1', 'HCP2.5', 'HCP4'], 
          ['VCP1', 'VCP2.5', 'VCP4'],
          ['PRP1', 'PRP2.5', 'PRP4']]

num = [[5,8,11],
       [14,17,20],
       [23,26,29]]


colour = ["b","y","r"]

fig, axes = plt.subplots(nrows = 3, ncols = 3,  sharex=True, sharey=True)

for i, row in enumerate(axes):
    for j, cell in enumerate(row):
        if num[i][j] == 5:
            legend = ["0.1m","0.3m","0.5m"]
        else:
            legend='_nolegend_'
        cell.hist([df[df.columns[num[i][j]]],df[df.columns[num[i][j]+1]],df[df.columns[num[i][j]+2]]], bins='auto', alpha=1, rwidth=0.85,
                  label=legend, color=colour, histtype='step')
        cell.set_title(titles[i][j])
        cell.set_xlim(0,101)
        if i == len(axes) - 1 and j==1:
            cell.set_xlabel("EC$_a$ [mS/m]".format(j + 1))
        if j == 0 and i ==1:
            cell.set_ylabel("Frequency".format(i + 1))

fig.legend(bbox_to_anchor=(1.12, 0.5),loc='center right', borderaxespad=0., title = "Height")
plt.tight_layout()

'''
s1 = 18
i=14 # 5=HCP, 14=VCP, 23=PRP
fig, ax1 = plt.subplots(figsize=(8,6))
#ax2 = ax1.twiny()

#EC
ax1.hist(df[df.columns[i]]   ,alpha=1, rwidth=0.85, histtype='step', label=df.columns[i], color='blue')
ax1.hist(df[df.columns[i+3]] ,alpha=1, rwidth=0.85, histtype='step', label=df.columns[i+3], color='red') 
ax1.hist(df[df.columns[i+6]] ,alpha=1, rwidth=0.85, histtype='step', label=df.columns[i+6], color='magenta')
#Thickness
#ax2.hist(bad[param[i+1]] ,alpha=1, rwidth=0.85, histtype='step', linestyle=('solid'), color='green') 
#ax2.hist(bad[param[i+3]] ,alpha=1, rwidth=0.85, histtype='step', linestyle=('solid'), color='gray')

ax1.set_xlabel('Electrical conductivity [mS/m]',fontsize=(s1))
ax1.set_ylabel('Frequency',fontsize=(s1))
ax1.legend(prop={'size': 14})

ax1.tick_params(axis='both', which='major', labelsize=14)
plt.tight_layout()
'''