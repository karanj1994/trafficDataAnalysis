

# https://www.dataquest.io/blog/web-scraping-tutorial-python/ - reference for Beautiful Soup Training

import requests # Gets the HTML from a webpage
from bs4 import BeautifulSoup # Used to parse HTML
import csv

highwayRankingWebpage = requests.get("https://reason.org/policy-study/24th-annual-highway-report/24th-annual-highway-report-executive-summary/")
extractMainWebPage = BeautifulSoup(highwayRankingWebpage.content, 'html.parser')

allStateCategories = extractMainWebPage.find_all('span', class_='highway-report-state-ranks--category-title')

allCategoryLinks = list(allStateCategories)
# list(allStateCategories)[1].find_all('a', href=True)
eachLink = 0
while eachLink < len(allCategoryLinks):
    categoryWebpage = "https://reason.org" + str(list(allStateCategories)[eachLink].find_all('a', href=True)[0]['href'])
    print("Weblink is this: " + categoryWebpage)
    # print(categoryWebpage)
    categorySpecificWebpage = requests.get(categoryWebpage)
    extractStateWebpage = BeautifulSoup(categorySpecificWebpage.content, 'html.parser')
    tableRanking = extractStateWebpage.find_all('table', class_='tablesorter')
    outputData = []
    if (len(list(tableRanking)[0].find_all('td')) != 153):
        print("Skipping this webpage. Doesn't have the data we need.")
        eachLink += 1
        continue
    extractHeader = list(extractStateWebpage.find_all('h5', class_='table-title'))[0].get_text()
    # print(extractHeader)
    allRankingsSorted = list(tableRanking)[0].find_all('td')
    eachStateData = 0
    while (eachStateData < len(allRankingsSorted)):
        outputData.append(list(allRankingsSorted)[eachStateData].get_text())
        eachStateData += 1
    new_list=[]
    i=0
    while i<len(outputData):
        new_list.append(outputData[i:i+3])
        i+=3
    print(new_list)
    with open("data/" + extractHeader + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(new_list)
    eachLink += 1

# print(len(allStateOverallRanksCount))
# list(allStateOverallRanks.find_all('a', href=True))[0]['href']
# eachState = 0
# while eachState < len(allStateOverallRanksCount):
#     print("State being checked: " + list(allStateOverallRanks.find_all('a', href=True))[eachState].get_text())
#     stateWebpage = "https://reason.org" + list(allStateOverallRanks.find_all('a', href=True))[eachState]['href']
    # print("Weblink is this: " + stateWebpage)
    # stateSpecificWebpage = requests.get(stateWebpage)
    # extractStateWebpage = BeautifulSoup(stateSpecificWebpage.content, 'html.parser')
#     stateStatsValue = extractStateWebpage.find_all('span', class_='highway-report-state-ranks--category-value')    
#     stateStatsTitle = extractStateWebpage.find_all('span', class_='highway-report-state-ranks--category-title')

#     print(stateStatsValue[0].get_text())
#     print(stateStatsTitle[0].get_text())

#     eachState += 1
    


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