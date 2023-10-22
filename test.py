from get_tooles import get_tools
from get_tools_description import get_description,get_name
from work_prompt import get_work_prompt
tools=get_tools()
question="What barbecue restaurant is 1000 meters around Shandong University"
print(get_work_prompt(get_description(tools),question,get_name(tools),"null",2))
