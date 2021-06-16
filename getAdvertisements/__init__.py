import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://hsneighborlycosmosacc:ULd2iw7gRbXVyxZrAn9ZJg0GRFwNNIV5TjLmAck34qIxcVIo27fltiHHFqY6OahdHZFuIFBkU0cWhFHs2SZVbQ==@hsneighborlycosmosacc.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@hsneighborlycosmosacc@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['hsneighborlycosmosdb']
        collection = database['advertisements']

        print("connected to mongodb")

        result = collection.find({})
        result = dumps(result)
        print("result")
        print(result)
        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

