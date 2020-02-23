import pandas as pd
import numpy as np

class analyze_data:
	df = None

	def __init__(self, dataframe):
		self.df = dataframe

	def analyze_data(self):

		ret = []

		dfDangerOS = self.df.loc[(self.df["kismet-device-base-manuf"] == "Unknown")].copy()
		dfSig = self.df["kismet-device-base-signal"]

		dctSigMax = {}
		for i in range(0,len(self.df)):
			#dctSigMax[self.df["kismet.device.base.macaddr"][i]] = self.df["kismet.device.base.signal"][0]["kismet.common.signal.max_signal"]
			dctSigMax["row" + str(i)] = [self.df["kismet-device-base-macaddr"][i], self.df["kismet-device-base-signal"][i]["kismet-common-signal-max_signal"]]

		dfSigMax = pd.DataFrame.from_dict(dctSigMax, orient="index")
		dfSigMax.columns = ["Mac Addr", "Max Sig"]

		upperQuart = dfSigMax["Max Sig"].quantile(.75)
		lowerQuart = dfSigMax["Max Sig"].quantile(.25)
		median = dfSigMax["Max Sig"].quantile(.5)

		innerQuartRange = (upperQuart - lowerQuart) * 1.5

		dfOutlier = dfSigMax.loc[(dfSigMax["Max Sig"] > (median + innerQuartRange)) | (dfSigMax["Max Sig"] < (median - innerQuartRange))]

		ret.append(dfOutlier)
		ret.append(dfDangerOS)	

		return ret

	def set_df(self, dataframe):
		self.df = dataframe