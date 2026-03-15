from flask import Flask,request,redirect,render_template
import string
import random

from model import (
    initdb,
    insert_url,
    get_all_urls,
    get_url,
    incerement_visit_count,
    delete_url_by_code
    )

app = Flask(__name__) # allows flask to scan scan everything in src project folder
initdb()

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits,k=length))
    
@app.route('/',methods=['GET','POST']) # route decorator to specify the url for the function
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        insert_url(original_url,short_code)
        return redirect('/')
    
    all_urls = get_all_urls()
    return render_template('index.html',all_urls=all_urls)
    
@app.route('/<short_code>')
def redirect_url(short_code):
    # print(short_code)
    url_data=get_url(short_code)
    if url_data:
        incerement_visit_count(short_code)
        return redirect(url_data[1])
    return render_template('404.html')

@app.route('/delete/<short_code>',methods=['POST'])
def delete_url(short_code):
    delete_url_by_code(short_code)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            
            ) # debug para for logs