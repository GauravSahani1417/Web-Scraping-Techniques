from facebook_scraper import get_posts

for post in get_posts('sushen.b.suryavanshi', pages=10):
    print(post['text'][:250])
