def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print("BMI = " + str(bmi))
    weight_classification(bmi)


def weight_classification(bmi):
    if bmi < 18.5:
        print("under weight")
    elif bmi >= 18.5 and bmi <= 25.0:
        print("normal weight")
    else:
        print("over weight")

calculate_bmi(weight=57, height=1.73)

