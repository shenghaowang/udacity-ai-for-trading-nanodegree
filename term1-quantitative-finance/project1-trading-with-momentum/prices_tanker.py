import pandas as pd
import heapq

def isNlargest(row, cut):
	return row.apply(lambda x: int(x >= cut))

def propogate(row):
	cut = heapq.nlargest(2, row)[-1]
	return isNlargest(row, cut) 

d = {
	'col1': [1, 2],
	'col2': [3, 4],
	'col3': [5, 6]
}
df = pd.DataFrame(data=d)
print(df)

#for index, row in df.iterrows():
#	cut = heapq.nlargest(2, row)[-1]
#	print(cut)
#	row = row.apply(lambda x: int(x >= cut))
	#print(row)
new_df = df.apply(propogate, axis=1)
print(new_df)
