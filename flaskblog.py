from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ad7c50b9dec61f71dfefc43baa0195ff'

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)