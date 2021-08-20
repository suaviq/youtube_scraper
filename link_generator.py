from yt_libraries import *
from data_structures import *

#for page in yt_polish:
#   find_codes(yt_polish)

HEADER = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

####################################################################################

#this is working    
def find_links(url, n):
    chrome_path = r'C:/Users/alase/Downloads/chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome(chrome_path)
    driver.get(url)
    time.sleep(3)
    list_of_links = []

    #click 'i agree' button to yt cookies
    consent_button_xpath = "//button[@aria-label='Agree to the use of cookies and other data for the purposes described']"
    button = driver.find_element_by_xpath(consent_button_xpath)
    button.click()

    # scroll down till the end of the page
    # get scroll height
    previous_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        # scroll down to bottom
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(3)
        # calculate new scroll height and compare it with last scroll height
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == previous_height:
            break
        previous_height = new_height

    time.sleep(2)

    # find links from whole site
    links=driver.find_elements_by_xpath('//*[@id="video-title"]')

    for link in links:
        print(link.get_attribute("href"))
        list_of_links.append(link.get_attribute("href"))
    
    print('\n\n\n\n')

    # save them to txt file 
    with open(f'links_{n}.txt', 'w') as f:
        for item in list_of_links:
            f.write("%s\n" % item)

    print('done -> find links')

####################################################################################

# extract hashcode from the links saved in txt file
def hashcode(file, name):
    # using regular expressions to extract hashcode from yt link
    list_hashcode = []
    pattern ="=[a-zA-Z0-9_-]*"
    with open(file) as file:
        for line in file:
            match = re.findall(pattern, line) 
            print(match)
            code = str(match)
            clear_code = code.replace('''['=''', '').replace('''']''','')
            list_hashcode.append(clear_code)
            
    # checking if everything is okey
    print('\n\n\n\n')
    for item in list_hashcode:
        print(item)

    # saving clear hashcodes to txt file
    with open(f'hashcodes_{name}.txt', 'w') as f:
        for item in list_hashcode:
            f.write("%s\n" % item)

    print('done -> hashcode')

find_links(yt_polish[0], yt_polish_authors[0])
hashcode(f"links_{yt_polish_authors[0]}.txt", yt_polish_authors[0])

find_links(yt_polish[1], yt_polish_authors[1])
hashcode(f"links_{yt_polish_authors[1]}.txt", yt_polish_authors[1])

