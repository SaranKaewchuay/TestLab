from fastapi.testclient import TestClient
from .calculate_grade import calculate_grade

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
    

def test_result_a_score_100():
    response = client.get("/calculate_grade/100")
    expected_result = "A"
    actual_result = response.json()
    assert response.status_code == 200
    assert expected_result == actual_result
    
def test_result_a_score_80():
    response = client.get("/calculate_grade/80")
    expected_result = "A"
    actual_result = response.json()
    assert response.status_code == 200
    assert expected_result == actual_result
    
        
def test_result_a_score_70():
    response = client.get("/calculate_grade/70")
    expected_result = "A"
    actual_result = response.json()
    assert response.status_code == 200
    assert expected_result == actual_result
    
  

def test_result_d_score_69():
    response = client.get("/calculate_grade/69")
    expected_result = "D"
    actual_result = response.json()
    assert response.status_code == 200
    assert expected_result == actual_result

def test_result_d_score_60():
    response = client.get("/calculate_grade/60")
    expected_result = "D"
    actual_result = response.json()
    assert response.status_code == 200
    assert expected_result == actual_result

def test_result_d_score_50():
    response = client.get("/calculate_grade/50")
    expected_result = "D"
    actual_result = response.json()
    assert response.status_code == 200
    assert expected_result == actual_result
    
def test_result_f_score_49():
    response = client.get("/calculate_grade/49")
    expected_result = "F"
    actual_result = response.json()
    assert response.status_code == 200
    assert expected_result == actual_result
    
def test_result_f_score_5():
    response = client.get("/calculate_grade/5")
    expected_result = "F"
    actual_result = response.json()
    assert response.status_code == 200
    assert expected_result == actual_result
    
def test_result_f_score_0():
    response = client.get("/calculate_grade/0")
    expected_result = "F"
    actual_result = response.json()
    assert response.status_code == 200
    assert expected_result == actual_result


