'''
✨ jupyter 명령어 ✨
🔍 명령 프롬포트에서 실행하는 코드를 실행시킴
!
ex) !pip install ... : 프롬포트에서 ...를 인스톨 하도록!

🔍 현재 디렉토리 경로 출력 / 파일을 읽고 쓸때 꼭 확인!
%pwd

🔍 현재 디렉토리의 파일 목록 표시
%ls

🔍 디렉토리 생성
%mkdir

🔍 jupyter에서 데이터프레임을 시각화하는 함수
display(데이터프레임변수명)

✨ 참고 사이트 ✨
🔍 Pillow 관련
https://playground.naragara.com/%ed%8c%8c%ec%9d%b4%ec%8d%ac-%ec%9d%b4%eb%af%b8%ec%a7%80-%ec%b2%98%eb%a6%ac-pillowpil-%ec%84%a4%ec%b9%98-%eb%b0%8f-%ec%82%ac%ec%9a%a9-%ec%98%88%ec%a0%9c-%ec%b4%9d%ec%a0%95%eb%a6%ac/

🔍 파이썬 변수 시각화
https://pythontutor.com/visualize.html#mode=edit

🔍 초보자를 위한 파이썬 300제
https://wikidocs.net/book/922
'''

# ✨ 라이브러리 ✨
# os 모듈 - 파일 생성 및 삭제 기타등등
import os
# numpy 모듈 - 다차원 배열, 행렬 연산 등등
import numpy as np
# glob 모듈 - 파일의 리스트를 뽑을때 사용 / glob 모듈
from glob import glob
# Image 모듈 - 이미지 분석 및 처리 / Pillow 모듈
from PIL import Image
from PIL import ImageFilter
# pandas - 데이터 전처리
import pandas as pd
# plt 모듈 - 그래프그리기 / matplotlib 모듈
import matplotlib.pyplot as plt
# shutil 모듈 -파일과 폴더를 이동하거나 복사하는 용도
import shutil
# re 모듈 - 정규표현식(문자열의 일정한 패턴을 표현하는 일종의 형식 언어)관련
import re
# qrcode 모듈 - QR코드생성
import qrcode
# time,datetime 모듈 - 날짜 시간관련
import time
import datetime