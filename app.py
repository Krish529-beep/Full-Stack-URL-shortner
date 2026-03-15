from flask import Flask
from model import (
    initdb,
    insert_url,
    get_all_urls,
    get_url,
    incerement_visit_count,
    delete_url_by_code
    )

app = Flask(__name__) # allows flask to scan scan everything in src project folder

@app.route('/') # route decorator to specify the url for the function
def hello_world():
    return 'Hello to flask'

if __name__ == '__main__':
    app.run(debug=True) # debug para for logs