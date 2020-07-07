from flask import Flask, render_template
# from app import app

app=Flask(__name__, template_folder='template')
@app.route('/')
def index():
    user = {'username': 'AKASH'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('third.html', title='Home', user=user, posts=posts)

if(__name__)=='__main__':
	app.run(debug=True)


# from flask import Flask , render_template

# app=Flask(__name__)

# @app.route('/')
# def random():
# 	return render_template('third.html')

# # @app.route('/about')
# # def contact():
# # 	return random()+" AKASH"


# if(__name__)=='__main__':
# 	app.run(debug=True)

