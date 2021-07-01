import time

from tqdm import tqdm

from utils import raiseErrors

from urllib.parse import quote_plus
from urllib.request import urlopen

from bs4 import BeautifulSoup
from selenium import webdriver

downloadDir = './DownloadImgs/'
SCROLL_PAUSE_SEC = 2

class Crawling:
    def __init__(self, browser, crawlCount, searchWord):
        self.browserDriver = self.checkBrowser(browser)
        self.url = f"""https://www.google.com/search?q={quote_plus(searchWord)}
                       &tbm=isch&ved=2ahUKEwjGh-qqh8LxAhVEUvUHHapYAJgQ2-cCegQIABAA&oq=%EB%8F%84%EB%B9%84
                       &gs_lcp=CgNpbWcQAzIECCMQJzIECCMQJzIFCAAQsQMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAO
                       gcIIxDqAhAnOgQIABADOggIABCxAxCDAVCSE1jSHWCJIGgCcAB4AYABggGIAaUEkgEDMC41mAEAoAEBqg
                       ELZ3dzLXdpei1pbWewAQrAAQE&sclient=img&ei=ys3dYMb6C8Sk1e8PqrGBwAk&bih=969&biw=1920&hl=ko"""
        self.crawlCount = crawlCount
        self.searchWord = searchWord

    def checkBrowser(self, browser):
        if browser == 1:
            try:
                driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
                return driver
            except:
                raiseErrors("driver_chrome")
        elif browser == 2:
            try:
                driver = webdriver.Edge(executable_path='./drivers/msedgedriver.exe')
                return driver
            except:
                raiseErrors("driver_edge")

    def scrollDown(self):
        last_height = self.browserDriver.execute_script("return document.body.scrollHeight")

        for i in range(5):
            self.browserDriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_SEC)
            new_height = self.browserDriver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                time.sleep(SCROLL_PAUSE_SEC)
                new_height = self.browserDriver.execute_script("return document.body.scrollHeight")

                try:
                    self.browserDriver.find_element_by_class_name("mye4qd").click()
                except:
                    if new_height == last_height:
                        break


        last_height = new_height

    def downloadImages(self):
        # Open Url from browser
        self.browserDriver.get(self.url) 

        time.sleep(SCROLL_PAUSE_SEC)                               # Wait for 2 Seconds
        self.scrollDown()                                          # Scroll Down to find enough images

        html = self.browserDriver.page_source                      # Get page HTML code
        soup = BeautifulSoup(html, 'html.parser')                  # Input HTML from selenium to BeautifulSoup
        imgs = soup.find_all('img', attrs={'class':'rg_i Q4LuWd'}) # Select img classes

        if len(imgs) > self.crawlCount:
            imgs = imgs[:self.crawlCount]

        print(f"{len(imgs)} images are searched")

        # Download searched Images
        for idx, img in tqdm(enumerate(imgs), desc=f"Download {self.searchWord}", ascii=True):
            try:
                imgUrl = img["src"]
            except:
                imgUrl = img["data-src"]
            with urlopen(imgUrl) as f:
                with open(downloadDir + self.searchWord + str(idx)+'.jpg','wb') as h:
                    img = f.read()
                    h.write(img)
                h.close()
            f.close()

        print('Image Crawling is done')
