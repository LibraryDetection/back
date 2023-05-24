# Back-end of the library reservation system

front-end에서 back-end로 이미지 전송 후 back-end에서 custom yolov5 모델 돌려서 결과 추출

yolov5을 django에서 사용하기 위해서

1. (terminal)'pip install yolov5'을 설치

2. views.py에서 import yolov5을 한 후

3. model = yolov5(custom model pt파일이 있는 경로 설정)한 후 사용
