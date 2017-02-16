from pandas import read_csv
from pprint import pprint
from glob import glob
import os


def CountZero(filename):
	df = read_csv(filename,names = ['stepname', 'stepcount'])
	df_length = df.count()[1]
	if df_length == 0:
		out = 'empty file'
	else:
	    out = 0
    	matrix1 = df.as_matrix()
    	for i1 in range(df_length):
    		if matrix1[i1][1] == 0:
    			out +=1
    	return out

#change directory path as per use
directory = raw_input('enter the path/directory \t')
#directory = "/home/kshitij/Music/logAnalysis/"

csv_files = glob(directory + "/*.csv")  
final_csv_files = []
for f in csv_files:
	if not os.path.isdir(f):
		final_csv_files.append(f)



CountZeroList = [[CountZero(f),f[len(directory):]] for f in final_csv_files]
pprint(CountZeroList)

EmptyFiles = [ y1[1] for y1 in CountZeroList if (y1[0] == 'empty file')]
print 'In particular, these', len(EmptyFiles), 'files are empty' 
pprint(EmptyFiles)

