# Mediscri BackendRESTApi

[![Build Status](https://travis-ci.org/mhoonjeon/mediscri.svg?branch=master)](https://travis-ci.org/mhoonjeon/mediscri)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

 소프트웨어 마에스트로 9기 mediscri팀의 백엔드 서버입니다.

# 사전 설치

- [Docker](https://docs.docker.com/docker-for-mac/install/) 를 설치해주시고, 도커 머신를 띄워주셔야 합니다. (상단의 도커 아이콘을 클릭했을 때 Docker is running!을 확인해주세요.)

# 로컬 환경에서 확인하기

Github에서 메디스크리 백엔드 서버 레포지토리를 클론합니다.

```shell
~$ git clone https://github.com/Mediscri/BackendRESTApi.git
```

BackendRESTApi 디렉토리로 이동합니다.

```shell
~$ cd BackendRESTApi
```

도커를 사용해, 미리 설정된 docker containers 이미지를 빌드합니다.

```bash
~$ docker-compose build
```

도커를 이용해서 django와 django rest framework을 사용한 server를 로컬 환경에 띄웁니다.

```bash
~$ docker-compose up -d
```

크롬을 열고 작동여부를 확인합니다. Django Rest Framework 화면이 뜨면 잘 작동되는 것입니다.

```http
http://localhost:8000/api/v1/
```

이제 클라이언트 앱을 띄울 차례입니다. [메디스크리 클라이언트 앱의 README](https://github.com/Mediscri/ClientDoctor)를 참고해주세요.