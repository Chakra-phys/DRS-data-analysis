# This program provides violin plot for ICOHP at three different charge states.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df1=pd.read_csv('ICOHPLIST.lobster', delim_whitespace=True)
df2=pd.read_csv('path/ICOHPLIST.lobster', delim_whitespace=True)
df3=pd.read_csv('path/ICOHPLIST.lobster', delim_whitespace=True)
df11=df1.iloc[0:18]
df12=df1.iloc[19:37]
df21=df2.iloc[0:18]
df22=df2.iloc[19:37]
df31=df3.iloc[0:18]
df32=df3.iloc[19:37]

df1.head()
#df2.describe()

icohp11 = np.array(df11["eF"], dtype=np.float32)
icohp12= np.array(df12["eF"], dtype=np.float32)
icohp21 = np.array(df21["eF"], dtype=np.float32)
icohp22= np.array(df22["eF"], dtype=np.float32)
icohp31 = np.array(df31["eF"], dtype=np.float32)
icohp32= np.array(df32["eF"], dtype=np.float32)

fig, axes=plt.subplots()

axes.violinplot(dataset=[icohp11,icohp12,icohp21,icohp22,icohp31,icohp32],showmeans=True,showextrema=True, showmedians=True)#df1["ICOHP(eF)"].astype(np.float32))

axes.set_ylabel('ICOHP for Mn-O')
axes.tick_params(labelbottom=False, bottom=False)
plt.show()

# Average of up and down

icohp1=0.5*(icohp11+icohp12)
icohp2=0.5*(icohp21+icohp22)
icohp3=0.5*(icohp31+icohp32)

fig, axes=plt.subplots()
axes.violinplot(dataset=[icohp1,icohp2,icohp3],showmeans=True,showextrema=True)#, showmedians=True)
axes.set_ylabel('ICOHP for Mn-O',fontsize='x-large')
axes.set_ylim(-1.7,-0.4)
axes.tick_params(labelbottom=False, bottom=False)
plt.savefig('Mn-O-cohp-avg.tif',dpi=500)
plt.show()
