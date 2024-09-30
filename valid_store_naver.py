import requests
from dotenv import load_dotenv
import os
import sys


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
            print(
                f"검색 결과가 없습니다: \n\t가게명 {query_store} \n\t주소 {query_address}"
            )
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
    if len(sys.argv) < 2:
        print("사용법: python valid_store_naver.py <가게이름> [주소]")
        sys.exit(1)

    store_name = sys.argv[1]
    store_address = sys.argv[2] if len(sys.argv) > 2 else ""

    flag = check_if_valid_store(store_name, store_address)
    if flag:
        print("유효한 가게")
        sys.exit(0)
    else:
        print("유효하지 않은 가게")
        sys.exit(1)
