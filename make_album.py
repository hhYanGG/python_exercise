def make_album(singer_name,album_name):
    album = {
        'singer' : singer_name,
        'album_n': album_name
    }
    return album

alb = make_album("jay chou","头文字D")
print(alb)