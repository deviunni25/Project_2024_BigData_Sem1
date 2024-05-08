from pymongo.mongo_client import MongoClient as MgdbClient
from pymongo.server_api import ServerApi as Api
import json
connectionurl = "mongodb+srv://Jo:Jobina@cluster0.9zg8fso.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
Mclient = MgdbClient(connectionurl, server_api=Api('1'))
# Provide an acknowlegement upon succesfull connection
try:
    Mclient.admin.command('ping')
    print("Jobina you have successfully connected to MongoDB!. Welcome to the world of MongoDB")
except Exception as e:
    print(e)

#printing the available databases before creating a new database
print("Databases available : ",Mclient.list_database_names())
#Mclient.drop_database("Jobina")
# 3
mydatabase = Mclient["Project_Database"]
mydatabase["Cars"]
# Open and load the JSON file
with open("C:/Users/email/Downloads/output.json", "r") as file:
    data = json.load(file)

# Insert the data into MongoDB
mydatabase.Cars.insert_many(data)

print("Data inserted successfully!")