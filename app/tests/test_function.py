from function import number_to_month,validate_number
import pytest

@pytest.mark.code  # pytest -m code
def test_january_input_1():
    input = 1
    expected_result = "january"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_february_input_2():
    input = 2
    expected_result = "february"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_march_input_3():
    input = 3
    expected_result = "march"
    actual_result = number_to_month(input)
    assert expected_result == actual_result
    
@pytest.mark.code 
def test_april_input_4():
    input = 4
    expected_result = "april"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_may_input_5():
    input = 5
    expected_result = "may"
    actual_result = number_to_month(input)
    assert expected_result == actual_result
    
@pytest.mark.code 
def test_june_input_6():
    input = 6
    expected_result = "june"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_july_input_7():
    input = 7
    expected_result = "july"
    actual_result = number_to_month(input)
    assert expected_result == actual_result
    
@pytest.mark.code 
def test_august_input_8():
    input = 8
    expected_result = "august"
    actual_result = number_to_month(input)
    assert expected_result == actual_result
    
@pytest.mark.code 
def test_september_input_9():
    input = 9
    expected_result = "september"
    actual_result = number_to_month(input)
    assert expected_result == actual_result
    
@pytest.mark.code 
def test_october_input_10():
    input = 10
    expected_result = "october"
    actual_result = number_to_month(input)
    assert expected_result == actual_result
    
@pytest.mark.code 
def test_october_input_11():
    input = 11
    expected_result = "november"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code 
def test_december_input_12():  
    input = 12
    expected_result = "december"
    actual_result = number_to_month(input)
    assert expected_result == actual_result
    
     
@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_0():  
    input = 0
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result
    
@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_13():  
    input = 13
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_minus_10():  
    input = -10
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result
    
@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_22():  
    input = 22
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result
    
@pytest.mark.validate # pytest -m validate
def test_input_integer_input_1_1():  
    input = 1.1
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_input_integer_input_13_1():  
    input = 13.1
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_input_integer_input_a():  
    input = "a"
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result
    
@pytest.mark.validate # pytest -m validate
def test_input_integer_input_sharp():  
    input = "#"
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_input_1():  
    input = 1
    expected_result = 1
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_input_12():  
    input = 12
    expected_result = 12
    actual_result = validate_number(input)
    assert expected_result == actual_result
    
@pytest.mark.validate # pytest -m validate
def test_input_0_5():  
    input = 0.5
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate # pytest -m validate
def test_input_minus_1_5():  
    input = -1.5
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_input_1_5():  
    input = 1.5
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result
