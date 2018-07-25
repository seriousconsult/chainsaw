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

#time.sleep(28219)# hours long pause


try:
    session = InstaPy(username=insta_username, password=insta_password)
    session.login()

    #### settings
    ###______________________________________________________________________________________
    session.set_upper_follower_count(limit= 12100)
    session.set_do_comment(True, percentage=1)
    session.set_comments(['Good vibe!','Thank you for posting this!','I like your feed. Keep it up.','Nice feel to this.',' Me gusta este estilo','Good vibe in this one.', 'Nice feel, I do like it a lot!'],media='Photo')
    session.set_dont_include(['nerdywhatsits','ladybellfarms'])
    # completely ignore liking images from certain users
    session.set_ignore_users(['cathy_rudis_mccammack', 'shellyclark434', 'natalia_seliverstova_a','marshall_alpha'])

    # searches the description and owner comments for the given words and won't like the image if one of the words are in there
    session.set_dont_like(['money','trump', 'bernie','snowden','sanjay', 'hate', 'china','republican','democrat','football',
	'Ethopia','church','superbowl','christ','jesus','bible','heaven','sinner', 'repost', 'iphone','virgin', 'moscow',
	'india ','god','sale','pizza','realtor','islamic','mosque','hindi','tactical','sponsored','weed','nsfw','via:'])

    #  4 per user likes
    session.set_user_interact(amount=random.randint(1,4), randomize=True, percentage=random.randint(30,50), media='Photo')

    #for tags check out https://displaypurposes.com/
    my_hashtags = ['spiritual','spirituality','meditation','consciousness','enlightenment','universe','awakening',
	'thirdeye','loveandlight','wisdom','lightworker','energy','meditate','spirit','knowledge','namaste','healing',
	'manifest','mind','PemaChodron','impermanence','cleargram','imperfectionisperfection','vibratehigher','transend',
	'meditation','meditate','stillness','peace','seewhatisthere','transcend','movement','buddha','vipassana','empoweryourself',
	'happinessisachoice','paradigmshift','understand','dailydharma','impermanent','stopandlook','stopandsee','dawn','healthymind',
	'abide','paradigmshift','understand','dailydharma','stonestack','sonya9','nikon','sonya7riii']


    #### actions
    ###______________________________________________________________________________________

    # session.follow_user_followers not working 2018 July 24
    #session.follow_user_followers(['lionsroarbuddhism','gypsyon__','ellakociuba','jo.kurth','kumpulainentomi'], amount=3, randomize=True, interact=True, sleep_delay=random.randint(151,285))
    i = 0
    while i < 21:
        i=i+1
        print "round... " + str(i)
        number_of_followers_to_like = random.randint(3,10)
    	number_of_throwoffs_to_like = random.randint(1,5)
        throw_off_sleep = random.randint(6, 112)#seconds
        session.like_by_feed(amount=number_of_followers_to_like, randomize=True, unfollow=False, interact=False)
        session.like_by_tags([random.choice(my_hashtags)], amount=number_of_throwoffs_to_like, media='Photo')
        session.like_by_feed(amount=number_of_followers_to_like, randomize=True, unfollow=False, interact=False)
        session.like_by_tags([random.choice(my_hashtags)], amount=number_of_throwoffs_to_like, media='Photo')
        session.like_by_feed(amount=number_of_followers_to_like, randomize=True, unfollow=False, interact=False)

        print "sleeping... " + str(throw_off_sleep)
        time.sleep(throw_off_sleep)



finally:
    # end the session
    session.end()



