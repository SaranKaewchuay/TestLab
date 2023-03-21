# input score
# score >= 70 -A    (70 / 100)
# score >= 50 -D    (50 / 69)
# score < 50 -F     (0 / 49)

def calculate_grade(score) :
    if score >= 70:
        return "A"
    elif score >= 50:
        return "D"
    else:    
        return "F"