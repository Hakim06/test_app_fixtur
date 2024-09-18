from tests.conftest import client

def test_should_status_code_ok(client):
    response = client.get('/index')          # Envoyer une requête GET à /index
    assert response.status_code == 200

def test_should_return_hello_world(client):
    response = client.get('/index')           # Envoyer une requête GET à /index
    data = response.data.decode()             # Décoder la réponse pour obtenir le texte
    assert data == 'Hello, World!'

def test_should_login_succfully(client):
    
    response = client.post('/login', data={'username' : 'testUser', 'password' : 'testPassword'})    # Envoyer une requête POST à /post_example
    assert response.status_code == 200         # Vérifier que la réponse est 200 
    assert response.json['message']=="Login successful!"

def test_should_login_fail(client):
    response= client.post('/login', data = {'username': 'testUser', 'password': 'wrongPassWord'})
    assert response.status_code==401
    assert response.json['message']== 'Login failed!'

def test_login_logout(client):
    client.post('/login', data={'username': 'testUser', 'password': 'testPassword'})
    response= client.post('/logout')
    assert response.status_code ==200
    assert response.json['message'] == "Logout successful!"