# 재귀 모델
# 모델 자체를 annotation의 유형으로 사용하여 더 복잡한 계층적 데이터 구조 정의

from typing import List
from pydantic import BaseModel

# typing 모듈 : python 3.5부터 type hint를 지원하기 위한 모듈로 기본 제공

class Foo(BaseModel):
    count: int
    size: float = None
    
class Bar(BaseModel):
    apple = 'x'
    banana = 'y'
    
class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]
    

m = Spam(foo={'count':4}, bars=[{'apple' : 'x1'}, {'apple' : 'x2'}])
print(m)
#> foo=Foo(count=4, size=None) bars=[Bar(apple='x1', banana='y'),
#> Bar(apple='x2', banana='y')]

print(m.dict())
"""
{
    'foo': {'count': 4, 'size': None},
    'bars': [
        {'apple': 'x1', 'banana': 'y'},
        {'apple': 'x2', 'banana': 'y'},
    ],
}
"""