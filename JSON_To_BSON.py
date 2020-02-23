#JSON to BSON converter

import json
from bson import BSON

bad_json = '{"this is": "missing the closing bracket"'

try:
    json.loads(bad_json)
except ValueError as error:
    print ("json.loads() ValueError for BSON object:", error)

json_string = ""
with open("data.json TYPE:", 'r', encoding='utf-8') as json_data:
    print ("data.json Type:", type(json_data))

    for i, line in enumerate(json_data):
        json_string += line

try:
    json_docs = json.loads(json_string)

    print ("json_docs TYPE:", type(json_docs))

    print ("MongoDB collections:", list(json_docs.keys()))

except ValueError as error:
    print ("json.loads() ValueError for BSON object:", error)
    quit()

for key, val in json_docs.items():

    for i, doc in enumerate(json_docs[key]):
    
        try:
            print ("\ndoc:", doc)

            data = BSON.encode(doc)
            print ("BSON encoded data:", type(data))

            print ("data:", data)

            decode_doc = BSON.decode(data)
            print ("decode_doc:", type(decode_doc))

        except Exception as error:
            print ("enumerate() JSON documents ERROR:", error)
