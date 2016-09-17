'''Author: Davis Whitehead
'''

import pandas as pd

def category_to_factor(df, category_col):
	""" Takes a column with categorical data and
		makes a column of incrementing ints per
		unique value.
	"""
	mapper = {}
	for i, x in enumerate(df[category_col].unique()):
		mapper.update({x: i})
	df[category_col + '_int'] = df[category_col].map(mapper).astype(int)

	return df

if __name__ == '__main__':
	main()

