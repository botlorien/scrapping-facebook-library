from facebook import Facebook
import dataprocessing as dp

face = Facebook()
face.init_browser()


def get_facebook_ads():
    return dp.process_content_ads(face.get_facebook_ads())


if __name__ == '__main__':
    get_facebook_ads()
