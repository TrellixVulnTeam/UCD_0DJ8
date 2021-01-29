import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
data = pd.read_csv('RDCDFinal.csv', index_col=0)

data=(data.pivot_table(values=['Weekly_Cases','DeathsxCases'] , index=['Week_Num'], aggfunc='sum', fill_value=0))
print(data)
fig, ax = plt.subplots()
plt.style.use('seaborn-whitegrid')
ax.plot(data.index, data['Weekly_Cases'], color='b', label='Cases Recorded Globally per Week')
ax.set_ylabel('Weekly Cases', color='b')
ax.tick_params('y', colors='blue')
plt.xlim(1, 39) #to set the axis ...xlim for x axis
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
plt.ylim(0, 2500000) #to set the axis ...xlim for x axis
plt.yticks([500000, 1000000, 1500000, 2000000, 2500000],['0.5m', '1.0m', '1.5m', '2.0m', '2.5m'])
ax2 = ax.twinx()
ax2.plot(data.index, data['DeathsxCases'], color='red', label='Global Deaths as % of Cases')
ax2.set_ylabel('Deaths % of Cases', color='red')
ax2.tick_params('y', colors='red')
ax.set_title('Death Rate peaks while weekly infection rates accelerate')
ax2.annotate('Over 7 in 100 people with disease are dying', xy=(18, 7.2),  xycoords='data',
                xytext=(-35, -80), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)

ax.annotate('Global infections accelerate again', xy=(23, 800000),  xycoords='data',
                xytext=(-0, -40), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"))

plt.legend()
plt.show()
fig.savefig('Death Rate peaks while weekly infection rates accelerate.png')
plt.close()