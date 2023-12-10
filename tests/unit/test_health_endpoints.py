import pytest


class TestHealthChecks:
    @pytest.fixture(scope="class")
    def _generate_token(self, client, prefix):
        """Generate a token to be used by the rest of the class."""
        credentials = {"username": "tester", "password": "password"}
        response = client.post(f"{prefix}/auth", data=credentials)
        response_json = response.json()
        token = response_json["auth_token"]
        assert response.status_code == 200
        return token

    def test_health(self, client, prefix):
        """Test unauthenticated health endpoint"""
        response = client.get(f"{prefix}/health")
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["message"] == "success"

    def test_authenticated_health(self, client, prefix, _generate_token):
        """Test authenticated health endpoint"""
        response = client.get(
            f"{prefix}/healthz", headers={"Authorization": f"Bearer {_generate_token}"}
        )
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["message"] == "success"

    def test_authenticated_health_bad_token(self, client, prefix, _generate_token):
        """Test unauthenticated health endpoint with a bad JWT token."""
        bad_token = "a" + _generate_token
        response = client.get(
            f"{prefix}/healthz", headers={"Authorization": f"Bearer {bad_token}"}
        )
        response_json = response.json()

        # print(response_json)
        assert response.status_code == 401
        assert response_json["status"] == "fail"
        assert response_json["message"] == ["Invalid header padding"]
