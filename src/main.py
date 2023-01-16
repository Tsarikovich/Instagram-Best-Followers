import json

import pyotp
from instagrapi import Client
from src.credentials import base32secret, login, password


def get_following_likes_list(followers_likes_list: dict):
    result = followers_likes_list

    my_following_names = [
        user_short.username
        for user_short in cl.user_following(str(cl.user_id)).values()
    ]

    result = {k: v for k, v in result.items() if k in my_following_names}
    result = dict(sorted(result.items(), key=lambda item: item[1]))

    with open('../result_following.json', 'w') as fp:
        json.dump(result, fp)

    return result


def get_followers_likes_list():
    print('Getting followers list ...')
    my_followers_likes = {
        user_short.username: 0
        for user_short in cl.user_followers(str(cl.user_id)).values()
    }

    print('Collecting posts ...')
    my_posts = cl.user_medias(cl.user_id)
    for i, media in enumerate(my_posts):
        print(f'Processing media #{i}')
        post_likers = [user.username for user in cl.media_likers(media.pk)]

        for liker in post_likers:
            if liker in my_followers_likes:
                my_followers_likes[liker] += 1

    my_followers_likes = dict(
        sorted(my_followers_likes.items(), key=lambda item: item[1])
    )

    with open('../result_followers.json', 'w') as fp:
        json.dump(my_followers_likes, fp)

    return my_followers_likes


def main():
    totp = pyotp.TOTP(base32secret)

    print('Login in ..')
    cl.login(login, password, verification_code=totp.now())

    # or if without 2FA:
    # cl.login(login, password)
    print('Login done')

    followers_likes_list = get_followers_likes_list()
    following_likes_list = get_following_likes_list(followers_likes_list)


if __name__ == '__main__':
    cl = Client()
    main()
