import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.documents as documents
from rest_framework import generics
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants
import requests
from datetime import date
from django.http import HttpResponse
import os
import json
url = 'https://weatherstorage.documents.azure.com:443/'
key = '9kHm46PZdBvmGpLYFFMhSxT7grL4XCLUC6y4a9d4bbVYh7nJN23B6joi2xh8bXku1dN63qbsVDdHR4kznlCacw=='
client = cosmos_client.CosmosClient(url, {'masterKey': key})

database_name = 'ToDoList'
container_name = 'Items'


# datatoload = [
# 	{
#         "id":"1",
# 		"temperature":20.74,
# 		"humidity":67.68
# 	},
# 	{
#         "id":"2",
# 		"temperature":29.74,
# 		"humidity":37.68
# 	},
# 	{
#         "id":"3",
# 		"temperature":23.74,WeatherforecastbyML
# 	},
# 	{
#         "id":"5",
# 		"temperature":20.74,
# 		"humidity":67.61
# 	},
# 	{
#         "id":"6",
# 		"temperature":20.74,
# 		"humidity":63.68
# 	}
# ]
# headers = {
# "Accept": "application/json",
# "x-ms-version": "2016-07-11",
# "Authorization": key,
# "Cache-Control": "no-cache",
# "Host": "djappdb.documents.azure.com:443",
# "Accept-Encoding": "gzip, deflate",
# "Connection": "keep-alive",
# "cache-control": "no-cache",
# }
class DatabaseManagement:
    # @staticmethod
     def find_database(client, id):
    #     global x
    #     global datatoload
    #     data_name = database_name + str(x)
    #     x+=1
    #     try:
    #         database = client.CreateDatabase({'id': data_name})
    #     except errors.HTTPFailure:
    #         database = client.ReadDatabase("dbs/" + data_name)
    #     containername = data_name + '_cont'            
    #     create_container(containername,['/temprature'],database)   
    #     insert_to_container(containername,database,datatoload)       
    #     get_container_list(containername,database)
        database = client.ReadDatabase("dbs/" + database_name)  
        get_item(container_name,database)
    
        
    # @staticmethod
    # def create_database(client, id):
    #     global x
    #     data_name = database_name + str(x)
    #     x+=1
    #     try:
    #         database = client.CreateDatabase({'id': data_name})
    #     except errors.HTTPFailure:
    #         database = client.ReadDatabase("dbs/" + data_name)
    
    # @staticmethod
    # def read_database(client, id):
    #     print("\n3. Get a Database by id")
    #     global x
    #     x+=1
    #     database_link  = 'dbs/'+database_name + str(x)
    #     try:
    #         # All Azure Cosmos resources are addressable via a link
    #         # This link is constructed from a combination of resource hierachy and 
    #         # the resource id. 
    #         # Eg. The link for database with an id of Foo would be dbs/Foo
           
    #         database = client.ReadDatabase(database_link)
    #         print('Database with id \'{0}\' was found, it\'s _self is {1}'.format(id, database['_self']))

    #     except errors.HTTPFailure as e:
    #         if e.status_code == 404:
    #            print('A database with id \'{0}\' does not exist'.format(id))
    #         else: 
    #             raise

    # @staticmethod
    # def list_databases(client):
    #     print("\n4. List all Databases on an account")
        
    #     print('Databases:')
        
    #     databases = list(client.ReadDatabases())
        
    #     if not databases:
    #         return

    #     for database in databases:
    #         print(database['id'])          

    # @staticmethod
    # def delete_database(client, id):
    #     print("\n5. Delete Database")
    #     global x
        
    #     try:
    #        database_link  = 'dbs/'+database_name + str(x)
    #        client.DeleteDatabase(database_link)

    #        print('Database with id \'{0}\' was deleted'.format(id))

    #     except errors.HTTPFailure as e:
    #         if e.status_code == 404:
    #            print('A database with id \'{0}\' does not exist'.format(id))
    #         else: 
    #             raise

    # def my_database_create(mydatabasename):
    #     data_link = url     
    #     print (data_link) 
    #     myobj = {
    #                 "id": "tempdb"
    #             }

    #     mydat = requests.post(url, headers={'Content-Type': 'application/json', 'Authorization': key,'x-ms-version':xms,'x-ms-date':str(date.today())}, data=json.dumps(myobj))
    #     person_dict = json.loads(mydat.text)
    #     print(person_dict)
        
        

# msg_txt_formatted = MSG_TXT.format(id=1, ts=time_stamp, temperature=temperature,   humidity=humidity, preasure=preasure, count=count)
# MSG_TXT = '{{"id":{id},"Time Stamp": "{ts}","temperature": {temperature},"humidity":{humidity},"preasure" : {preasure},"Packet Count": {count}}}'

# def create_container(container_name,containerpath,mydatabase): 
   
#     container_definition = {'id': container_name,
#                             'partitionKey':
#                                         {
#                                             'paths': containerpath,
#                                             'kind': documents.PartitionKind.Hash
#                                         }
#                             }
#     try:
#         container = client.CreateContainer("dbs/" + mydatabase['id'], container_definition, {'offerThroughput': 400})
#     except errors.HTTPFailure as e:
#         if e.status_code == http_constants.StatusCodes.CONFLICT:
#             container = client.ReadContainer("dbs/" + mydatabase['id'] + "/colls/" + container_definition['id'])
#         else:
#             raise e
        
        
# def get_container_list(container_name,mydatabase):
#     database_id = mydatabase['id']
#     container_id = container_name
#     container = client.ReadContainer("dbs/" + database_id + "/colls/" + container_id)
#     print(json.dumps(container, indent=4, sort_keys=True))
    
    
# def insert_to_container(container_name,mydatabase,payload):
#     database_id = mydatabase['id']
#     container_id = container_name
#     for data in payload:
#         container = client.UpsertItem("dbs/" + database_id + "/colls/" + container_id, data)    



def get_item(container_name,mydatabase):  
    database_id = mydatabase['id']
    container_id = container_name
    response = []
    print ("the container id is {} and name is {}".format(container_id,container_name))
    for item in client.QueryItems("dbs/" + database_id + "/colls/" + container_id,
                              'SELECT top 5 * FROM ' + container_id ,
                              {'enableCrossPartitionQuery': True}):
            response.append(item)
        #print(json.dumps(response, indent=True))
    return HttpResponse(json.dumps(response, indent=True))
# def delete_item(container_name,mydatabase):  
#     database_id = mydatabase['id']
#     container_id = container_name 
#     for item in client.QueryItems("dbs/" + database_id + "/colls/" + container_id,
#                                 'SELECT * FROM products p WHERE p.productModel = "DISCONTINUED"',
#                                 {'enableCrossPartitionQuery': True}):80%
#         client.DeleteItem("dbs/" + database_id + "/colls/" + container_id + "/docs/" + item['id'], {'partitionKey': 'Pager'})        