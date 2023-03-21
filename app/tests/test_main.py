from fastapi.testclient import TestClient
# from .calculate_grade import calculate_grade

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
    
def test_80():
    response = client.get("/calculate_grade/80")
    assert response.status_code == 200
    assert response.json() == {"grade": "A"}


# def test_result_a_score_100():
#     score = 100
#     expected_result = "A"
#     actual_result = calculate_grade(score)
#     assert expected_result == actual_result
    
# def test_result_a_score_80():
#     score = 80
#     expected_result = "A"
#     actual_result = calculate_grade(score)
#     assert expected_result == actual_result