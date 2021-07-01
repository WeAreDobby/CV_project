# Simple Crawling 실행 방법
```
1. Git clone repository
git clone https://github.com/WeAreDobby/CV_project.git

2. Create new environment
conda create -n envName python=3.8

3. install packages
pip install requirements.txt

4. install Browser Drivers
Chrome : https://chromedriver.chromium.org/downloads
Edge   : https://developer.microsoft.com/ko-kr/microsoft-edge/tools/webdriver/

5. start code
cd Crawling
python main.py --browser 1   # "1. Chrome, 2. Edge (Default == 1)"
               --count 100   # "how many images to download (Default == 100)"
```
 - [Chrome Driver Download Center](https://chromedriver.chromium.org/downloads)
 - [Edge Driver Download Center](https://developer.microsoft.com/ko-kr/microsoft-edge/tools/webdriver/)  

## 주의 사항
 - Driver 버전 확인 (본인 브라우저 버전과 일치한 버전을 설치해야 함)
   - Chrome : chrome://settings/help
   - Edge : edge://settings/help
 - Driver 설치 경로
 ```
 └─CV_project
      └─Crawling
         └─drivers               # download in this folder
             ├─chromedriver.exe  # do not change exe file's name 
             └─msedgedriver.exe  # do not change exe file's name
 ```
  - Downloaded Image 경로
    - 이미지는 .jpg 확장자로 설치됨 
  ```
 └─CV_project
      └─Crawling
         ├─drivers
         └─DownloadImgs           # download in this folder
             ├─img1.jpg           # downloaded image
             └─img2.jpg
             ...
 ```

# StyleGAN 활용방법
 - Not Yet
## [Dataset GoogleDrive](https://drive.google.com/drive/folders/1I3qlAwIZkl4v8TEYjkvNkSeR0Ozb3OEH?usp=sharing)


# 참고 자료
## Youtube
 - [얼굴을 디즈니 애니메이션으로 만들어버리는 인공지능 / 빵형의 개발도상국](https://www.youtube.com/watch?v=84EqhSY-n6c)

## Blog

## Paper
 - [Analyzing and Improving the Image Quality of StyleGAN](https://arxiv.org/pdf/1912.04958.pdf)
