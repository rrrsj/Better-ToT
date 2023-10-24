from tools.math import division_calculator,adding_computer,subtraction_calculator,multiplication_calculator
def use_tools(message,tools_list):
    if "multiplication_calculator" in message["ation"]:
        return tools_list["multiplication_calculator"](num1=message["action_input"]["num1"],num2=message["action_input"]["num2"])
    elif "division_calculator" in message["ation"]:
        return tools_list["division_calculator"](num1=message["action_input"]["num1"],num2=message["action_input"]["num2"])
    elif "adding_computer" in message["ation"]:
        return tools_list["adding_computer"](num1=message["action_input"]["num1"],num2=message["action_input"]["num2"])
    elif "subtraction_calculator" in message["ation"]:
        return tools_list["subtraction_calculator"](num1=message["action_input"]["num1"],num2=message["action_input"]["num2"])