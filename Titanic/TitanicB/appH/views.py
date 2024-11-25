from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import HousePriSerializer
from .models import HousePrModel
from .load_model import ModelHelper
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Create your views here.


class HousePriView(APIView):
  
    def get(self,request):
        self.model_obejects = HousePrModel.objects.all()
        self.serialize = HousePriSerializer(self.model_obejects, many=True)
        return Response(self.serialize.data, status=status.HTTP_200_OK)
    





    def post(self, request, format=None):
        try:
            
            self.modelobj = ModelHelper()
            self.model = self.modelobj.LoadModel()
            self.data = request.data

            features = [[self.data.get("area"), self.data.get("bedrooms"), self.data.get("bathrooms"), self.data.get("stories"),
                          self.data.get("mainroad"), self.data.get("guestroom"), self.data.get("basement"), self.data.get("parking"),
                           self.data.get("prefarea"), self.data.get("furnishingstatus"), self.data.get("luxury_item")]]     
                   
            
            # self.input_data = [[5000.0, 0.0, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,]]
            # self.input_data = torch.tensor(self.input_data, dtype=torch.float32)
            # self.input_data = self.input_data.unsqueeze(0)

            
            self.input_data = torch.tensor(features, dtype=torch.float32)   # making it tensor 
            self.input_data = self.input_data.unsqueeze(0)
            

            # self.model.eval()
            with torch.inference_mode():
                self.test_pred = self.model(self.input_data).item()
                # self.test_pred = self.test_pred.to('cpu').detach().numpy()
            
            context = {'result': self.test_pred, "house_data": features}



            print("\n\n")
            print("Input data is ----> {}".format(context))
            print("\n")

            

            return Response(context, status=status.HTTP_200_OK)
            
        except ValueError as e:
             Response(e.args[0],status=status.HTTP_400_BAD_REQUEST)
        

     

