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

#time.sleep(8219)#2 hour pause


try:
    session = InstaPy(username=insta_username, password=insta_password)
    session.login()

    #### settings
    ###______________________________________________________________________________________
    session.set_upper_follower_count(limit= 9999100)
    session.set_do_comment(True, percentage=1)
    session.set_comments(['Good vibes!','I appreicate you posting this!','Keep it up. I like the feed.','Nice feel to it .','Me gusta este estilo.','Good vibes.  I like it.', 'Nice feel, I do like it a lot!','Please keep up the postings!'],media='Photo')
    session.set_dont_include(['nerdywhatsits','ladybellfarms'])
    # completely ignore liking images from certain users
    session.set_ignore_users(['cathy_rudis_mccammack', 'shellyclark434', 'natalia_seliverstova_a', 	'gustaevirgin_hair','canteeqwardrobe','hajarjahanam.official','droneactionnation','vdorotheaswanepoelbiles','marshall_alpha'])

    # searches the description and owner comments for the given words and won't like the image if one of the words are in there
    session.set_dont_like(['trump', 'bernie','Delhi','snowden','sanjay', 'hate', 'china','republican','democrat','football',
	'Ethopia','church','superbowl','christ','jesus','bible','heaven','sinner', 'repost', 'iphone','virgin',
	'india','god','sale','pizza','realtor','islamic','mosque','hindi','tactical','sponsored','weed','nsfw','via:','elephants','virgin '])

    #  3 per user likes
    session.set_user_interact(amount=random.randint(1,3), randomize=True, percentage=random.randint(30,50), media='Photo')

    #for tags check out https://displaypurposes.com/
    my_hashtags = ['spiritual','spirituality','meditation','consciousness','enlightenment','universe','awakening',
	'thirdeye','loveandlight','wisdom','lightworker','energy','meditate','spirit','knowledge','namaste','healing',
	'manifest','mind','PemaChodron','impermanence','cleargram','imperfectionisperfection','vibratehigher','transend',
	'meditation','meditate','stillness','peace','seewhatisthere','transcend','movement','buddha','vipassana','empoweryourself',
	'happinessisachoice','paradigmshift','understand','dailydharma','impermanent','stopandlook','stopandsee','dawn','healthymind',
	'abide','paradigmshift','understand','dailydharma','stonestack','sonya9','nikon','sonya7riii']


    #### actions
    ###______________________________________________________________________________________


    # This is used to perform likes on your own feeds
    # amount=100  specifies how many total likes you want to perform
    # randomize=True randomly skips posts to be liked on your feed
    # unfollow=True unfollows the author of a post which was considered
    # inappropriate interact=True visits the author's profile page of a
    # certain post and likes a given number of his pictures, then returns to feed
    #session.follow_user_followers(['lionsroarbuddhism','gypsyon__','ellakociuba','jo.kurth','kumpulainentomi'], amount=3, randomize=True, interact=True, sleep_delay=random.randint(151,285))
    i = 0
    while i < 20:
        i=i+1
        print "round... " + str(i)
        number_of_followers_to_like = random.randint(4,7)
    	number_of_throwoffs_to_like = random.randint(1,4)
        throw_off_sleep = random.randint(8, 11)#seconds
        session.like_by_feed(amount=number_of_followers_to_like, randomize=False, unfollow=False, interact=False)
        session.like_by_tags([random.choice(my_hashtags)], amount=number_of_throwoffs_to_like, media='Photo')
        session.like_by_feed(amount=number_of_followers_to_like, randomize=False, unfollow=False, interact=False)
        session.like_by_tags([random.choice(my_hashtags)], amount=number_of_throwoffs_to_like, media='Photo')
        session.like_by_feed(amount=number_of_followers_to_like, randomize=False, unfollow=False, interact=False)

        print "sleeping... " + str(throw_off_sleep)
        time.sleep(throw_off_sleep)



finally:
    # end the session
    session.end()



