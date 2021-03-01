# pydantic 에서 객체를 정의하는 주요 수단은 모델을 사용하는 것입니다
# (모델은 단순히에서 상속하는 클래스입니다 BaseModel).

# 모델은 엄격하게 유형이 지정된 언어의 유형과 유사하거나
# API에서 단일 엔드 포인트의 요구 사항으로 생각할 수 있습니다.

# 신뢰할 수없는 데이터는 모델에 전달할 수 있으며
# 구문 분석 및 유효성 검사 후 pydantic 은
# 결과 모델 인스턴스의 필드가 모델에 정의된 필드 유형을 준수함을 보장합니다.

# using basic model

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'Jane Doe'
    
    # name은 필수가 아님 (기본값 존재)
    # name의 기본값에서 유형이 유추됨

# user = User(id='abc')
# ValidationError 발생

user = User(id='123')
# 원래 ValidationError여야 하지만, 필드 유형에 따라 자동 캐스팅

# https://wikidocs.net/21050
# assert는 뒤의 조건이 True가 아니면 AssertError 발생
# assert 조건, '메세지' ('메세지'는 생략 가능)
# 단순히 에러를 찾는 것이 아니라, 값을 보증하기 위해 사용
# 실수를 가정해 값을 보증하는 방식 -> 방어적 프로그래밍
assert user.id == 123
# 캐스팅 된 것을 확인

assert user.name == 'Jane Doe'
# user.name을 확인

assert user.__fields_set__ == {'id'}
# 모델 인스턴스가 초기화될 때 설정된 필드 이름 세트 확인
# name은 기본값이기에 id만 확인

assert user.dict() == dict(user) == {'id' : 123, 'name': 'Jane Doe'}
# 초기 필드와 같은지 확인

user.id = 321
assert user.id == 321
# 필드 변경방법

# 모델 속성
# dict() : 모델의 필드와 값의 dictionary 반환
# json() : Json 문자열 표현을 반환
# copy() : 모델의 복사본(swallow copy) 반환
# parse_obj() : 객체가 dictionary가 아닌 경우, 오류 처리를 이용하여 모델에 객체를 로드하는 유틸리티
# parse_raw() : 다양한 형식의 문자열을 로드하기 위한 유틸리티
# parse_file() : parse_raw와 같지만 파일 경로에 대한 유틸리티
# from_orm() : 임의의 클래스에서 모델로 데이터를 로드함.
# schema() : 모델을 Json schema로 나타내는 dictionary를 반환
# schema_json : schema()의 json 문자열 표현을 반환
# construct() : 유효성 검사를 실행하지 않고 모델을 생성하는 클래스 메서드
# __fields_set__ : 모델 인스턴스가 초기화될 때 설정된 필드 이름 세트
# __fileds__ : 모델 필드의 사전
# __config__ : 모델의 구성 클래스, 참조