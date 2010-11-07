#!/usr/bin/python2.6

import os
import json
import urllib

import tornado.httpserver
import tornado.ioloop
import tornado.web


boss_http_base = "http://boss.yahooapis.com/ysearch/images/v1/"
app_id = "fOwNVoHV34FaT7MH5A6Jzl2.DTD1A2NQ6tz1i2.f1zxxxSmVkO2M1RM1267Qx80-"
social_hashtag = '#socialcollage'


class GlueHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("glue.html")


class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        query = self.get_argument("query", None)
        num = 9

        if query is None:
            # fixme: return 404 or something
            pass

        url = boss_http_base + urllib.quote('"%s"' % query) + "?appid=" + app_id
        filename, headers = urllib.urlretrieve(url)
        try:
            inp = json.load(open(filename))['ysearchresponse']['resultset_images']
        except KeyError, e:
            # didn't get valid results
            # fixme: handle this
            pass

        image_urls = [s['thumbnail_url'] for s in inp[0:num]]
        self.write(json.dumps(image_urls))


def parse_tweet(text):
    parts = text.split()
    hashtag = parts[0]
    url = parts[1]
    rest = parts[2:]

    return hashtag, url, rest


def has_our_hash(text):
    return text.split()[0] == social_hashtag


class UserHandler(tornado.web.RequestHandler):
    def get(self, username):
        # http://api.twitter.com/1/statuses/user_timeline.json?screen_name=weschow

        inp = json.load(open("user.inp"))

        images = []
        for tw in inp:
            if has_our_hash(tw['text']):
                hashtag, url, rest = parse_tweet(tw['text'])
                images.append([url, " ".join(rest)])

        self.render("user.html", username=username, images=images)


class TweetHandler(tornado.web.RequestHandler):
    def get(self):
        # http://twitter.com/home?status=@neilyourself%20%23tweetgen

        image_url = self.get_argument("image", None)
        query = self.get_argument("query", None)

        if image_url is None:
            # fixme: handle this
            pass

        if query is None:
            # fixme: handle this
            pass

        twitter_text = "%s %s %s" % (social_hashtag, image_url, query)
        twitter_url = "http://twitter.com/home?status=" + urllib.quote(twitter_text)
        self.redirect(twitter_url)


class CollageHandler(tornado.web.RequestHandler):
    def get(self):
        #inp = json.loads(open('search.inp').read())

        url = "http://search.twitter.com/search.json?q=" + urllib.quote("#socialcollage")
        filename, headers = urllib.urlretrieve(url)
        inp = json.load(open(filename))

        results = inp['results']
        tweets = []
        for tw in results:
            if has_our_hash(tw['text']):
                hashtag, url, rest = parse_tweet(tw['text'])
                tweets.append({ 'username': tw['from_user'],
                                'url': url,
                                'query': " ".join(rest) })

        self.render('collage.html', tweets=tweets)


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

application = tornado.web.Application(
    [(r"/glue", GlueHandler),
     (r"/user/([A-Za-z0-9_]+)", UserHandler),
     (r"/search", SearchHandler),
     (r"/tweet", TweetHandler),
     (r"/", CollageHandler)],
    **settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
