import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
import random
import csv
import other_insights as ag


def dropout(a, percent, seed):
    # create a copy
    mat = a.copy()
    # number of values to replace
    prop = int(mat.size * percent)
    # indices to mask
    random.seed(seed)
    mask = random.sample(range(mat.size), prop)
    # replace with NaN
    np.put(mat, mask, [np.NaN]*len(mask))
    return mat

def missing_data(db, percentage, seed):
    df = db.copy()
    data = df.values
    modified = dropout(data, percentage, seed)
    new_df = pd.DataFrame(modified)  # Change % of data to NA in the dataset
    columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang',
       'oldpeak', 'slope', 'ca', 'thal']
    new_df.columns = columns
    return new_df

db = pd.read_csv('heart.csv')
df = db[db['target'] == 1]
#df.drop(df.columns[[0]], axis=1, inplace=True)
df.drop(['target'], axis=1, inplace=True)


db_ideal = df.copy()

ideal_topk = ag.generate_correlation_insights_abs(db_ideal)
df_ideal = ag.correlation_ideal_abs(db_ideal)

#print(ideal_topk, len(ideal_topk))


k_list = [5,6,7,8,9,10,11,12,13,15,20,30,40,50,60,70,78]
mlist = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] 

for k in k_list:
	topk, cum_topk = ideal_topk[:k], ag.get_sum_correlation_ideal_abs(k,df_ideal)
	for i in mlist:
	    for j in range(100):
	    	data = missing_data(df, i, j)
	    	temp_topk, cum_missing_topk = ag.generate_correlation_insights_abs(data), ag.get_sum_correlation_insights_cum_abs(k, df_ideal, data)
	    	missing_topk = temp_topk[:k]
	    	with open('results/correlation_missing_vs_ideal_abs.csv', 'a', newline='') as f:
	    		#print(missing_topk, len(missing_topk))
	    		#print(topk, len(topk))
	    		fields = [i*100, k, ag.rboresult(missing_topk, topk), ag.jaccard_similarity(missing_topk, topk), ag.c_d(cum_missing_topk, cum_topk)]
	    		print(fields)
	    		writer = csv.writer(f)
	    		writer.writerow(fields)

        