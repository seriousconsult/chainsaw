from instapy import InstaPy
import time
import random
import os






# to execute:  chin@ chin-z:~/InstaPy$ python quickstart.py

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
    session.set_upper_follower_count(limit=50015 +random.randint(1,25))
    session.set_do_comment(True, percentage=1)
    session.set_comments(['Cool', 'Nice', 'Good vibe', 'Magnifica','thank you for posting.','Me Gusta','Nice!','Good vibes'],media='Photo')
    session.set_dont_include(['nerdywhatsits','ladybellfarms'])
    # completely ignore liking images from certain users
    session.set_ignore_users(['cathy_rudis_mccammack', 'shellyclark434', 'natalia_seliverstova_a', 'droneactionnation','vdorotheaswanepoelbiles'])

    # searches the description and owner comments for the given words and won't like the image if one of the words are in there
    session.set_dont_like(['trump', 'bernie','hate', 'republican','democrat','football','church','superbowl','christ','jesus','bible','heaven','sinner','sale','realtor','buyer','black panther','anish','islamic','sponsored','weed','nsfw'])

    #  3 per user likes
    session.set_user_interact(amount=random.randint(1,3), randomize=True, percentage=random.randint(30,50), media='Photo')


    #for tags check out https://displaypurposes.com/
    my_hashtags = ['spiritual','spirituality','meditation','consciousness','enlightenment','universe','awakening','thirdeye','loveandlight','wisdom','lightworker','energy','meditate','spirit','knowledge','namaste','chakras','peace','healing','manifest','mind','PemaChodron','impermanence','impermanentart','cleargram','imperfectionisperfection','vibratehigher','transend','meditation','meditate','stillness','peace','seewhatisthere','transcend','movement','buddha','vipassana','happinessisachoice','paradigmshift','understand','dailydharma','impermanent','stopandlook','stopandsee','dawn','abide','paradigmshift','understand','dailydharma','impermanent','sonya7riii']


    #### actions
    ###______________________________________________________________________________________


    # This is used to perform likes on a specific user's feed.
    # pick a maximum how many to like, should not exceed 30, as I think this will flag as a bot.
    # session.like_by_users(usernames=['annnnnsb'], amount=12, randomize=True, media='Photo')
    # or session.like_by_users(usernames=['amandagormn','albougain','rosa.lopezzapata','stories_without_words'], amount=...

    session.like_by_users(usernames=['msjessicaleigh','broadysbarstool','sreateorg'], amount=random.randint(10,13), randomize=True, media='Photo')


finally:
    # end the session
    session.end()



