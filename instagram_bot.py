from instapy import InstaPy
from instapy.util import smart_run

insta_username = ""
insta_password = ""

dont_like = ["food", "girl"]
ignore_words = ["pizza"]
friend_list = ["friend1", "friend2", "friend3"]
hashtags = ["#photography", "#naturephotography", "#alexasxt", "#excellent_minimal", "#cinematographylife",
            "#ihaveathingforminimal", "#notgreyskies", "#lensculturestreets", "#imaginarymagnitude",
            "#streetphotographyinternational", "#capturestreets", "#worldtravelscapes", "#iphonography",
            "#lensculture", "#earthofficial", "#everybodyfilm", "#sonyalphain"]

bot = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
with smart_run(bot):
    bot.set_relationship_bounds(
        enabled=True,
        potency_ratio=-1.21,
        delimit_by_numbers=True,
        max_followers=4590,
        max_following=5555,
        min_followers=45,
        min_following=77,
    )
    bot.set_do_comment(True, percentage=10)
    # bot.set_comments(["Cool!", "Awesome!", "Nice!"])
    bot.set_dont_include(friend_list)
    bot.set_dont_like(dont_like)
    bot.set_do_follow(True, percentage=50)
    bot.set_ignore_if_contains(ignore_words)
    bot.like_by_tags(hashtags, amount=100)
    bot.end()
