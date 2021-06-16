import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "AccountEndpoint=https://hsneighborlycosmosacc.documents.azure.com:443/;AccountKey=h56x0NaruDZCCp1JVYNGHteH9rJd9XXHTdEEZtWd0PSaI4IAeRVHFKNMjnScEzlWGNf7ARluxvPa7PUkutVfOA==;"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['hsneighborlycosmosacc']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

