import requests
from bs4 import BeautifulSoup

def scrape():
    base_url = "https://www.j-archive.com/"
    urls = [base_url + "showgame.php?game_id=" + i for i in range(1, 9468)]
    #if page contains body, div-content, p class error OR no jeopardy round
    # if game_title has 'Celebrity Jeopardy' then triple round
    response = requests.get(base_url)
    print(response.text)
    #

if __name__ == '__main__':
    scrape()