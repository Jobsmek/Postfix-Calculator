class operations:
    def add(num1, num2):
        convertedNum1 = int(num1)
        convertedNum2 = int(num2)
        num3 = convertedNum1 + convertedNum2
        return num3
    def sub(num1, num2):
        convertedNum1 = int(num1)
        convertedNum2 = int(num2)
        num3 = convertedNum1 - convertedNum2
        return num3
    def div(num1, num2):
        convertedNum1 = int(num1)
        convertedNum2 = int(num2)
        if convertedNum2 == 0:
            return "ERROR: Division by zero"
        else:
            num3 = convertedNum2 / convertedNum1
            return num3
    def mult(num1, num2):
        convertedNum1 = int(num1)
        convertedNum2 = int(num2)
        num3 = convertedNum1 * convertedNum2
        return num3
    def pow(num1, num2):
        convertedNum1 = int(num1)
        convertedNum2 = int(num2)
        num3 = pow(convertedNum1, convertedNum2)
        return num3