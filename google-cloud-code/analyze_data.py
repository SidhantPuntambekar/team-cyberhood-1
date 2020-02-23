import pandas as pd
import numpy as np

class analyze_data:
	df = None

	def __init__(self, dataframe):
		self.df = dataframe

	def analyze_data(self):
		return self.df

	def set_df(self, dataframe):
		self.df = dataframe
