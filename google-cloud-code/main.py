import analyze_data.py
import pandas as pd
import pymongo as pm

def main():

	URI = "mongodb+srv://krypt:cyberhood12345@hackcu-cyberhood-kismet-data-phlpm.gcp.mongodb.net/test?retryWrites=true&w=majority"
	client = pm.MongoClient(URI)
	db = client.gettingStarted()
	cursor = db.people.find()
	df = pd.DataFrame(list(cursor))
	ad = analyze_data(df)


if __name__ == "__name__":
	main()