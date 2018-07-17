from instapy import InstaPy
import time
import random
import os





# to execute:  chin@ chin-z:~/InstaPy$ python like_username.py


insta_secret = os.environ["YOYO"]
print(insta_secret)

insta_secret = insta_secret.split(',')

insta_username = insta_secret[0]
insta_password = insta_secret[1]


try:
    session = InstaPy(username=insta_username, password=insta_password)
    session.login()

    #### settings
    ###______________________________________________________________________________________
    session.set_upper_follower_count(limit=999999999)
    session.set_do_comment(True, percentage=1)
    session.set_comments(['Cool pic, keep them coming.', 'Nice feel to it.', 'Me gusta tu feed.', 'Good vibe in this one','thank you for posting.','Me gusta este estilo.','I like your feed.','Good vibes in this one.'],media='Photo')
    session.set_dont_include(['nerdywhatsits','ladybellfarms'])
    # completely ignore liking images from certain users
    session.set_ignore_users(['cathy_rudis_mccammack', 'shellyclark434', 'natalia_seliverstova_a', 'droneactionnation','vdorotheaswanepoelbiles'])

    # searches the description and owner comments for the given words and won't like the image if one of the words are in there
    session.set_dont_like(['trump', 'bernie','hate', 'republican','Delhi','democrat','football','church','superbowl','christ','jesus','bible','heaven','sinner','sale','realtor','buyer','black panther','anish','islamic','sponsored','weed','nsfw'])

    #  3 per user likes
    session.set_user_interact(amount=random.randint(1,3), randomize=True, percentage=random.randint(30,50), media='Photo')


    #for tags check out https://displaypurposes.com/
    my_hashtags = ['spiritual','spirituality','meditation','consciousness','enlightenment','universe','awakening','thirdeye','loveandlight','wisdom','lightworker','energy','meditate','spirit','knowledge','namaste','chakras','peace','healing','manifest','mind','PemaChodron','impermanence','impermanentart','cleargram','imperfectionisperfection','vibratehigher','transend','meditation','meditate','stillness','peace','seewhatisthere','transcend','movement','buddha','vipassana','happinessisachoice','paradigmshift','understand','dailydharma','impermanent','stopandlook','stopandsee','dawn','abide','paradigmshift','understand','dailydharma','impermanent','sonya9','nikon','sonya7riii']


    #### actions
    ###______________________________________________________________________________________


    #jamais_tres_loin

    # follows the followers of a given user
    # The usernames can be either a list or a string
    # The amount is for each account, in this case 30 users will be followed
    # If random is false it will pick in a top-down fashion
    # default sleep_delay=600 (10min) for every 10 user following, in this case sleep for 60 seconds
    session.follow_user_followers(['jamais_tres_loin'], amount=5, randomize=True, interact=True, sleep_delay=random.randint(51,235))
    # For 61% of the 30 newly followed, move to their profile
    # and randomly choose 5 pictures to be liked.

finally:
    # end the session
    session.end()
