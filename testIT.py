from Tools.Scripts.treesync import raw_input

def checkCircumference():
    diameter = float(raw_input("What is the diameter?"))
    print (diameter * 3.142 )

def checkDiameter():
    radius = float(raw_input("What is the radius?"))
    print ( radius * 2 )

def checkRadius():
    diameter = float(raw_input("What is the diameter?"))
    radius = float(raw_input("What is the radius?"))
    print ( diameter / radius)

def checkArea():
    radius = float(raw_input("What is the radius?))"))
    print ( 3.142 * (radius^2))

def whatToCheck():
    choice = input("What would you like to check?")
