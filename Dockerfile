#./Dockerfile
FROM python:3
ENV PYTHONUNBUFFERED 1
#기반이 될 이미지

# 작업디렉토리(default)설정
WORKDIR /usr/src/app 

#현재 패키지 설치 정보를 도커 이미지에 복사
COPY requirements.txt ./ 
#설치정보를 읽어 들여서 패키지를 설치
RUN pip install -r requirements.txt

## Copy all src files
COPY . . 