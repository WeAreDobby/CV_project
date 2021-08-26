# Simple Preprocessing 실행 방법
```
1. Git clone repository
git clone https://github.com/WeAreDobby/CV_project.git

2. Create new environment
conda create -n envName python=3.8 or higher version

3. install packages
pip install requirements.txt

4-A. start code (with .py)
cd Preprocessing
python main.py -dd or --data_dir './dataset/original_image'   # "Original dataset direction"
               -sd or --save_dir './dataset/resized_image'    # "To save resized dataset direction"
               -s  or --size 256                              # "resize image size (default = 256)"

4-B. start code (with .ipynb)
Open main.ipynb and fllow each discriptions
```
  ## 주의 사항
  - 이미지 확장자는 변하지 않음
  - 절대 경로, 상대 경로 모두 사용 가능
  - 이미지 사이즈 변환시 변환 비율은 1:1로 고정됨(비율 변환 X)
  ## 전처리 데이터 저장 경로
  ```
 ├─Data_dir             # take data from this folder
 └─Save_dir             # save preprocessed data in this folder
    ├─img1.jpg          # preprocessed image
    └─img2.jpg
      ...
 ```
