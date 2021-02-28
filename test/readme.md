## 1. fastapi-from-blog 💯

    https://soyoung-new-challenge.tistory.com/81

1.  <code>pip install fastapi uvicorn</code>
2.  <code>create main.py</code>
3.  <code>uvicorn main:app --reload --host=0.0.0.0 --port=8000</code>

    - 파일이름이 main.py가 아니면 uvicorn이 안 됨
    - 2021.02.28에 파일명을 fastapi.py, 실행 명령어를 uvicorn fastapi.app --reload --host=0.0.0.0 --port=8000으로 시도하였으나 안 됨.
    - 해당 부분 해결을 위해 test 내 세부 directory로 추가 구분, fastapi 폴더 생성 후 python file을 main.py로 변경

4.  <code>localhost:8000에서 return값 확인</code>
5.  <code>localhost:8000/docs에서 openapi 문서 확인</code>
6.  <code>Item class를 정의하여(main.py), test.py로 확인</code>

    - post로는 405 error 발생, get으로 하면 정상적인 결과 확인 가능

<br>

## 2. pydantic-from-doc

    https://pydantic-docs.helpmanual.io

1. model tutorial
