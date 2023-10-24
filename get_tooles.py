from tools.math import division_calculator,adding_computer,subtraction_calculator,multiplication_calculator
def get_tools(retiver=None,k=None,one=False,name=""):
    tooles = [
        {
            "name": "multiplication_calculator",
            "description": "Enter two numbers and calculate their multiplication.",
            "parameters": {
                "properties": {
                    "num1": {
                        "type": "float",
                        "description": "The first multiplier.",
                    },
                    "num2":{
                        "type":"float",
                        "description":"The second multiplier.",
                    }
                },
            },
        },
        {
            "name": "division_calculator",
            "description": "Enter two numbers and calculate their division.",
            "parameters": {
                "properties": {
                    "num1": {
                        "type": "float",
                        "description": "dividend.",
                    },
                    "num2": {
                        "type": "float",
                        "description": "divisor.",
                    }
                },
            },
        },
        {
            "name": "adding_computer",
            "description": "Enter two numbers and calculate their adding.",
            "parameters": {
                "properties": {
                    "num1": {
                        "type": "float",
                        "description": "The first addition.",
                    },
                    "num2": {
                        "type": "float",
                        "description": "The second addition.",
                    }
                },
            },
        },
        {
            "name": "subtraction_calculator",
            "description": "Enter two numbers and calculate their subtraction.",
            "parameters": {
                "properties": {
                    "num1": {
                        "type": "float",
                        "description": "subtraction.",
                    },
                    "num2": {
                        "type": "float",
                        "description": "subtrahend.",
                    }
                },
            },
        },
    ]
    if retiver==None and not one:
        return tooles
    else:
        for i in tooles:
            if(i["name"]==name):
                ans=[]
                ans.append(i)
                return ans
def get_available_tools():
    available_tools = {
        "multiplication_calculator":multiplication_calculator,
        "division_calculator":division_calculator,
        "adding_computer":adding_computer,
        "subtraction_calculator":subtraction_calculator,
    }
    return available_tools

        
