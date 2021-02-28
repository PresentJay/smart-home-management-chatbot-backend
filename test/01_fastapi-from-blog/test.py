# 1. 필요한 라이브러리 임포트
import requests
import json

# 2. 요청 보낼 url 주소
url = "http://127.0.0.1:8000/items/"

# 3. 같이 보낼 데이터 작성
data = {"name": "new_challenge", "description":"test1", "price":2020, "tax":2021}

# 4. post로 API서버에 요청보내기
res = requests.get(url, data=json.dumps(data))

# 5. 결과 확인하기
print(res.text)