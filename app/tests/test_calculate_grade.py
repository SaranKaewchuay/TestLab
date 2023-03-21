from .calculate_grade import calculate_grade

def test_result_a_score_100():
    score = 100
    expected_result = "A"
    actual_result = calculate_grade(score)
    assert expected_result == actual_result
    
def test_result_a_score_80():
    score = 80
    expected_result = "A"
    actual_result = calculate_grade(score)
    assert expected_result == actual_result

def test_result_a_score_70():
    score = 70
    expected_result = "A"
    actual_result = calculate_grade(score)
    assert expected_result == actual_result

def test_result_d_score_69():
    score = 69
    expected_result = "D"
    actual_result = calculate_grade(score)
    assert expected_result == actual_result

def test_result_d_score_60():
    score = 60
    expected_result = "D"
    actual_result = calculate_grade(score)
    assert expected_result == actual_result

def test_result_d_score_50():
    score = 50
    expected_result = "D"
    actual_result = calculate_grade(score)
    assert expected_result == actual_result
    
def test_result_f_score_49():
    score = 49
    expected_result = "F"
    actual_result = calculate_grade(score)
    assert expected_result == actual_result
    
def test_result_f_score_5():
    score = 5
    expected_result = "F"
    actual_result = calculate_grade(score)
    assert expected_result == actual_result
    
def test_result_f_score_0():
    score = 0
    expected_result = "F"
    actual_result = calculate_grade(score)
    assert expected_result == actual_result




    

