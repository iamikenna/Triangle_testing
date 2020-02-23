""" This is a traingle function"""
def classify_triangle(a_word, b_word, c_word):
    """ Your correct code goes here. Fix the faulty logic below until the code passes"""
    if a_word >= 200 or b_word >= 200 or c_word >= 200:
        return 'InvalidInput'
    elif a_word <= 0 or b_word <= 0 or c_word <= 0:
        return 'InvalidInput'
    elif (a_word+b_word) <= c_word or (a_word+c_word) <= b_word or (b_word+c_word) <= a_word:
        return 'NotATriangle'
    elif a_word == b_word and b_word == c_word and a_word == c_word:
        return "Equilateral"
    elif(a_word ** 2 + b_word ** 2) == c_word ** 2: #Checking for Right triangles
        return "Right"
    elif a_word != b_word and a_word != c_word and b_word != c_word: #Checking
        return "Scalene"
    elif a_word == b_word and a_word != c_word and b_word != c_word:#Checking
        return "Isosceles"
    elif a_word != b_word and a_word == c_word and b_word != c_word:#Checking
        return "Isosceles"
    elif a_word != b_word and b_word == c_word and a_word != c_word:#Checking
        return "Isosceles"
    else:
        return None



if __name__ == '__main__':
    classify_triangle(3, 5, 6)
