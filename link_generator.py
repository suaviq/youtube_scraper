from yt_libraries import *

#for page in yt_polish:
#   find_codes(yt_polish)

HEADER = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}
def scroll_down(url):
    chrome_path = r'C:/Users/alase/Downloads/chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome(chrome_path)
    driver.get(url)
    time.sleep(2)
    previous_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(3)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == previous_height:
            break
        previous_height = new_height

def find_codes(url):
    # page = ''
    # while page == '':
    #     try:
    #         page = requests.get(url).text
    #         break
    #     except:
    #         print("Connection refused by the server..")
    #         print("Let me sleep for 5 seconds")
    #         print("ZZzzzz...")
    #         time.sleep(5)
    #         print("Was a nice sleep, now let me continue...")
    #         continue
    # response = requests.get(url, headers=HEADER)
    # page =response.text
    # soup = BeautifulSoup(page,'html.parser')
    # print(soup.prettify())
    chrome_path = r'C:/Users/alase/Downloads/chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome(chrome_path)
    driver.get(url)
    time.sleep(2)

    
    #click 'i agree' button to yt cookies
    # folder = driver.find_element_by_xpath("//@div[@class='VfPpkd-RLmnJb']")
    # actionchains = ActionChains(driver)
    # ActionChains(driver).double_click(folder).perform()
    # scroll down till the end of the page
    scroll_down(url)

    # find links of all the
    links=driver.find_elements_by_xpath('//*[@id="video-title"]')
    for link in links:
        print(link.get_attribute("href"))
    
    # df = pd.DataFrame(columns = ['link', 'title'])

find_codes("https://www.youtube.com/user/vroobelekbillie/videos")


    
