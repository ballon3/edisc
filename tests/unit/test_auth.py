def test_auth_correct(client, prefix):
    """Test login with correct credentials"""
    credentials = {"username": "tester", "password": "password"}
    response = client.post(f"{prefix}/auth", data=credentials)
    response_json = response.json()
    token = response_json["auth_token"]

    assert response.status_code == 200
    assert response_json["status"] == "success"
    assert response_json["message"] == "Successfully logged in."
    assert type(token) == str


def test_auth_bad_user(client, prefix):
    """Test login with incorrect username."""
    credentials = {"username": "wrong", "password": "password"}
    response = client.post(f"{prefix}/auth", data=credentials)
    response_json = response.json()

    assert response.status_code == 400
    assert response_json["status"] == "fail"
    assert response_json["message"] == "User does not exist."


def test_auth_bad_password(client, prefix):
    """Test login with incorrect password."""
    credentials = {"username": "tester", "password": "wrong"}
    response = client.post(f"{prefix}/auth", data=credentials)
    response_json = response.json()

    assert response.status_code == 400
    assert response_json["status"] == "fail"
    assert response_json["message"] == "Password is incorrect."


def test_auth_bad_username_password(client, prefix):
    """Test login with incorrect username and password. Should return username error first."""
    credentials = {"username": "teste", "password": "wrong"}
    response = client.post(f"{prefix}/auth", data=credentials)
    response_json = response.json()

    assert response.status_code == 400
    assert response_json["status"] == "fail"
    assert response_json["message"] == "User does not exist."
