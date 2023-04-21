import re
import sys
from rivescript import RiveScript


bot = RiveScript(utf8=True, debug=False)
bot.unicode_punctuation = re.compile(r'[.,!?;:]')
bot.load_directory("eg/brain")
bot.sort_replies()
msg = sys.argv[1]
def response(text):
    reply = bot.reply("localuser", text)
    return reply

def main():        
    input_text = msg
    reply_text = response(input_text)
    print ("Bot: " + str(reply_text)) 
if __name__ == "__main__":
    main()