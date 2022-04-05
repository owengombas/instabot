from crawler.Crawler import Crawler

if __name__ == '__main__':
    c = Crawler(
        username="combienrepete",
        enc_password="#PWD_INSTAGRAM_BROWSER:10:1649178231:AYBQAHi9afhohrW9NZhF85L2SJfYbFHZnNufa3ink7wqaoRV5hULFeyBmC6gMCEII4AGGBSZM1j4diKh3g0NeKzRBOcmziOT72o7vj3D9/6GN20PDPaCBsd1YjvSvf4T/nq8AO3Ih90e0oh3DDB2zPw="
    )

    c.login()

    c.post_image(
        '/Users/owen/Pictures/test2.jpg',
        'voilà'
    )
