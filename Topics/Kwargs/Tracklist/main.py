def tracklist(**kwargs):
    for group, content in kwargs.items():
        print(group)
        for album, track in content.items():
            print('ALBUM: {} TRACK: {}'.format(album, track))
