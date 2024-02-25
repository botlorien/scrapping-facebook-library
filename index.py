import datetime

from flask import Flask, jsonify
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)


class Facebook:

    def __init__(self):
        self.base_url = 'https://www.facebook.com/ads/library/?active_status=all&ad_type=political_and_issue_ads&country=BR&q=marketing%20digital&publisher_platforms[0]=facebook&regions[0]=Mato%20Grosso&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all&content_languages[0]=pt'

    def init_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get(self.base_url)
        time.sleep(5)

    def get_cards_ads(self):
        script = """
        var cards = document.querySelectorAll('div.x1cy8zhl.x78zum5.xyamay9.x1pi30zi.x18d9i69.x1swvt13.x1n2onr6')
        let list_cards = []
        cards.forEach(item=>{
            list_cards.push(item.innerText)
        })
        console.log(list_cards)
        return list_cards
        """
        return self.driver.execute_script(script)

    def get_facebook_ads(self):
        cards_content = self.get_cards_ads()
        print(cards_content)
        self.driver.quit()
        return cards_content


def process_content_ads(content):
    cards = {}
    for i, card in enumerate(content):
        card_col = {}
        columns = [col for col in card.split('\n') if len(col.strip()) > 0 and col not in ('\u200b')]
        for j, col in enumerate(columns):
            card_col[f'col_{j + 1}'] = col
        cards[f'card_{i + 1}'] = card_col

    print(cards)
    return cards


def get_facebook_ads():
    face = Facebook()
    face.init_browser()
    return process_content_ads(face.get_facebook_ads())


# Define a route for the API
@app.route('/', methods=['GET'])
def hello():
    # Return a simple JSON response
    return jsonify({'message': [get_facebook_ads()]})
@app.route('/msg', methods=['GET'])
def hello2():
    # Return a simple JSON response
    return jsonify({'message': [{'data':str(datetime.datetime.now())}]})
@app.route('/msg2', methods=['GET'])
def hello3():
    # Return a simple JSON response
    return jsonify({'message': 'Hello world'})

if __name__ == '__main__':
    app.run(debug=True, port=10000)
