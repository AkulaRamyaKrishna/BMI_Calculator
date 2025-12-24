def calculate_bmi(weight, height):
    return (weight * 703) / (height * height)

def calculate_bmi(weight, height):
    return (weight * 703) / (height * height)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal weight"
    elif bmi <= 29.9:
        return "Overweight"
    elif bmi <= 34.9:
        return "Obese"
    elif bmi <= 39.9:
        return "Severely Obese"
    else:
        return "Morbidly Obese"

    