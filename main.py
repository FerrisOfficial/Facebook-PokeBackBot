#imports
import os 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#alerts ingonre
import warnings
warnings.filterwarnings("ignore")

#login details
userName = "Jan@gmail.com"
passWord = "12345678pass"

#login to facebook
os.system('cls')    

option = Options()
option.add_argument("--disable-notifications")
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options, executable_path = r"C:/chromedriver_win32/chromedriver.exe", chrome_options = option)
driver.maximize_window()
driver.get("https://www.facebook.com/pokes")

accept = driver.find_element("xpath", '/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]')
accept.click()

userBox = driver.find_element("xpath", '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/form/div/div[1]/div[1]/input')
userBox.send_keys(userName)

passBox = driver.find_element("xpath", '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/form/div/div[1]/div[3]/input')
passBox.send_keys(passWord)

logBox = driver.find_element("xpath", '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/form/div/div[2]/button')
logBox.click()

#poking
os.system('cls') 

def PokeCheck(pokeBox):
    try:
        pokeText = pokeBox.text
    except:
        print("Error: Text")
        return False
    else:
        if(pokeText[0] == "Z" or pokeText[0] == "W"):
            return False
        return True

counter = 0

while(True):
    try:
        pokeBox = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[1]/div/span/span')
    except KeyboardInterrupt:
        print("Program stopped")
        exit()
    except:
        print("Error: pokeBox")
    else:
        if(PokeCheck(pokeBox)):
            counter += 1
            try:
                print(driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/span/span/span/a').text, counter)
            except:
                print("Error: nameBox")
            else:
                pokeBox.click()
                driver.refresh()
