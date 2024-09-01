# 경희대학교 공과대학 열람실 예약시스템 개선

**빈번히 일어나는 열람실 사석화와 미반납 문제를 해결하고자 시작하게 된 연구입니다.**

YOLOv5 모델을 이용해 짐과 사람, 의자를 감지하고, django와 react를 기반으로 구현한 예약시스템에서 사석화와 미반납 행위가 실시간 카메라로 감지될 시 자동으로 퇴실처리되는 시스템입니다.

## Contributed Members

| Name         | Department                                   | Git                        | Role                        |
| :--------------- | :--------------------------------------------: | :------------------------------: | :------------------------------: |
| 서정민    | Industrial Management Engineering & Software Convergence                    | https://github.com/jeongmin1217     | 팀장, BE, FE, Data Analysis |
| 권기현  | Industrial Management Engineering & Computer Science                    | https://github.com/kkh0331     | BE, FE, Data Analysis |

## Main Functions

- 일반적인 예약시스템의 CRUD 구현 (예약, 반납)
- 예약된 상태에서 짐은 자리에 있지만 사람이 없는 경우가 지속되는 경우 반납 처리 (사석화 문제 처리)
- 예약된 상태에서 짐도, 사람도 없는 경우가 지속되는 경우 반납 처리 (미반납 행위 처리)
  
**네트워크 포트포워딩을 통해 송출한 실시간 IP카메라의 영상을 서버에서 프레임 단위로 받아 자체 구축한 YOLOv5 모델로 분석 후 결과값을 DB에 쌓아 상황에 따라 알맞은 처리를 진행합니다.**

## Overview

<img src="https://github.com/LibraryDetection/.github/assets/79658037/98132ca8-024e-4dd5-b9c7-b962e102b814" style="width:30rem; height:auto;"></img>

1. 영상 하단에 실시간 IP 카메라 주소를 입력하여 열람실 카메라 실시간 송출
2. 9번 좌석 : 사석화 자리에 대해 일정 시간 지난 후, 자동으로 좌석 반납 처리
3. 10번 좌석 : 잠시 자리를 비운 경우는 사석화와 달리 좌석 반납 처리가 되지 않음
4. 3번 좌석 : 자리를 떠났지만 시스템 상 반납을 깜박한 경우, 일정 시간 지난 후 자동으로 좌석 반납 처리

## Project Architecture

<img src="https://github.com/LibraryDetection/.github/assets/79658037/e751cdd9-2e55-4651-8c4d-d7c2277488e1" align="center" style="width:50rem; height:auto;"></img>

## Awards
- 경희대학교 2023학년도 1학기 캡스톤디자인 경진대회 우수상 (경희대학교 LINC 사업단)
- 2023년 도시형소공인 집적지구 캡스톤 경진대회 장려상 (용인시산업진흥원)

## Back-end of the library reservation system

front-end에서 back-end로 이미지 전송 후 back-end에서 custom yolov5 모델 돌려서 결과 추출

yolov5을 django에서 사용하기 위해서

1. (terminal)'pip install yolov5'을 설치

2. views.py에서 import yolov5을 한 후

3. model = yolov5(custom model pt파일이 있는 경로 설정)한 후 사용
