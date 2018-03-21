import expanddouban
import csv
from bs4 import BeautifulSoup

"""
	return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category,location):	
	url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}".format(category,location)
	return url

"""
return a list of Movie objects with the given category and location.
"""
class Movie():
	def __init__(self,name,rate,location,category,info_link,cover_link):
		self.name = name
		self.rate = rate
		self.location = location
		self.category = category
		self.info_link = info_link
		self.cover_link = cover_link
	def print_data(self):
		return "{},{},{},{},{},{}".format(self.name,self.rate,self.location,self.category,self.info_link,self.cover_link)	

"""
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location):
	movies = []
	for loc in location:
		html = expanddouban.getHtml(getMovieUrl(category,loc),True)
		soup = BeautifulSoup(html,'html.parser')
		content_a = soup.find(id='content').find(class_='list-wp').find_all('a',recursive=False)
		for element in content_a:
		    M_name = element.find(class_='title').string
		    M_rate = element.find(class_='rate').string
		    M_location = loc
		    M_category = category
		    M_info_link = element.get('href')
		    M_cover_link = element.find('img').get('src')
		    movies.append(Movie(M_name,M_rate,M_location,M_category,M_info_link,M_cover_link).print_data())
		return movies


location_list=["美国"]
my_list1=getMovies("黑色幽默",location_list)
print(my_list1)


with open('movies.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    for m in my_list1:
    	spamwriter.writerow(m)
  

