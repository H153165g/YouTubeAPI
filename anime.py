import requests
import json

API_KEY = ''
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
VIDEO_URL = 'https://www.googleapis.com/youtube/v3/videos'
ANIME_URL = 'https://anime-api.deno.dev/anime/v1/master'

def transformdata(animes, year, n):
    anime = {
        "name": animes["title"],
        "shortname": [
            animes["title_short1"],
            animes["title_short2"],
            animes["title_short3"],
            animes["twitter_hash_tag"]
        ],
        "year": year,
        "n": n
    }
    return anime

def get_anime_name():
    all_anime = []  # すべてのアニメ情報を保存するリスト

    for year in range(2014, 2024):
        for n in range(1, 5):
            response = requests.get(f'{ANIME_URL}/{year}/{n}')
            if response.status_code == 200:
                anime_list = response.json()
                for anime in anime_list:
                    anime_data = transformdata(anime, year, n)
                    all_anime.append(anime_data)  # アニメ情報をリストに追加
            else:
                print(f"Failed to retrieve data for {year} Q{n}: {response.status_code}")

    # すべてのアニメ情報をファイルに書き込む
    with open('anime.json', 'w', encoding='utf-8') as f:
        json.dump(all_anime, f, ensure_ascii=False, indent=4)

def main():
    get_anime_name()

if __name__ == '__main__':
    main()
