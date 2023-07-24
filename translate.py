from colorama import init, Fore
from googletrans import Translator     
import requests


def get_raw_words(count, lang):
    return (requests.get(f"https://random-word-api.herokuapp.com/word?number={ count }&lang={ lang }")).json()


def get_words(data):
    init()
    handler = Translator()
    translate_data = handler.translate(text=data, src="en", dest="ru")
    for i, word in enumerate(translate_data):
        print(Fore.RED + str(data[i]), Fore.RESET + "--->", Fore.GREEN + str(word.text))


if __name__  == "__main__":
    lang = "en"       # Italian(it), Espanian(es), China(zt), French(de), English(en)
    count = "10"     # Words count
    raw_words = get_raw_words(count, lang)
    get_words(raw_words)
