import asyncio
from pyppeteer import launch
from dotenv import load_dotenv

load_dotenv()


class Facebook:

    def __init__(self):
        self.base_url = 'https://www.facebook.com/ads/library/?active_status=all&ad_type=political_and_issue_ads&country=BR&q=marketing%20digital&publisher_platforms[0]=facebook&regions[0]=Mato%20Grosso&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all&content_languages[0]=pt'

    async def init_browser(self):
        self.browser = await launch(headless=False, args=['--no-sandbox', '--disable-dev-shm-usage'])
        self.page = await self.browser.newPage()
        await self.page.goto(self.base_url)
        await asyncio.sleep(5)  # Wait for 5 seconds

    # def init_browser(self):
    #     asyncio.get_event_loop().run_until_complete(self._init_browser())

    async def get_cards_ads(self):
        script = """()=>{
        let cards = document.querySelectorAll('div.x1cy8zhl.x78zum5.xyamay9.x1pi30zi.x18d9i69.x1swvt13.x1n2onr6');
        let list_cards = [];
        cards.forEach(item => {
            list_cards.push(item.innerText);
        });
        return list_cards;}
        """
        return await self.page.evaluate(script)

    async def _get_facebook_ads(self):
        cards_content = await self.get_cards_ads()
        print(cards_content)
        return cards_content

    async def close(self):
        await self.browser.close()

    async def get_facebook_ads(self):
        ads_content = await self._get_facebook_ads()
        await self.close()
        return ads_content  # Return the ads content

    def main(self):
        return asyncio.get_event_loop().run_until_complete(self.get_facebook_ads())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(get_facebook_ads())

# import os.path
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
#
#
# class Facebook:
#
#     def __init__(self):
#         self.base_url = 'https://www.facebook.com/ads/library/?active_status=all&ad_type=political_and_issue_ads&country=BR&q=marketing%20digital&publisher_platforms[0]=facebook&regions[0]=Mato%20Grosso&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all&content_languages[0]=pt'
#
#     def init_browser(self):
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#         self.driver.get(self.base_url)
#         time.sleep(5)
#
#     def get_cards_ads(self):
#         script = """
#         var cards = document.querySelectorAll('div.x1cy8zhl.x78zum5.xyamay9.x1pi30zi.x18d9i69.x1swvt13.x1n2onr6')
#         let list_cards = []
#         cards.forEach(item=>{
#             list_cards.push(item.innerText)
#         })
#         console.log(list_cards)
#         return list_cards
#         """
#         return self.driver.execute_script(script)
#
#     def get_facebook_ads(self):
#         cards_content = self.get_cards_ads()
#         print(cards_content)
#         return cards_content
#
#
# if __name__ == '__main__':
#     face = Facebook()
#     face.init_browser()
#     face.get_facebook_ads()
#     input()
