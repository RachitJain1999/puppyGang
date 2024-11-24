from flask import Flask,render_template,request

app  =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup_form():
    return render_template('signup.html')

@app.route('/thankyou')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thank_you.html',first=first,last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'),404

if __name__ ==  '__main__' :
    app.run(debug=True)