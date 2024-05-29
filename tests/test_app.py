import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_resultados_nba(client):
    """Testa a rota /v1/resultados_nba"""
    rv = client.get('/v1/resultados_nba')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert isinstance(json_data, list)
    assert len(json_data) == 3
    assert json_data[0]['time_casa'] == 'Los Angeles Lakers'
    assert json_data[1]['time_visitante'] == 'Milwaukee Bucks'
    assert json_data[2]['pontos_casa'] == 98
