from flask import Flask, render_template, request, redirect, session
from database import create_tables
from routes import register_blueprints

app = Flask(__name__)
app.secret_key = 'chave_super_secreta'

@app.before_request
def require_register():
    allowed_routes = ['auth_bp.register', 'static']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/register')

@app.route('/')
def index():
    return render_template('index.html')

register_blueprints(app)

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, port=8080)
