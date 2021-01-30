import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv('RDCDFinal.csv', index_col=0)
print(data.columns)
RD = data.loc[:, ['location', 'Econ_Block', 'Week_Num', 'Weekly_Cases',
                  'Stringency_Indexed', 'population', 'Weekly_Deaths',
                  'DeathsxCases']]
RDEcon = RD.query('Econ_Block== "EU"')
RDEcon = RDEcon.query('location == "Ireland"')
#RDEcon['Week_Case']=(RDEcon['Weekly_Cases'] **3)
RDEcon = pd.DataFrame(RDEcon)
print(RDEcon)


# Chart showing Case numbers over time, against number of deaths
g= sns.relplot(x='Week_Num', y='Weekly_Cases', data=RDEcon, height=2, aspect=1.5, s=200, size='Weekly_Cases', hue='Weekly_Deaths')
g.fig.suptitle('Ireland; Cases & Deaths', x=0.5, y=1.0)
g.set_ylabels('Weekly Cases Recorded')
g.set_xlabels('Week Number')
plt.subplots_adjust(top=0.85)
sns.set_palette("RdBu")
#sns.set(style='whitegrid')
sns.set_context('paper')
#leg=g._legend
#leg.set_bbox_to_anchor([0.5, 0.5])

#leg._loc=2
#fig=ax.get_figure()
#fig.savegig('Ireland; Cases & Deaths.png')
plt.savefig('Ireland; Cases & Deaths.png')
plt.show()
plt.cla()
