from time import sleep
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url,str(e)))
        return None

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    print(e)

#http://www.brawlhalla.com/rankings/1v1/

#Create file to write data to
file = open("output.txt",'w')

#keep track of page number: Last page 5233
last_page_number = 5300 #use as estimate for percentage
page_number = 0

while True:
    raw_html = simple_get('http://www.brawlhalla.com/rankings/1v1/' + str(page_number))

    #raw_html of non ranked page should be 2691, Create small buffer in just in case
    if ( len(raw_html) < 5000):

        print("End of Scrape")
        print(raw_html)
        print(page_number)
        break

    html = BeautifulSoup(raw_html, 'html.parser')

#Separate common tags to get data for each player
    odd_players = html.find_all('tr', class_='odd')
    even_players = html.find_all('tr', class_='odd')

#Find current rank from list of specific players data
    for player in odd_players:
        player_data = player.find_all('td', class_='pcenter')

        if player_data:
            file.write(player_data[3].text + '\n')

    for player in even_players:
        player_data = player.find_all('td', class_='pcenter')

        if player_data:
            file.write(player_data[3].text + '\n')

    #Next page number
    print(str(round(page_number / last_page_number,4) * 100) + "%")
    page_number += 1

    sleep(0.2)

file.close()