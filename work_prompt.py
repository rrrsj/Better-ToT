def get_work_prompt(tool_description,question,tool_names,environment,num):
    message=f'You are a planner and you can use tools to solve problems.A tool is an api that takes inputs and feeds back outputs.\n\
All available tools are listed following, including their names,function descriptions, input paramaters and examples of use:\n\
{tool_description}\
You need to generate {num} plans based on the current situation. \n\
Your output should be a list of {num} elements, each element is a dictionary representing a plan, each dictionary contains planid, step, where step is a list and each element is a step containing stepid, action, action input, score, The action input is also a dictionary\n  \
In particular, if you want to use the output of a step, you can use $stepid to indicate it.\n\
[{{\
"planid":(This is the number of the plan,it should be a number),\
"step":\
[{{\
"stepid":(This is the number of the step,it should be a number),\
"action":the action to take, should be one of [{tool_names}],\
"action_input":the input to the action,It should be a dictionary {{"paramter":"value"}},\
"score":How important you think this step is on a scale of 1-5, with higher scores indicating greater importance\
}}...List can contain multiple steps]\
}},...List should contain {num} plans]\n\
Here is an example:\n \
Environment:null.\n\
Question:What is the weather like in Beijing?Generate 1 plan for me\n\
Answer:\n\
{{\
"planid":"1",\
"step":\
[\
{{\
"stepid":"1",\
"action":"get_local",\
"action_input":{{"local_now":"Beijing"}},\
"score":4\
}},\
{{\
"stepid":"2",\
"action":"get_weather",\
"action_input":{{"longitude":"$1","dimensionality":"$1"}},\
"score":4\
}}\
]\
}}]\n\
You should base your answer on the environment and the question.You must generate {num} plans,list should contain {num} elements!!\n\
Environment:{environment}.\n\
Question:{question}\n\
Answer:\n'
    return message