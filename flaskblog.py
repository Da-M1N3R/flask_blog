from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Kim Chaewon',
        'title': 'LE SSERAFIM - Lead Singer',
        'content': 'Darwin, you are discipline, relentless & unpredictable. You will be a fine young man.',
        'date_posted': 'July 21, 2023',
    },
    {
        'author': 'Kok Jia Wei',
        'title': 'Nestle - Food Science Engineer',
        'content': 'Darwin, you will be rich. With your work ethic and mindset, nothing can stand in your way. Remember that.',
        'date_posted': 'March 22, 2023',
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)