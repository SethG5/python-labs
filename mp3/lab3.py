def bmiCal(height, weight):
    bmi = weight/(height**2)
    return bmi
    
def bmiCat(bmi):
    if bmi < 18.5:
        return 'under weight'
    elif bmi < 25:
        return 'normal weight'
    elif bmi < 30:
        return 'over weight'
    else:
        return 'obese'

### user inputs ###
weight = float(input("Weight (KG): "))
height = float(input("Height (METERS): "))
### returns ###

print(f'You have a bmi of {bmiCal(height, weight)}\nand you are {bmiCat(bmiCal(height, weight))}')


