

# https://www.dataquest.io/blog/web-scraping-tutorial-python/ - reference for Beautiful Soup Training

import requests # Gets the HTML from a webpage
from bs4 import BeautifulSoup # Used to parse HTML

highwayRankingWebpage = requests.get("https://reason.org/policy-study/24th-annual-highway-report/24th-annual-highway-report-executive-summary/")
extractMainWebPage = BeautifulSoup(highwayRankingWebpage.content, 'html.parser')

allStateOverallRanks = extractMainWebPage.find_all('table', class_='tablesorter')[0]
allStateOverallRanksCount = list(extractMainWebPage.find_all('table', class_='tablesorter'))[0].find_all('a', href=True)

print(len(allStateOverallRanksCount))
list(allStateOverallRanks.find_all('a', href=True))[0]['href']
eachState = 0
while eachState < len(allStateOverallRanksCount):
    print("State being checked: " + list(allStateOverallRanks.find_all('a', href=True))[eachState].get_text())
    stateWebpage = "https://reason.org" + list(allStateOverallRanks.find_all('a', href=True))[eachState]['href']
    print("Weblink is this: " + stateWebpage)
    stateSpecificWebpage = requests.get(stateWebpage)
    extractStateWebpage = BeautifulSoup(stateSpecificWebpage.content, 'html.parser')
    # print(list(extractStateWebpage.contents))
    stateStatsValue = extractStateWebpage.find_all('span', class_='highway-report-state-ranks--category-value')    
    stateStatsTitle = extractStateWebpage.find_all('span', class_='highway-report-state-ranks--category-title')
    print(stateStats[0])#.find_all('span', class_='highway-report-state-ranks--category-title')))#[0].get_text()
    print(stateStats[1])

    eachState += 1
    


# print(len(list(allStateOverallRanks)[0].find_all('a', href=True)))
# firstVal = list(allStateOverallRanks)[0].find_all('a', href=True)[0]['href']
#     # Append reason.org in front of every href string
# #firstVal = list(allStateOverallRanks)[0].find_all('a')[0].get_text()
# print(firstVal)


# trafficWebPage = requests.get("https://reason.org/policy-study/24th-annual-highway-report/alabama/")
# extractWebPage = BeautifulSoup(trafficWebPage.content, 'html.parser')

# allAlabamaRanks = extractWebPage.find_all('span', class_='highway-report-state-ranks--category-value')
# # print(allAlabamaRanks)

# firstVal = list(allAlabamaRanks)[0]
# print(len(list(allAlabamaRanks)))
# secondVal = list(firstVal.children)[0]
# print(secondVal)
# val1 = secondVal.get_text()
################
#page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

# #soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup.prettify()) # Prints out the html content of webpage in clean way
# # print(list(soup.children))

# htmlBody = list(soup.children)[2]
# # print(htmlBody)

# paragraphData = list(htmlBody.children)[3]
# print(paragraphData)