import argparse

from crawling import Crawling

from utils import getSearchWord
from utils import createFolder

downloadDir = './DownloadImgs/'
SCROLL_PAUSE_SEC = 2

def main(args):
    browser = args.browser
    crawlCount = args.count

    # make Folder to download images
    if createFolder(downloadDir): 
        while True:
            searchWord = getSearchWord()

            if searchWord == "stop":
                break
            else:
                crawlModel = Crawling(browser, crawlCount, searchWord)
                crawlModel.downloadImages()
                crawlModel.browserDriver.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawling")

    parser.add_argument('--browser', '-b', type=int ,default=1, help="Choose your browser \n1. Chrome\n2. Edge\n input number plz not a name")
    parser.add_argument('--count', '-c', type=int ,default=100, help="please fill the count to crawl images")
    
    args = parser.parse_args()

    main(args)