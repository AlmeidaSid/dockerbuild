import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_resultados_nba(client):
    response = client.get('/v1/resultados_nba')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert len(data) > 0