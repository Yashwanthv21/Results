#import the library used to query a website
import urllib2
#import pandas to convert list to data frame
import pandas as pd
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Take hallticket number as input
hallticket = "13671a1237"

pcode = [[35,1000],[51,750],[62,750],[91,750],[125,750]]

#specify the url
url_first = "http://jbiet.edu.in/jbexamresult.php?pcode="
url_sec = "&htno=" + hallticket + "&jbietapi=hf76h47f&jbietkey=13MQ8UJ618Lgo"
#Generate lists
sub_name=[]
internal_marks=[]
external_marks=[]
total_marks=[]
result=[]

for code in pcode:
	url = url_first + str(code[0]) + url_sec
	print (url)
	#Query the website and return the html to the variable 'page'
	page = urllib2.urlopen(url)

	#Parse the html in the 'page' variable, and store it in Beautiful Soup format
	soup = BeautifulSoup(page)

	#find marks
	subjects = soup.find('table', border="1")
	for subject in subjects.findAll('tr'):
		cells = subject.findAll('td')
		if len(cells) == 5 and cells[0].find(text=True) != " ":
			sub_name.append(cells[0].find(text=True))
			internal_marks.append(cells[1].find(text=True))
			external_marks.append(cells[2].find(text=True))
			total_marks.append(cells[3].find(text=True))
			result.append(cells[4].find(text=True))
	print ("sum is" + str(sum(map(int, total_marks))))

df=pd.DataFrame(sub_name,columns=['Subject Name'])
df['Internal Marks']=internal_marks
df['External Marks']=external_marks
df['Total Marks']=total_marks
df['Result']=result
df
print df

#find name and details
table1 = soup.find('table')
print table1