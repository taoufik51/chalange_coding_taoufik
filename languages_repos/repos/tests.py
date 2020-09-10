from django.test import TestCase
from rest_framework import status
from rest_frame.test import APITestCase
from .views import *
from .controller_api import *

# Create your tests here.



                
class RegistrationTestCase(APITestCase):

                
                    self.controller = RepoController()
		
       
                    response  = self.client.post("https://api.github.com/search/repositories?q=created:>2020-09-09&sort=stars&order=desc",self.controller)
                    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

