# python_poc

python

## 컴파일 언어, 인터 프리터 언어

- 컴파일언어: 0, 1만 파악, C언어, 번역 한 다음 함, 빠름
- 인터프린터 언어: 간단히 적을 수 있음, Python, 한줄씩, 느림

### 파이썬

- 개발속도가 빠르다.
- 파이썬 할수 있는것
  > 시스템 유틸리티, GUI 프로그램, C/C++과의 결합, 웹프로그래밍[장고, 플라스트], 수치연산 프로그래밍, 데이터베이스 프로그래밍[판다스], 인공지능  
  > 클로버, 누구 등
- 파이썬 할 수 없는것
  > 시스템 앱(window, linux), 모바일 프로그래밍
- 파이썬 설치하기
  > Add Path 포함하여 설치
  > print("hello")로 설치 여부 확인
- IDLE: 메모장 + 파이썬에서 사용 / IDE: 메모장
- pycharm 또는 vscode 사용
- 실행: 파이썬 위에 > 로 실행 또는 터미널에서 `python hello.py` 로 실행

## 크롤링 만들기

> ide에서 사용(ptyone 설치)  
> Beautiful Soup 검색  
> pip install bs4
> 코딩(네이버 실시간 검색어 가져오기)
> pip install google_images_download

## 셀레니움으로 크롤링 하기

1. 가상 환경 늘어 가기: venv 이용

- https://docs.python.org/ko/3/library/venv.html

```py
python -m venv selenium
cd selenium/Scripts # 이동
activate # 가상환경 실행

# F:\DEV_APP\python_poc\selenium\Scripts\Activate.ps1 파일을 CN=Python Software Foundation, O=Python
# Software Foundation, L=Wolfeboro, S=New Hampshire, C=US이(가) 게시했지만 시스템에서 신뢰할 수
# 없습니다. 신뢰된 게시자가 서명한 스크립트만 실행하십시오.
# [V] 실행한 적 없음(V)  [D] 실행 안 함(D)  [R] 한 번 실행(R)  [A] 항상 실행(A)  [?] 도움말
# (기본값은 "D"):A
(selenium) ../selenium/Scripts>
```

2. 셀레늄, chromedriver 설치

- (selenium) 가상 환경 내에서 설치
  `pip install selenium`

- chromedriver를 내 브라우저의 버전 값 확인 후 다운로드 함

  > ex)chromedriver_win32.zip

- selenium 가상 환경 폴더 내로 옮김

- 동일 경로 내에 google.py[googleImg.py 로 지정함]라는 파이선 함수 만들어야 함

3. 구글 이미지 크롤링 코드 작성

- `python selenium example` 검색
