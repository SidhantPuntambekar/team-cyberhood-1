from analyze_data import analyze_data
import pandas as pd

def main():

	#URI = "mongodb+srv://krypt:cyberhood12345@hackcu-cyberhood-kismet-data-phlpm.gcp.mongodb.net/test?retryWrites=true&w=majority"
	#client = pm.MongoClient(URI)
	#db = client.gettingStarted()
	#cursor = db.people.find()
	#df = pd.DataFrame(list(cursor))
	#ad = analyze_data(df)

	df = pd.read_json("kismet_data_example.json")
	ad = analyze_data(df)
	ad.analyze_data().head()


if __name__ == "__main__":
	main()