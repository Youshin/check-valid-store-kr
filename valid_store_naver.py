import requests
from dotenv import load_dotenv
import os


def check_if_valid_store(query_store, query_address=""):
    # 네이버 API 키 설정
    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")

    query = f"{query_store} {query_address}"
    # 지역 검색 API URL
    url = f"https://openapi.naver.com/v1/search/local.json?query={query}&display=5"

    # 헤더에 클라이언트 ID와 시크릿을 포함
    headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

    # GET 요청
    response = requests.get(url, headers=headers)

    # 결과 출력
    if response.status_code == 200:
        if not response.json()["items"]:
            print("검색 결과가 없습니다.")
            return False
        for item in response.json()["items"]:
            store_name = item["title"].replace("<b>", "").replace("</b>", "")
            store_address = item["address"].strip()
            road_address = item["roadAddress"].strip()
            if query_store == store_name and (
                query_address in store_address or query_address in road_address
            ):
                print(
                    f"가게 이름: {store_name}, 주소: {store_address} 도로명 주소: {road_address}"
                )
                return True
            else:
                print(
                    f"가게 이름: {store_name}, 주소: {store_address} 도로명 주소: {road_address}"
                )
                return False
        else:
            return False


if __name__ == "__main__":

    load_dotenv()
    flag = check_if_valid_store(
        "투썸플레이스 문정역점"  # , "서울 송파구 법원로 114 엠스테이트 B동 1층"
    )
    if flag:
        print("유효한 가게")
    else:
        print("유효하지 않은 가게")
