from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from repos.controller_api import *

# Create your views here.



 

api_controller = RepoController()

class LanguageView(APIView):
	"""
	    Lists the languages used by the 100 trending public repos on GitHub.
	"""
        
	

       def  get(self,request):
                

                data =  [key for key in  api_controller.languages]

              
                #return JsonResponse({'language' :  data})

                return Response({'languages' :  data})

                   
                
class LanguageReposView(APIView):
	"""
	    Lists the languages used by the 100 trending public repos on GitHub.
	"""

            
      
	def get(self,request):
                
		data = api_controller.get_score()    

		return Response({'language-repos' : data})
		
           
	         #or return JsonResponse ({'language-repos':data})

