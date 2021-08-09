import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

col_names = ["TIME", "MOTES", "messages"]

####### Put the file you want to parse ######
BBRdata = pd.read_csv('timeout0_55BBR_TOPO_ringvs4_30min.txt', header = None , sep='\t', names=col_names)
COAPdata= pd.read_csv('timeout0_55CoAP_TOPO_RING_30min.txt', header = None, names=col_names, sep='\t')

#### data1   here we filter data through numbers of Sending messages , you can change this keywords "Sending"
### to the keyword you want to filter example ; Received ACK #######
our_code=BBRdata[BBRdata.messages.str.contains('Sending', regex= True, na=False)]
our_code.messages=our_code.messages.str.replace(r'\D+', '').astype('int')

##### data 2  same goes here ###########
default_code=COAPdata[COAPdata.messages.str.contains('Sending', regex= True, na=False)]
default_code.messages=default_code.messages.str.replace(r'\D+', '').astype('int')

motes = "ID:"
# 13 is the number of motes in our example you could change it to your need
motes=[motes+str(i) for i in range(13)]
#####number of subplot in one figure ########

plt.figure(figsize=(15,15))
for i in range(1,13):
    ourmotes= our_code.loc[(our_code['MOTES'] == motes[i])]
    defaultmotes= default_code.loc[(default_code['MOTES'] == motes[i])]
    plt.subplot(4,3, i,)

    ##### formula to compare bandwith from data1 vs data2 you can change the formula as you need
    plt.plot(defaultmotes.TIME/1000, defaultmotes.messages/defaultmotes.TIME/1000, 'b', label=motes[i]+ 'Data1 ')
    plt.plot(ourmotes.TIME/1000, ourmotes.messages/ourmotes.TIME/1000, 'r--', label=motes[i]+ 'Data2 ')
    plt.legend()
    plt.suptitle("debit ", fontsize=20)

    #### Saving the result in a png image
    plt.savefig('debit Ring Topo_timeout=2.png')
plt.show()

