import os
import tornado.ioloop
import tornado.web

root = os.path.dirname(__file__)
port = 9999


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        argument = self.get_argument('argument', '')

        login_response = {}
        if not argument:
            login_response = {
                'error': True,
                'msg': 'Thank You.'
            }

        # self.write on dicts produces json
        self.write(login_response)

application = tornado.web.Application(
    [
        (r"/", MainHandler),
    ],
    template_path=root + 'template/',
    static_path=root)

if __name__ == '__main__':
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
