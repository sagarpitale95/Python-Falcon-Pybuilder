import falcon
import logging

from services import HelloWorld

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

api = application = falcon.App()

hi = HelloWorld()

api.add_route('/hi', hi)
