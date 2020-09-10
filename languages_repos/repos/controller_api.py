import requests
import datetime



def date_from_last_30():
	"""
	    Return the last 30 days using str of string
	"""

	date = datetime.datetime.now() - datetime.timedelta(days=30)  # using string  

	return date.strftime('%Y-%m-%d')                              # YYYY-MM-DD date format

class  RepoController:

                 def __init__(self):
		                  self.api_data = self.get_api_repos_data_github()             
		                  self.fetching_data = self.get_repos_fetching()                
		                  self.languages = self.get_languages_data()              
		                  self.score =  self.get_list_and_score_of_repos()


                 def get_api_repos_data_github( self):
                                  number_repos = 100
                                  start_date =  date_from_last_30()
                                  url = f"https://api.github.com/search/repositories?q=created:>{start_date}&sort=stars&order=desc" 
                                  data = requests.get(url).json()
                                  if url == number_repos :
                                             
                                            url += number_repos
                                            
                                  elif data ==  url :
                                     
                                            url += data
                                  else:
                                            data  !=  url

                                  return    data

                 def get_repos_fetching(self):

                                    data_number = list(zip (self.api_data.items()))
                     
                                    data_item =(lambda  name :(name.get("language"),name.get("url_language")),data_number) 

                                    return data_item


                 def  get_languages_data(self):

                                   language_item =  self.fetching_data 
                                   languages_update = set() 
                                  

                                   languages=list (requests.get(language_item[1]).json().items())
                                   languages  = set(languages)
                                  
                                   languages_update   = language_item.append({language_item [0]:languages})
                                   languages = set(languages)

                                   languages_update  = languages_update.union(languages) 
                                   

                                   return  languages_update

                                
                 def get_list_and_score_of_repos(self):

                                  

                                    languages  = get_repos_fetching()

                                    data_dictionary =  list ( zip (languages.items([] for language in languages)))
                                    

                                  
                                                             
                                    data_dictionary[language].append(language)

                                    return data_dictionary 

                 def get_score(self):

                         
                                  
                                   score = get_languages_from_data()


                                   data =  self.score
                                   


  
                                   score = {"Repos data number":data.__len__(),"List of repos":data}


                                   return score
                                   
#def date_from_last_30():
#Return the last 30 days using str of string

#def __init__(self):          
#initialize the methods used  and get the results of  API

#def get_api_repos_data_github( self):
#Search the  repos created in the last 30 days

#def get_repos_fetching(self):
#Get repos name , url , date , language

#def  get_languages_data(self):
#get  the score of every data : repos  , url  date , language


                                



              

                                
