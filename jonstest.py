import csv
import scipy
import numpy as np
import pandas as pd

from scipy.sparse import dok_matrix
# Reads csv file 


with open('patientlist.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		#patientlist = [None]*22000 # need to learn how many lines in a csv in general
		patientlist = []
		ens_list = [] # this will store the ENS IDs 
		avg_list = [] # will store averages among the 7 patients, both lists built simulataneously 
	
		i = 0
		firstrow = next(readCSV)
		for row in readCSV:
			 # probably unnecessary at this point since using enslist
				#print(Dforward.get(row[0]))
				#row[0] = Dforward.get(row[0])
				#patientlist[Dforward.get(row[0])] = row;
			ens_list.append(row[0])
			patientlist.append(row[1:])
			vals = [float(j) for j in row[1:]]
			avg_i = np.mean(vals)
			#print(avg_i)
			avg_list.append(avg_i)
			i = i + 1;

		#print(avg_list);
		#print(ens_map)
		#print(patientlist[8068]);
		S = sorted(range(len(avg_list)), key=lambda k: avg_list[k]) # this returns indices of avg_list such that
		# S[0] is the index of the smalles element of avg-list and so on, will also allow us to get the ens is correspo
		# to smallest avg 
		#print(S);
		S_sorted = [(ens_list[i],avg_list[i]) for i in S]
		print(S_sorted[-100:]);

		pd.DataFrame(S_sorted[-100:]).to_csv('sortedlist.csv')

		# the whole list goes from tiny numbers around 0 up to 72517, total elems around 20000
		#last 100 elems range from 1000 to 72000, roughly