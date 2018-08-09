import os
import random
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_secret = os.environ["YOYO"]
print(insta_secret)

insta_secret = insta_secret.split(',')

insta_username = insta_secret[0]
insta_password = insta_secret[1]

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

try:
    session.login()

    # settings
    session.set_relationship_bounds(enabled=True,
				 potency_ratio=-0.0,
				  delimit_by_numbers=True,
				   max_followers=999590,
				    max_following=999955,
				     min_followers=4,
				      min_following=4)
    session.set_do_comment(True, percentage=1)
    session.set_comments(['Good vibe!','Thank you for posting this!','I like your feed. Keep it up.','Nice feel to this.',' Me gusta este estilo','Good vibe in this one.','Nice feel, I do like it a lot!'],media='Photo')

    session.set_dont_include(['nerdywhatsits','ladybellfarms'])

    session.set_dont_like(['money','trump', 'bernie','snowden','sanjay', 'hate', 'china','republican','democrat','football',
	'Ethopia','church','superbowl','christ','jesus','bible','heaven','sinner', 'repost', 'iphone','virgin', 'moscow',
	'india ','god','sale','pizza','realtor','islamic','mosque','hindi','tactical','sponsored','weed','nsfw','via:'])


    # actions=======================================

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

    session.follow_user_followers(['lionsroarbuddhism','gypsyon__','ellakociuba','jo.kurth','kumpulainentomi'], amount=2, randomize=True, interact=True, sleep_delay=random.randint(19,185))
    i = 0
    while i < 10:
        i=i+1
        print "round... " + str(i)
        number_of_followers_to_like = random.randint(5,10)
    	number_of_throwoffs_to_like = random.randint(1,3)
        throw_off_sleep = random.randint(6, 112)#seconds
        session.like_by_feed(amount=number_of_followers_to_like, randomize=True, unfollow=False, interact=False)
        session.like_by_tags([random.choice(my_hashtags)], amount=number_of_throwoffs_to_like, media='Photo')
        session.like_by_feed(amount=number_of_followers_to_like, randomize=True, unfollow=False, interact=False)
        session.like_by_tags([random.choice(my_hashtags)], amount=number_of_throwoffs_to_like, media='Photo')
        session.like_by_feed(amount=number_of_followers_to_like, randomize=True, unfollow=False, interact=False)

        print "sleeping... " + str(throw_off_sleep)
        time.sleep(throw_off_sleep)










except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()

