from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist
from .DatabaseManagement import DatabaseManagement,client
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
from django.http import HttpResponse
import requests
import json

database_name = 'ToDoList'
container_name = 'Items'


# class CreateView(generics.ListCreateAPIView):
#     """This class defines the create behavior of our rest api."""
#     queryset = Bucketlist.objects.all()
#     serializer_class = BucketlistSerializer

#     def perform_create(self, serializer):
#         """Save the post data when creating a new bucketlist."""
#         #datname = 'mydb'+str(DATABASE_ID)
#         DatabaseManagement.find_database(datname)
#         DatabaseManagement.find_database(client, DATABASE_ID)
#         serializer.save()


# class DetailsView(generics.ListAPIView):
#     """This class handles the http GET, PUT and DELETE requests."""
    
#     queryset = Bucketlist.objects.all()
#     serializer_class = BucketlistSerializer
    
# class UpdateView(generics.RetrieveUpdateAPIView):
#     """This class handles the http DELETE requests."""
#     queryset = Bucketlist.objects.all()
#     serializer_class = BucketlistSerializer
#     def perform_update(self, serializer):
#         DatabaseManagement.read_database(client, DATABASE_ID)


# class DeleteView(generics.RetrieveDestroyAPIView):
#     """This class handles the http DELETE requests."""
#     queryset = Bucketlist.objects.all()
#     serializer_class = BucketlistSerializer
#     def perform_destroy(self, serializer):
#         DatabaseManagement.delete_database(client, DATABASE_ID)
        
        
    
# class ListView(generics.ListAPIView):
#     """This class handles the http DELETE requests."""

#     queryset = Bucketlist.objects.all()
#     serializer_class = BucketlistSerializer    
    
    
class WeatherData(generics.ListAPIView):
    def get(self,request):  
        
        response = []
       
       # dict_body = json.loads(request.body)
        database_id = "ToDoList"
        container_id = 'Items'
        
        
        # database_id = dict_body['id']
        # container_id = dict_body['containername']
        for item in client.QueryItems("dbs/" + database_id + "/colls/" + container_id,
                                #'SELECT * FROM ' + container_id ,
                                #'SELECT top 5 * FROM ' + container_id ,
                                'SELECT top 1 * FROM ' + container_id + " order by " + container_id + " ._ts desc " ,
                                #'SELECT * FROM ' + container_id + " WHERE " + container_id + " .temperature BETWEEN 20 AND 35 " ,
                                #'SELECT * FROM ' + container_id + " WHERE " + container_id + " .temperature > 30 " ,
                                #'SELECT * FROM ' + container_id + " WHERE " + container_id + " .temperature < 30 " , 


                                {'enableCrossPartitionQuery': True}):
            response.append(item)
        return HttpResponse(json.dumps(response, indent=True))
       
    
