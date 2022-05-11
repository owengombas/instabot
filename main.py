from crawler.Crawler import Crawler
import pandas as pd

if __name__ == '__main__':
    instagram_0x6f77656e = Crawler(
        username="0x6f77656e",
        enc_password="#PWD_INSTAGRAM_BROWSER:10:1652197635:AepQAFxKBab+AXJAqgQQ5vl20WOxcF4pJUQaTfzD+52yr/wFTl0ljrkQmz3GlQ+iJxSnE5uocQWEneRj5Vg35sD2NnHF7Nfa+fc/pvyCrzFgKTNnKUt4QggoCmrZgvW3LtR1+aLsQBGyXWUj0smYzuCDQAs="
    )

    instagram_0x6f77656e.login(False)

    followings = instagram_0x6f77656e.get_all_followers("0x6f77656e")

    pd.DataFrame.from_dict(followings)

    # c.post_image(
    #     '/Users/owen/Pictures/test2.jpg',
    #     'voilà'
    # )

    #faces_gan.faces_gan.create_model("/Users/owen/Downloads/img_align_celeba")
    #faces_gan.faces_gan.generate_faces(100, faces_dir='faces')
