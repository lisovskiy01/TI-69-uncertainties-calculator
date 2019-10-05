from lib import calculator as calc
from sys import exit

print('''
-------------------------------------------
|                  TI-69                  | 
| Uncertainty calculator for IB chemistry |
|       version 1.0 by Gilfoyle M.        |
-------------------------------------------\n\n
''')

#-------------------Interface-------------------

menu = '''
Current supported operations:

(1) Uncertainty to percentage uncertainty
(2) Uncertainty to fractional uncertainty
(3) Percentage to absolute uncertainty
(4) Fractional to absolute uncertainty

(0) Exit

'''

print(menu)

prompt = "Input measurements in format [value,uncertainty,unit]: "
#(5) Add measurements with uncertainties #TODO
#(6) Subract measurements with uncertainties #TODO
#(7) Multiple measurments with uncertainties #TODO
#(8) Divide measurments with uncertainties #TODO
#(n) More?


#--------------------Definitions--------------------
def valueParse(data):
    data = data.split(',')
    try:
        data[0] = float(data[0])
        data[1] = float(data[1])
        data[2] = str(data[2])
        obj = calc.Object(data[0], data[1], data[2])
        return obj
    except:
        print('Wrong format: use numbers separated by comas')
        exit(1)



if __name__ == '__main__': # Execution start
    while True:
        operation = str(input("Input number: ")) # Ask for command
        #print(operation+" type: "+str(type(operation)))

        if operation == '0':
            exit(0)
        elif operation == '1':
            input_data = input(prompt)
            calc.calcPerc(valueParse(input_data))
        elif operation == '2':
            input_data = input(prompt)
            calc.calcFrac(valueParse(input_data))
        elif operation == '3':
            input_data = input(prompt)
            calc.percToAbs(valueParse(input_data))
        elif operation == '4':
            input_data = input(prompt)
            calc.fracToAbs(valueParse(input_data))
        else:
            print("Operation unsupported\n\n")
