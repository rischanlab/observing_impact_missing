import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

input_file = 'results/missing_a_m_vs_ideal.csv'

output_plot = '10_missing_a_m_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file, names=['percentage','k','RBO','Jaccard','Cumulative_distance'])

percent = 10
#[5, 10, 15, 50, 100, 256]
k5j = df[(df['k'] == 5) & (df['percentage'] == percent)]
k5j = k5j['Jaccard']
k10j = df[(df['k'] == 10) & (df['percentage'] == percent)]
k10j = k10j['Jaccard']

k50j = df[(df['k'] == 50) & (df['percentage'] == percent)]
k50j = k50j['Jaccard']

k80j = df[(df['k'] == 70) & (df['percentage'] == percent)]
k80j = k80j['Jaccard']


k100j = df[(df['k'] == 126) & (df['percentage'] == percent)]
k100j = k100j['Jaccard']


#RBO
k5r = df[(df['k'] == 5) & (df['percentage'] == percent)]
k5r = k5r['RBO']
k10r = df[(df['k'] == 10) & (df['percentage'] == percent)]
k10r = k10r['RBO']

k50r = df[(df['k'] == 50) & (df['percentage'] == percent)]
k50r = k50r['RBO']

k80r = df[(df['k'] == 70) & (df['percentage'] == percent)]
k80r = k80r['RBO']

k100r = df[(df['k'] == 126) & (df['percentage'] == percent)]
k100r = k100r['RBO']


k5c = df[(df['k'] == 5) & (df['percentage'] == percent)]
k5c = k5c['Cumulative_distance']
k10c = df[(df['k'] == 10) & (df['percentage'] == percent)]
k10c = k10c['Cumulative_distance']

k50c = df[(df['k'] == 50) & (df['percentage'] == percent)]
k50c = k50c['Cumulative_distance']

k80c = df[(df['k'] == 70) & (df['percentage'] == percent)]
k80c = k80c['Cumulative_distance']

k100c = df[(df['k'] == 126) & (df['percentage'] == percent)]
k100c = k100c['Cumulative_distance']



k5j = list(mean_confidence_interval(k5j))
k5j.insert(0,5)
k5j.insert(1,'Jaccard')
k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,10)
k10j.insert(1,'Jaccard')

k50j = list(mean_confidence_interval(k50j))
k50j.insert(0,50)
k50j.insert(1,'Jaccard')

k80j = list(mean_confidence_interval(k80j))
k80j.insert(0,70)
k80j.insert(1,'Jaccard')

k100j = list(mean_confidence_interval(k100j))
k100j.insert(0,126)
k100j.insert(1,'Jaccard')


k5r = list(mean_confidence_interval(k5r))
k5r.insert(0,5)
k5r.insert(1,'RBO 0.95')
k10r = list(mean_confidence_interval(k10r))
k10r.insert(0,10)
k10r.insert(1,'RBO 0.95')

k50r = list(mean_confidence_interval(k50r))
k50r.insert(0,50)
k50r.insert(1,'RBO 0.95')

k80r = list(mean_confidence_interval(k80r))
k80r.insert(0,70)
k80r.insert(1,'RBO 0.95')

k100r = list(mean_confidence_interval(k100r))
k100r.insert(0,126)
k100r.insert(1,'RBO 0.95')


k5c = list(mean_confidence_interval(k5c))
k5c.insert(0,5)
k5c.insert(1,'Cumulative_distance')
k10c = list(mean_confidence_interval(k10c))
k10c.insert(0,10)
k10c.insert(1,'Cumulative_distance')

k50c = list(mean_confidence_interval(k50c))
k50c.insert(0,50)
k50c.insert(1,'Cumulative_distance')

k80c = list(mean_confidence_interval(k80c))
k80c.insert(0,70)
k80c.insert(1,'Cumulative_distance')

k100c = list(mean_confidence_interval(k100c))
k100c.insert(0,126)
k100c.insert(1,'Cumulative_distance')


df = pd.DataFrame([k5j, k10j,k50j, k80j, k100j, k5r, k10r, k50r, k80r, k100r, k5c, k10c, k50c, k80c, k100c])
df.columns = ['k','measurement','mean','lb','ub']

mean0 = df[df['measurement'] == 'Jaccard'].reset_index()
mean0 = mean0['mean']
ub0 = df[df['measurement'] == 'Jaccard'].reset_index()
ub0 = ub0['ub']
lb0 = df[df['measurement'] == 'Jaccard'].reset_index()
lb0 = lb0['lb']

mean1 = df[df['measurement'] == 'RBO 0.95'].reset_index()
mean1 = mean1['mean']
ub1 = df[df['measurement'] == 'RBO 0.95'].reset_index()
ub1 = ub1['ub']
lb1 = df[df['measurement'] == 'RBO 0.95'].reset_index()
lb1 = lb1['lb']

mean2 = df[df['measurement'] == 'Cumulative_distance'].reset_index()
mean2 = mean2['mean']
ub2 = df[df['measurement'] == 'Cumulative_distance'].reset_index()
ub2 = ub2['ub']
lb2 = df[df['measurement'] == 'Cumulative_distance'].reset_index()
lb2 = lb2['lb']

# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (14, 14))
# Font size to 14
matplotlib.rc('font', size = 25)
# Do not display top and right frame lines
matplotlib.rc('axes.spines', top = False, right = False)
# Remove grid lines
matplotlib.rc('axes', grid = False)
# Set backgound color to white
matplotlib.rc('axes', facecolor = 'white')


t = np.arange(len(mean0))

_, ax = plt.subplots()
# Plot the data, set the linewidth, color and transparency of the
# line, provide a label for the legend
ax.plot(mean0, lw = 1, color = '#539caf', alpha = 1, label = 'Jaccard', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean1, lw = 1, color = '#b65332', alpha = 1, label = 'RBO 0.95', marker='<', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#5be19a', alpha = 1, label = 'Cumulative distance', marker='o', linestyle='-', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb0, ub0, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb1, ub1, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#5be19a', alpha = 0.4)


# Label the axes and provide a title
ax.set_title("Impact of k on Effectiveness, 10 % A+M missing")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness - Missing on A+M to Ideal")
x = [5, 10, 50, 70, 126]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
