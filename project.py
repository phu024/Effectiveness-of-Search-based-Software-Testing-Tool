import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the branches coverage file
branches = pd.read_csv('Branches Coverage.csv')

# Read the Statement coverage file
statements = pd.read_csv('Statement Coverage.csv')

#select the columns of EvoSuite-60s
Evosuite_60s = branches[['Evosuite-60s-1st','Evosuite-60s-2nd','Evosuite-60s-3rd','Evosuite-60s-4th','Evosuite-60s-5th']]

#select the columns of EvoSuite-120s
Evosuite_120s = branches[['Evosuite-120s-1st','Evosuite-120s-2nd','Evosuite-120s-3rd','Evosuite-120s-4th','Evosuite-120s-5th']]

#select the columns of EvoSuite-300s
Evosuite_300s = branches[['Evosuite-300s-1st','Evosuite-300s-2nd','Evosuite-300s-3rd','Evosuite-300s-4th','Evosuite-300s-5th']]

#select the columns of UTBot-60s
UTBot_60s = branches[['UTBot-60s-1st','UTBot-60s-2nd','UTBot-60s-3rd','UTBot-60s-4th','UTBot-60s-5th']]

#select the columns of UTBot-120s
UTBot_120s = branches[['UTBot-120s-1st','UTBot-120s-2nd','UTBot-120s-3rd','UTBot-120s-4th','UTBot-120s-5th']]

#select the columns of UTBot-300s
UTBot_300s = branches[['UTBot-300s-1st','UTBot-300s-2nd','UTBot-300s-3rd','UTBot-300s-4th','UTBot-300s-5th']]

#calculate the average of EvoSuite-60s
Evosuite_60s_avg = Evosuite_60s.mean(axis=1).rename('Evosuite-60s_Mean')

#Evosuite_60s_new
Evosuite_60s_new = pd.concat([Evosuite_60s,Evosuite_60s_avg],axis=1)

#calculate the average of EvoSuite-120s
Evosuite_120s_avg = Evosuite_120s.mean(axis=1).rename('Evosuite-120s_Mean')

#Evosuite_120s_new
Evosuite_120s_new = pd.concat([Evosuite_120s,Evosuite_120s_avg],axis=1)

#calculate the average of EvoSuite-300s
Evosuite_300s_avg = Evosuite_300s.mean(axis=1).rename('Evosuite-300s_Mean')

#Evosuite_300s_new
Evosuite_300s_new = pd.concat([Evosuite_300s,Evosuite_300s_avg],axis=1)

#calculate the average of UTBot-60s
UTBot_60s_avg = UTBot_60s.mean(axis=1).rename('UTBot-60s_Mean')

#UTBot_60s_new
UTBot_60s_new = pd.concat([UTBot_60s,UTBot_60s_avg],axis=1)

#calculate the average of UTBot-120s
UTBot_120s_avg = UTBot_120s.mean(axis=1).rename('UTBot-120s_Mean')

#UTBot_120s_new
UTBot_120s_new = pd.concat([UTBot_120s,UTBot_120s_avg],axis=1)

#calculate the average of UTBot-300s
UTBot_300s_avg = UTBot_300s.mean(axis=1).rename('UTBot-300s_Mean')

#UTBot_300s_new
UTBot_300s_new = pd.concat([UTBot_300s,UTBot_300s_avg],axis=1)

#compare the average of EvoSuite-60s, UTBot-60s Evosuite-120s, UTBot-120s Evosuite-300s, UTBot-300s
compare = pd.concat([Evosuite_60s_avg,UTBot_60s_avg,Evosuite_120s_avg,UTBot_120s_avg,Evosuite_300s_avg,UTBot_300s_avg],axis=1)

#statistics of the average of EvoSuite-60s, UTBot-60s Evosuite-120s, UTBot-120s Evosuite-300s, UTBot-300s
compare.describe()

#compare the average of Sample CUTs, EvoSuite-60s, UTBot-60s Evosuite-120s, UTBot-120s Evosuite-300s, UTBot-300s
compare2 = pd.concat([branches['Sample CUTs'],Evosuite_60s_avg,UTBot_60s_avg,Evosuite_120s_avg,UTBot_120s_avg,Evosuite_300s_avg,UTBot_300s_avg],axis=1)


#branchesCoverage together columns to rows and rename the columns 
branchesCoverage = pd.melt(compare2, id_vars=['Sample CUTs'], value_vars=['Evosuite-60s_Mean','UTBot-60s_Mean','Evosuite-120s_Mean','UTBot-120s_Mean','Evosuite-300s_Mean','UTBot-300s_Mean'], var_name='Tool', value_name='Branches Coverage')
print(branchesCoverage)

#add column of time 
branchesCoverage['Time'] = branchesCoverage['Tool'].str.extract('(\d+)', expand=False)
print(branchesCoverage)

#rename the column of Tool
branchesCoverage['Tool'] = branchesCoverage['Tool'].str.replace('-\d+s_Mean','')
print(branchesCoverage)


# create grouped boxplot branchesCoverage
sns.set(style="whitegrid")
ax = sns.boxplot(x="Time", y="Branches Coverage", hue="Tool", data=branchesCoverage, palette="Set3")
ax.set(xlabel='Time(s)', ylabel='Branches Coverage')
plt.show()
