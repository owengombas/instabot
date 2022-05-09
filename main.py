from crawler.Crawler import Crawler
import pandas as pd

if __name__ == '__main__':
    c = Crawler(
        username="quizzical.bhabha",
        enc_password="#PWD_INSTAGRAM_BROWSER:10:1652123837:AepQAPTDEnFlJ7jJzRCO/JRjEHprSs0bt0yv+UO3jdSmkdRs7v8KU2XcbYIYwcedClPpLt8BX8F2/WzwZ6tfFsHV8ZyTZOioQYlryCqbLG2B7/LHLq6yPjt4mBjFpxYYfDP7nrJoqMCfg5T1/DPLkEfYtTE=",
        x_instagram_ajax="a1c047c8ac09"
    )

    c.login(False)

    followings = c.get_all_following("venfoo")

    pd.DataFrame.from_dict(followings)

    # c.post_image(
    #     '/Users/owen/Pictures/test2.jpg',
    #     'voilà'
    # )

    #faces_gan.faces_gan.create_model("/Users/owen/Downloads/img_align_celeba")
    #faces_gan.faces_gan.generate_faces(100, faces_dir='faces')
