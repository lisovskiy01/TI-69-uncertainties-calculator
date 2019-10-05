'''
Calculation lib for chemlab
'''

class FormatError: # Reserved for future error handling
    def __init__(self):
        print("Wrong format")

# Class for measurment
class Object:
    def __init__(self, value, uncertainty, unit):
        self.value = value
        self.uncertainty = uncertainty
        self.unit = unit

# Calculate percentage uncertainty
def calcPerc(object):
    uncertainty = object.uncertainty
    value = object.value
    unit = object.unit

    if unit == "C" or unit == "c":
        value = value+273
        unit,object.unit = "F"


    result = uncertainty/value*100
    print("Percentage uncertainty: %s +- %s %s" % (value,result,unit))


# Calculate fractional uncertainty
def calcFrac(object):
        uncertainty = object.uncertainty
        value = object.value
        unit = object.unit

        if unit == "C" or unit == "c":
            value = value+273
            unit,object.unit = "F"

        result = uncertainty/value
        print("Fractional uncertainty: %s +- %s %s" % (value,result,unit))


# Calculate percentage error
def percToAbs(object):
    uncertainty = object.uncertainty
    value = object.value
    unit = object.unit

    result = uncertainty*value/100
    print("Abs. uncertainty: %s +- %s %s" % (value,result,unit))


# Fractional back to absolute uncertainty

def fracToAbs(object):
    uncertainty = object.uncertainty
    tvalue = object.value
    unit = object.unit

    if unit == "C" or unit == "c":
            value = value+273
            unit,object.unit = "F"

    result = uncertainty*value
    print("Result: %s +- %s %s" % (value,result,unit))


# Percentagge back to absoult unsertainty
def percToAbs(object):
    uncertainty = object.uncertainty
    value = object.value
    unit = object.unit

    if unit == "C" or unit == "c":
            value = value+273
            unit,object.unit = "F"

    result = uncertainty/100*value
    print("Result: %s +- %s %s" % (value,result,unit))
