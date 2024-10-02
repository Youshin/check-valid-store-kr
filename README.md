# 국내 장소 유효성 체크

Naver 위치 API를 이용한 국내 장소 유효성 체크

## How to use

location.yaml 파일에 위치 정보를 추가하면 된다.

Example

```yaml
locations:
  - 장소명:
    - 주소: 주소(도로명 주소 가능)
    - 특징: 장소 설명
  - 투썸플레이스 문정역점: 
    - 주소: 서울 송파구 법원로 114
    - 특징: 초코케익 맛있음
  - 투썸플레이스 문정점: # 문정역점이 맞음
    - 주소: 서울 송파구 법원로 114
    - 특징: 초코케익 맛있음
```

Github Action을 통해 자동으로 유효성 체크가 이루어진다.

## 주의사항

네이버 API 키를 발급받아야 한다.
NAVER_CLIENT_ID=${{ secrets.NAVER_CLIENT_ID }}"
NAVER_CLIENT_SECRET=${{ secrets.NAVER_CLIENT_SECRET }}
