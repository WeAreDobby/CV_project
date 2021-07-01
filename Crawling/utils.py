import os

def raiseErrors(errorCode):
    if errorCode == "driver_chrome":
        raise Exception("Please Check your Chrome Driver or download driver again \n           Download Link : https://chromedriver.chromium.org/downloads")
    elif errorCode == "driver_edge":
        raise Exception("Please Check your Edge Driver or download driver again \n           Download Link : https://developer.microsoft.com/ko-kr/microsoft-edge/tools/webdriver/")

def createFolder(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
            print('created '+dir)

        return 1
    except OSError:
        print('Error : already Created' + dir)
        return -1

def getSearchWord():
    return input('검색어를 입력하세요 : ')