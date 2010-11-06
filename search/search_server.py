#!/usr/bin/python2.6

import os
import json
import urllib

import tornado.httpserver
import tornado.ioloop
import tornado.web


boss_http_base = "http://boss.yahooapis.com/ysearch/images/v1/"
app_id = "fOwNVoHV34FaT7MH5A6Jzl2.DTD1A2NQ6tz1i2.f1zxxxSmVkO2M1RM1267Qx80-"


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


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

        twitter_text = "#socialcommodity %s %s" % (image_url, query)
        twitter_url = "http://twitter.com/home?status=" + urllib.quote(twitter_text)
        self.redirect(twitter_url)


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

application = tornado.web.Application(
    [(r"/", IndexHandler),
     (r"/search", SearchHandler),
     (r"/tweet", TweetHandler)],
    **settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
