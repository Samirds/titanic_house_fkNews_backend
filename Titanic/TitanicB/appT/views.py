from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import TitanicSerializer
from .models import TitanicModel
import pickle
from . ml_model_helper import ProcessTestData




# Create your views here.


class TitanicView(APIView):
  
    def get(self,request):
        model_obejects = TitanicModel.objects.all()
        serialize = TitanicSerializer(model_obejects, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)


    # def post(self, request, format=None):
    #     serializers = TitanicSerializer(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response({'msg': 'Registration Succesfull'}, status=status.HTTP_201_CREATED)
        
    #     return Response(serializers.errors)

    def post(self, request, format=None):
        try:
            
            mdl = pickle.load(open("appT/pklModel.pkl", 'rb'))
            data = request.data
            features = [[data.get("age"), data.get("fare"), data.get("pclass"), data.get("gender"), data.get("sbsp"), data.get("parch"), data.get("cabin"), data.get("embarked")]]            
            pr = ProcessTestData(features) # process data basically encode the data into model's ideal form
            process_data = pr.imputerFrTest()
            result = mdl.predict([process_data])[0]
            context = {'result': result, "titanic_data": data}
            return Response(context, status=status.HTTP_200_OK)
            
        except ValueError as e:
             Response(e.args[0],status=status.HTTP_400_BAD_REQUEST)
        

     


