import json
import re
from get_tooles import get_tools
from get_tools_description import get_description,get_name
from work_prompt import get_work_prompt
from test import get_output
now_node=0
num=1
tree=[]
question="Find barbecue restaurants 1000 meters around Shandong University's Qingdao campus"
input = f"{question}.Generate {num} plan for me."
tools = get_tools()
prompt=get_work_prompt(get_description(tools),input,get_name(tools),"null",num)
print(prompt)
ans=get_output(prompt)
print(ans)

    
    