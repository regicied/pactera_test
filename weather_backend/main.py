#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : main.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/3/21 10:27
# @Desc  :
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

CONFIG = dict(
    weather_api='https://api.oceandrivers.com:443/v1.0/getWeatherDisplay/{city}/?period=latestdata',
)


class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self, city):
        external_address = CONFIG['weather_api']
        client = AsyncHTTPClient()
        external_address = external_address.format(city=city)
        response = yield client.fetch(external_address)

        response = json.loads(response.body)
        temperature = response.get('TEMPERATURE')
        wind = response.get('TWS_GUST')
        weather = response.get('WEATHER_DES')
        timestamp = response.get('TIME_STRING')
        res = dict(
            temperature=temperature,
            weather=weather,
            wind=wind,
            timestamp=timestamp,
            city=city
        )
        self.write(res)


class TestHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(dict(status=True))


def make_app():
    return tornado.web.Application([
        (r"/weather/(?P<city>.+)", MainHandler),
        (r"/test", TestHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    # server = tornado.httpserver.HTTPServer(app)
    # server.bind(8888)
    # server.start(0)  # forks one process per cpu
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
