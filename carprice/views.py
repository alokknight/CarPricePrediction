from rest_framework.decorators import api_view
from rest_framework.views import APIView#
from rest_framework.renderers import JSONRenderer#
# from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse#
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
import sklearn
import numpy as np


# class UserCountView(APIView):
#     """
#     A view that returns the count of active users in JSON.
#     """
#     renderer_classes = [JSONRenderer]

#     def get(self, request, format=None):
#         user_count = User.objects.filter(active=True).count()
#         content = {'user_count': user_count}
#         return Response(content)


#     queryset = User.objects.all()
# renderer_classes = [TemplateHTMLRenderer]
# def get(self, request, *args, **kwargs):
#     self.object = self.get_object()
#     return Response({'predictions': self.object}, template_name='indexcarpriceprediction.html')


standerd_to = StandardScaler()

@api_view(['GET'])
#@renderer_classes([TemplateHTMLRenderer, JSONRenderer])
def Home(request, format=None):

    # self.predictions = self.get_object()
    #return Response(return_data)
    # return Response({'predictions': predictions}, template_name='indexcarpriceprediction.html')
    # return render(request,'indexcarpriceprediction.html',{predictions:self.object})
    return render(request,'indexcarpriceprediction.html')


@api_view(["POST"])
def carpriceprediction(request, format=None):
    Fuel_Type_Diesel=0
    if request.method == "POST":
        Year=0
        Year = int(request.data.get('Year'))
        Present_Price= float(request.data.get('Present_Price'))
        Kms_Driven= int (request.data.get('Kms_Driven'))
        Owner  = int(request.data.get('Owner'))
        Fuel_Type_Petrol=request.data.get("Fuel_Type_Petrol")

        if(Fuel_Type_Petrol=='Petrol'):
            Fuel_Type_Diesel=0
            Fuel_Type_Petrol=1
        elif(Fuel_Type_Petrol=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0

        Year=2021-Year

        Seller_Type_Individual=request.data.get('Seller_Type_Individual')
        if(Seller_Type_Individual=="Individual"):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0


        Transmission_Mannual=request.data.get('Transmission_Mannual')
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0

        result = [Present_Price,Kms_Driven,Owner,Fuel_Type_Diesel]
        model_path = 'ml_model/random_forest_regression_model.pkl'
        classifier = pickle.load(open(model_path, 'rb'))
        prediction = classifier.predict([result])[0]
        predictions = {
            'error' : '0',
            'message' : 'Successfull',
            'prediction' : prediction,
        }

    #     output=round(predictions['prediction'],2)
    #     print(output)
    #     # output=198.657
    #     if output<0:
    #         return render(request,'indexcarpriceprediction.html',prediction_text="Sorry you cannot sell this car")
    #     else:
    #         return render(request,'indexcarpriceprediction.html',prediction_text="You Can Sell The Car at {}".format(output))
    # else:
    #     return render(request,'indexcarpriceprediction.html')

        #for api view
        #return Response(predictions)

        #for json view
        #return JsonResponse({'predictions': predictions})

        return render(request, 'indexcarpriceprediction.html',{'predictions': predictions})


    else:
        return render(request, 'indexcarpriceprediction.html')
