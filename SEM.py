# Standard Error of Mean
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import scikit_posthocs as sp
import seaborn as sns
from scipy import stats

df = pd.read_csv("Actin_thickness_data.csv")

df_mean = (df.groupby('label', as_index=False).mean()).T
df_sem = (df.groupby('label', as_index=False).sem()).T
# groups = df.groupby("label").groups

# Set First Row as Header
df_mean.columns = df_mean.iloc[0]
df_mean = df_mean[1:]
df_sem.columns = df_sem.iloc[0]
df_sem = df_sem[1:]
df_sem.to_csv("Actin_sem_data.csv", encoding='utf-8', index=False)
print(df_mean.head())
print(df_sem.head())

my_columns = ["vehicle sem", "12h PT sem", "24h sem", "48h sem"]
df_sem.columns = my_columns
print(df_sem.head())

df_merged = pd.concat([df_mean, df_sem], axis=1)
print(df_merged.head())

#specify x-axis locations
x_ticks = [0,10,20,30,40,49]
#specify x-axis labels
x_labels = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

ax0 =  df_merged.plot(kind = "line", y = "vehicle", yerr = "vehicle sem", linestyle='--', c='blue')
ax1 = df_merged.plot(ax=ax0, kind = "line", y = "12h PT", yerr = "12h PT sem", c='red')
ax2 = df_merged.plot(ax=ax1, kind = "line", y = "24h", yerr = "24h sem", c='green')
df_merged.plot(ax=ax2, kind = "line", y = "48h", yerr = "48h sem", c='lightgreen')
# plt.gca().axes.get_xaxis().set_visible(False)
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.legend(loc='upper right')
plt.xlabel('Distance')
plt.ylabel('Mean Thickness (nm)')
plt.title("Histogram of Actin Thickness")
plt.savefig("Histogram of Actin Thickness Sem.png", bbox_inches='tight')
plt.show()