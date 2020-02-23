from analyze_data import analyze_data
import pandas as pd
import pymongo as pm

def main():

	URI = "mongodb+srv://krypt:cyberhood12345@hackcu-cyberhood-kismet-data-phlpm.gcp.mongodb.net/test?retryWrites=true&w=majority"
	client = pm.MongoClient(URI)
	db = client.cyberhood
	cursor = db.user.find()
	df = pd.DataFrame(list(cursor))
	ad = analyze_data(df)

	#df = pd.read_json("~/Documents/team-cyberhood/kismet_data_example.json", lines=True)
	#ad = analyze_data(df)
	ret = ad.analyze_data()
	print(ret[0])

if __name__ == "__main__":
	main()
