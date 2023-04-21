import requests
import goose3
from bs4 import BeautifulSoup


def main():
    #url = 'https://www.statista.com/topics/9087/russia-ukraine-war-2022'
    url = 'https://en.wikipedia.org/wiki/Casualties_of_the_Russo-Ukrainian_War'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    soup.find_all('table', class_='wikitable')
    print(soup.find_all('table', class_='wikitable')[2].find_all('tr')[12].find_all('td')[0].text.split(" ")[0])

if __name__ == "__main__":
    main()
