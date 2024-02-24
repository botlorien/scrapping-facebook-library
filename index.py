from flask import Flask, jsonify
import tasks as ts

app = Flask(__name__)


# Define a route for the API
@app.route('/', methods=['GET'])
def get_facebook_ads():
    # Return a simple JSON response
    return jsonify({'message': [ts.get_facebook_ads()]})


if __name__ == '__main__':
    app.run(debug=True)
