from colorama import Fore, Back, Style
import requests
from bs4 import BeautifulSoup
def select():
    palte = input(Fore.MAGENTA+Style.NORMAL+"palte : "+Fore.WHITE)
    url = F"http://aladl.adnan-alharbi.com/bills/{palte}.html"
    req = requests.get(url=url)
    src = req.content
    soup = BeautifulSoup(src,"lxml")
    selecteds = soup.find_all("span")
    if not  selecteds :
       print(Fore.RED+"There is no customer on this Plate")
    else:
         for x in range(8):
            if x == 0:
                print(Fore.MAGENTA+Style.NORMAL+"Name : "+Fore.WHITE+selecteds[0].text.strip())
            elif x == 1:
                print(Fore.MAGENTA+Style.NORMAL+"Mobile : "+Fore.WHITE+selecteds[1].text.strip())
            elif x == 2:
                print(Fore.MAGENTA+Style.NORMAL+"Reform : "+Fore.WHITE+selecteds[2].text.strip())
            elif x == 3:
                print(Fore.MAGENTA+Style.NORMAL+"Guarantees : "+Fore.WHITE+selecteds[3].text.strip())
            elif x == 4:
                print(Fore.MAGENTA+Style.NORMAL+"hand made : "+Fore.WHITE+selecteds[4].text.strip())
            elif x == 5:
                print(Fore.MAGENTA+Style.NORMAL+"Spare parts : "+Fore.WHITE+selecteds[5].text.strip())
            elif x == 6:
                print(Fore.MAGENTA+Style.NORMAL+"total : "+Fore.WHITE+selecteds[6].text.strip())
            elif x == 7:
                print(Fore.MAGENTA+Style.NORMAL+"Exit date: "+Fore.WHITE+selecteds[7].text.strip())


select()
