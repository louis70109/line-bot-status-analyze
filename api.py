
from controller.line_controller import LineController
from controller.kuma_controller import KumaController
from flask_restful import Api
from flask_cors import CORS
from flask import Flask
import logging
import os

debug = False
if os.getenv('PY_ENV') != 'production':
    from dotenv import load_dotenv
    load_dotenv()
    debug = True


logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)
app = Flask(__name__)
CORS(app)

api = Api(app)


@app.get("/")
def check():
    return {"message": "Hello World!"}


api.add_resource(LineController, '/webhooks/line')
api.add_resource(KumaController, '/kuma')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=debug)
