import pandas as pd

def df_transform(df, row_transformer, new_columns):
	'''
	This function helps to generate new dataframe with same index and new columns
	that are mapped from existing columns

	For example:
	
	# df is dataframe which has first 3 records as following
	year	month	day	product
	19		1		4	de
	17		2		5	ax
	18		3		6	xy
	
	# row_transformer is a map function that has parameter as data series
	def row_transformer(s):
	    date = '20{:02d}-{:02d}-{:02d}'.format(s['year'], s['month'], s['day'])
	    product_id = '{}_20{:02d}{:02d}{:02d}'.format(s['product'], s['year'], s['month'], s['day'])
	    return (date, product_id)
	
	# new column names
	new_columns = ['date', 'product_id']
	
	# transformation
	new_df = df_transform(df, row_transformer, new_columns)

	# The new_df has first 3 records as following
	date		product_id
	2019-01-04	de_20190104
	2017-02-05	ax_20170205
	2018-03-06	xy_20180306
	
	'''

    return pd.DataFrame(df.apply(row_transformer, axis=1).tolist(), columns=new_columns)