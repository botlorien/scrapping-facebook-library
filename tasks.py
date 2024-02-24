from facebook import Facebook
import dataprocessing as dp




def get_facebook_ads():
    face = Facebook()
    face.init_browser()
    return dp.process_content_ads(face.get_facebook_ads())


if __name__ == '__main__':
    get_facebook_ads()
