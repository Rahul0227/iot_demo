import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.documents as documents
import requests
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants
import requests
from datetime import date
import os
import json


class DatabaseManagement1():
    print('.....................................................')
   
    url = 'https://zingacosmodb.documents.azure.com:443/'
    key = 'mgHbGQ74GSZ61S3StNAJof4u930d3UuwR9GQmb3qgQUabzly1CQCRQfC7JMbbEsu6AkmmIu5NU78W391wm4Cbw=='
    client = cosmos_client.CosmosClient(url, {'masterKey': key})
    DATABASE_ID = 'zingacosmodb'
    database_name = 'AzureSampleFamilyDatabase'
    xms = '2016-07-11'
    x=0
    data_name = "items"
    containername = "WeatherforecastbyML" #data_name + '_cont' 
    database = client.ReadDatabase("dbs/items")

    
    
    def get_item(self,query,mydatabase,containername): 
        data = [] 
        database_id = mydatabase['id'] 
        for item in self.client.QueryItems("dbs/" + database_id + "/colls/" + containername ,query ,{'enableCrossPartitionQuery': True}):
            data.append(json.dumps(item, indent=True))
            print(json.dumps(item, indent=True))
        return data
    
    def temp_greater_than(self,value):
        min_val = str(value)
        a = self.get_item('SELECT DeviceData.temperature, DeviceData.humidity,DeviceData.preasure FROM DeviceData WHERE DeviceData.temperature>'+min_val ,self.database, self.containername)
        print(a)
        return a
    
    
    # def temp_less_than(self,value):
    #     min_val = str(value)
    #     a = self.get_item('SELECT DeviceData.temperature, DeviceData.humidity,DeviceData.preasure FROM DeviceData WHERE DeviceData.temperature<'+min_val ,self.database, self.containername)
    #     return a
    # #print(json.dumps(a, indent=True))
    
    # def humidity_in_between(self,val_min,val_max):
    #     min_val = str(val_min)
    #     max_val = str(val_max)
    #     a = self.get_item('SELECT DeviceData.temperature, DeviceData.humidity,DeviceData.preasure FROM DeviceData WHERE DeviceData.humidity BETWEEN '+min_val+' AND '+max_val ,self.database, self.containername)
    #     return a
    
    
    # def between_time(self,val_min,val_max):
    #     min_val = str(val_min)
    #     max_val = str(val_max)
    #     a = self.get_item('SELECT DeviceData.temperature, DeviceData.humidity,DeviceData.preasure FROM DeviceData WHERE DeviceData.gateway_ts BETWEEN '+min_val+' AND '+max_val ,self.database, self.containername)
    #     print(a)
    
    
    # def latest_data(self,value):
    #     min_val = str(value)
    #     a = self.get_item('SELECT top '+min_val+' DeviceData.temperature, DeviceData.humidity,DeviceData.preasure FROM DeviceData order by DeviceData._ts desc',self.database, self.containername)
    #     return a
    
    # def all_data(self,value):
    #     min_val = str(value)
    #     a = self.get_item('SELECT top '+min_val+' * FROM DeviceData order by DeviceData._ts desc',self.database, self.containername)
    #     print(a)