#Marisol Guzman
# Finding the high bins of the E2
# 06-12-16 12:57 pm

from psana import *
import math
import matplotlib.pyplot as plt
import numpy as np
import h5py

h5 = h5py.File('/reg/d/ana01/temp/davidsch/molecular_runs_all.h5', 'r') # this is to get the file that I need
predicted_peaks = h5['predict_enPeaks'][:]
idx2 = h5['predict_enPeaks'][:] == 2 #you have to add the colons to print out whole array of booleans
w = h5['acq.waveforms']
e2pos = h5['regr_predict_acq.e2.pos'][:]# These are all of the e2 positions

NothasNeg1 = np.array(filter(lambda x: x > -1, e2pos)) #Filtering negative numbers out
minNum = min(NothasNeg1)
maxNum = max(NothasNeg1)
minNum = math.floor(minNum*10)/10
maxNum = math.ceil(maxNum*10)/10

binBounds = np.linspace(minNum, maxNum, 20) #makes a list of bounds, there will be 19 bins 
all_bins = []

for i in range(len(binBounds)-1):
	boolbin = np.logical_and(e2pos >= binBounds[i], e2pos < binBounds[i+1])
	boolinterval = np.logical_and(idx2,boolbin)
	if sum(boolinterval) != 0:
		ch0_e2_bin = w[boolinterval, 0, :]
		bin_mean  = np.mean(ch0_e2_bin)
		all_bins += [bin_mean] 
		#The all bins list will have all the bin numbers and find the mean of that bin
	else:
		all_bins += [0]

all_bins = np.array(all_bins) # In the end we end up with 19 things in the array because we ended up making 20 bins

bincountL = []
for i in range(len(all_bins)):
	bincountL += [[binBounds[i], all_bins[i]]]
print bincountL

#print all_bins
plt.plot(binBounds[:-1],all_bins)  # This is graphing the bounds with the means of these bounds
plt.xticks(binBounds[:-1]) #This changes all the ticks to have all of the bounds
plt.savefig('E2HighestBins.png')
plt.show()
# sort the bin with bound from high to low

#These are the highest bins for E1:
# [4.6421052631578945, 303.23645231018645],[4.757894736842105, 361.52516409266411],[4.8736842105263154, 318.08569196428573]

#These are the highest bins for E2:
#[2.9947368421052634, 551.06610209044197], [3.1368421052631579, 677.58659556643897], [3.2789473684210524, 661.40439015803474], [3.4210526315789473,# 475.04051262433052]


	
	





