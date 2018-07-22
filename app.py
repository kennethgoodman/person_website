import tornado.ioloop
import tornado.web
import os


settings = {'debug': True,
            # 'static_path': '~/PycharmProjects/person_website/static',
            'autoreload': True

            }


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/index.html")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {'path': './static/images/'})
        # /(r"/static/images/(.*)", tornado.web.StaticFileHandler,  {'path':'~/PycharmProjects/person_website/'}),
        # (r'/(github\.png)', tornado.web.StaticFileHandler, {'path':'~/PycharmProjects/person_website/static/images/'})
    ], **settings
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()