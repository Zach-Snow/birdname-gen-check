from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from main import get_bird_names
import time
from menu import print_menu
import random

chrome_options = Options()
chrome_options.add_argument #("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://www.name.com/domain/search/domain'
name_list = get_bird_names()

while True:
    print("----------------------------------")
    print("SEARCHING...")
    print("----------------------------------")

    n = random.randint(0, len(name_list) - 1)
    domain_name = name_list[n]

    url = 'https://www.name.com/domain/search/' + domain_name + ".com"

    browser.get(url)
    time.sleep(2)
    available = ''
    try:
        available = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[5]/div/div[1]/div/div/div[1]/div/div[1]/span/span[2]').text
    except:
        pass

    print(available)
    if available == 'available' or available == 'Domain':
        print(domain_name + ".com" + " is available!")
        print_menu()
        user_input = input(": ").rstrip()
        while True:
            try:
                user_input = int(user_input)
                break
            except:
                user_input = input(": ").rstrip()
                continue
        if user_input == 1:
            # implement stuff
            new_browser = webdriver.Chrome()
            new_browser.get(url)
            continue
        if user_input == 2:
            # implement stuff
            pass
        if user_input == 3:
            # implement stuff
            break
    else:
        print(domain_name + ".com" + " is taken!")
        continue
