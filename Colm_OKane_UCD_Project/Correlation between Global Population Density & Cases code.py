import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams

#Bubble Chart, cases per Area on YTD Wk39
data = pd.read_csv('RDCDFinal.csv', index_col=0)
data=data.query('Week_Num== 39')
PopDen=(data.pivot_table(values=['PopKM2'], index='location', aggfunc='sum', fill_value=0, margins=True, margins_name='Grand_Total').iloc[:-1,:])
PopDen.to_csv('PopDen.csv')
CaseArea=(data.pivot_table(values=['CasesxArea'], index='location', aggfunc='sum', fill_value=0, margins=True, margins_name='Grand_Total').iloc[:-1,:])
CaseArea.to_csv('CaseArea.csv')
print(CaseArea)


data2= pd.read_csv('PopDen.csv')
data2a=data2.sort_values('location')
print(data2a)
data3 = pd.read_csv('CaseArea.csv')
data3a=data3.sort_values('location')
print(data3a)

fig, ax =plt.subplots()
plt.scatter(data3a['CasesxArea'], data2a['PopKM2'], s=data3a['CasesxArea'])


plt.xlabel('Cases per Mi²')
plt.ylabel('Population Density (per Mi²)')
plt.title('Correlation between Population Density & Cases Globally')
plt.xlim(0, 150) #to set the axis ...xlim for x axis
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
plt.yscale('log')
#plt.ylim(0, 25000) #to set the axis ...xlim for x axis


plt.yticks([50, 250, 500, 1000, 2500, 5000, 10000, 20000],['50/Mi²','250/Mi²', '500/Mi²', '1000/Mi²', '2500/Mi²', '5000/Mi²', '10000/Mi²', '20000/Mi²'])

plt.grid(True)
# Additional customizations
ax.annotate('Monaco recorded 107 cases per Mi²', xy=(107, 20000),  xycoords='data',
                xytext=(-10, -30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True, color='red')
ax.annotate('Bahrain 106 cse/Mi²', xy=(106, 2600),  xycoords='data',
                xytext=(-15, -50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True )
ax.annotate('Singapore 83 cse/Mi²', xy=(83, 8400),  xycoords='data',
                xytext=(-15, -50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True )

plt.text(3, 80, '} Lower Cases per Mi² where Population Density is lower')

plt.show()
fig.savefig('Correlation between Population Density & Cases Globally.png')
plt.close()