from flask import Flask, render_template, send_from_directory, url_for, request, redirect
from flask_login import LoginManager, login_manager, current_user, login_user

# Usuarios
from models import users, User

app = Flask(__name__, static_url_path='')
login_manager = LoginManager()
login_manager.init_app(app) # Para mantener la sesión

# Configurar el secret_key. OJO, no debe ir en un servidor git público.
# Python ofrece varias formas de almacenar esto de forma segura, que
# no cubriremos aquí.
app.config['SECRET_KEY'] = 'qH1vprMjavek52cv7Lmfe1FoCexrrV8egFnB21jHhkuOHm8hJUe1hwn7pKEZQ1fioUzDb3sWcNK1pJVVIhyrgvFiIrceXpKJBFIn_i9-LTLBCc4cqaI3gjJJHU6kxuT8bnC7Ng'

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        error = None
        if request.method == "POST":
            if request.form['email'] != 'admin@um.es' or request.form['password'] != 'admin':
                error = 'Invalid Credentials. Please try again.'
            else:
                user = User(1, 'admin', request.form['email'].encode('utf-8'),
                            request.form['password'].encode('utf-8'))
                users.append(user)
                login_user(user)
                return redirect(url_for('index'))
    return render_template('login.html',  error=error)
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = get_user(form.email.data)
    #     if user is not None and user.check_password(form.password.data):
    #         login_user(user, remember=form.remember_me.data)
    #         next_page = request.args.get('next')
    #         if not next_page or url_parse(next_page).netloc != '':
    #             next_page = url_for('index')
    #         return redirect(next_page)

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')