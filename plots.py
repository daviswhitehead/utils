'''Author: Davis Whitehead
'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def corr_plot(df):
	mask = np.zeros_like(df.corr())
	mask[np.triu_indices_from(mask)] = True
	with sns.axes_style("white"):
		sns.heatmap(df.corr(), mask=mask, annot=True, linewidths=.1)


def scatter_matrix(df):
	pd.scatter_matrix(df, alpha=0.2, figsize=(15, 15), diagonal='kde')


if __name__ == '__main__':
	main()

