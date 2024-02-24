import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Facebook:

    def __init__(self):
        self.base_url = 'https://www.facebook.com/ads/library/?active_status=all&ad_type=political_and_issue_ads&country=BR&q=marketing%20digital&publisher_platforms[0]=facebook&regions[0]=Mato%20Grosso&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all&content_languages[0]=pt'

    def init_browser(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.base_url)
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
        self.driver.get(self.base_url)
        time.sleep(5)
        cards_content = self.get_cards_ads()
        print(cards_content)
        return cards_content


if __name__ == '__main__':
    face = Facebook()
    face.init_browser()
    face.get_facebook_ads()
    input()
