from rivescript import RiveScript
import requests
from bs4 import BeautifulSoup

class MyObjectHandler:
    def __init__(self):
        self._objects = {}
    def load(self, name, code):
        # name = the name of the object from the RiveScript code
        # code = the source code of the object
        print(name, code)
    def call(self, rs: RiveScript, name, fields, depth):
        # rs     = the current RiveScript interpreter object
        # name   = the name of the object being called
        # fields = array of arguments passed to the object
        question = rs.get_uservar("localuser", "question")
        country = rs.get_uservar("localuser", "country")
        if question is None or question == "undefined":
            return "What do you want to know? For example, I can tell you how many civilians or soldiers died in the Ucraine war."
        if country is None or country == "undefined":
            return "Which country do you prefer? Russia or Ucraine?"
        # Question and country are defined, so we can query
        # Get the table with the information:
        url = 'https://en.wikipedia.org/wiki/Casualties_of_the_Russo-Ukrainian_War'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        table = soup.find_all('table', class_='wikitable')[2]
        if question == "civilians" and country == "ucraine":
            # Get the number estimated by Ukrainian war crimes prosecutor
            killed = table.find_all('tr')[3].find_all('td')[0].text.split(" ")[0]
            date = table.find_all('tr')[3].find_all('td')[1].text
            return "This are the number of killed civilians: " + killed + " on " + date
        elif question == "civilians":
            # Get the number estimated United Nations, because far lower
            killed = table.find_all('tr')[4].find_all('td')[0].text.split(" ")[0]
            date = table.find_all('tr')[4].find_all('td')[1].text
            return "This are the number of killed civilians: " + killed + " on " + date
        elif question == "russian_soldiers" and country == "ucraine":
            killed = table.find_all('tr')[13].find_all('td')[0].text.split(" ")[0]
            date = table.find_all('tr')[13].find_all('td')[1].text
            return "This are the number of killed russian soldiers: " + killed + " on " + date
        elif question == "russian_soldiers":
            killed = table.find_all('tr')[12].find_all('td')[0].text.split(" ")[0]
            date = table.find_all('tr')[12].find_all('td')[1].text
            return "This are the number of killed russian soldiers: " + killed + " on " + date
        elif question == "ukrainian_soldiers" and country == "ucraine":
            killed = table.find_all('tr')[8].find_all('td')[0].text.split("-")[0]
            date = table.find_all('tr')[8].find_all('td')[1].text
            return "This are the number of killed ukrainian soldiers: " + killed + " on " + date
        elif question == "ukrainian_soldiers":
            killed = table.find_all('tr')[7].find_all('td')[0].text.split("")[0]
            date = table.find_all('tr')[7].find_all('td')[1].text
            return "This are the number of killed ukrainian soldiers: " + killed + " on " + date
        return "I can't answer this question."

bot = RiveScript()
bot.load_directory("./eg/brain")
bot.sort_replies()
bot.set_handler("python", MyObjectHandler())
# This function is needed to be able to call the object from RiveScript
def function_test(rs, args):
    pass
# Register the function
bot.set_subroutine("war_function", function_test)
while True:
    msg = input('You> ')
    if msg == '/quit':
        quit()

    reply = bot.reply("localuser", msg)
    print ('Bot>', reply)
