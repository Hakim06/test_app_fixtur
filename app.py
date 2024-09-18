from flask import Flask, request, jsonify, session

def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key='supersecretkey'

    @app.route('/index')
    def index():
        return 'Hello, World!'
    

    @app.route('/login', methods=['POST'])
    def login():
        username = request.form.get('username')
        password = request.form.get('password')

        if username== 'testUser' and password == 'testPassword':
            session['logging_in']= True
            return jsonify({"message" : "Login successful!"}), 200
        else:
            return jsonify({"message": "Login failed!"}), 401
        
    @app.route('/logout', methods=['POST'])   
    def logout() :
        session.pop('logging_in', None)  
        print(f"Session after logout: {session}")
        return jsonify({"message": "Logout successful!"}), 200

    return app