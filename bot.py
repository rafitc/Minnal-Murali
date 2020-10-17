from flask import Flask, request
from urllib import unquote_plus
import json
import re
import json 


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    Go to localhost:5000 to see a message
    """
    return ('This is a website.', 200, None)


@app.route('/web', methods=['POST'])
def parse_request():
    data = request.get_data()
    data_parser(data)
    return("OK",200)
    # need posted

def data_parser(data):
   sort = json.loads(data)
   email = sort['form_response']['answers'][1]['email']
   name = sort['form_response']['answers'][0]['text']
   print(name)
   print(email)
   

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)