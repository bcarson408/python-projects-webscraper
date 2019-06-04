from bs4 import BeautifulSoup
import requests
import lxml


players_dict = {}
players=[]


def returnSoup(url):
	response = requests.get(url)
	page = response.content
	return BeautifulSoup(page,'lxml')

def table_rows(table):
	team_dict = {}
	thisWeek_dict ={}
	week_of_season = ""
	for row in table[0].findAll('tr'):
		line=[]
		for cell in row.findAll('td'):
			line.append(cell.text)
		print(line)


def main():
  base_url ="https://www.cbssports.com/fantasy/football/stats/posvsdef/"
  my_soup = returnSoup(base_url)
  mytext = my_soup.get_text(strip=True)
  doc_table = my_soup.findAll("table")
  table_rows(doc_table)

main()
