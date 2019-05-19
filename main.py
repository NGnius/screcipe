from flask import Flask
import api

app = Flask(__name__)
api_routings = api.APIController(app)

if __name__ == '__main__':
    app.run(threaded=True)
