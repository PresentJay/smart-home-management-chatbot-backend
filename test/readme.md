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

## 2. pydantic-from-doc 😋

    https://pydantic-docs.helpmanual.io

1. model tutorial
2. recursive-model
3. orm instance

<br>

## 3. fastapi-from-doc 😋

    https://fastapi.tiangolo.com/ko/tutorial/

1. basic creation
2. put endpoint
3. enumeration
4. path parameters
5. query parameter type conversion
6. multiple query parameters & paths
7. required query parameter
8. basic model
9. request body + path parameters + query parameters

<br>

## 4. heroku - github auto deployment 💯

    https://test-fastapi-service.herokuapp.com/

- must have Procfile in root directory of branch.
- uvicorn must be version lower than 0.12.0 (because of uvloop dependancy error)
- uvloop need to python version upper than 3.7, and basic heroku python version is 3.6.0. so we need to indicate the version. (runtime.txt)
  <br>
  check this url > https://devcenter.heroku.com/articles/python-runtimes/
