import json
import re
from get_tooles import get_tools
from get_tools_description import get_description,get_name
from work_prompt import get_work_prompt
from test import get_ans
from tool_prompt import get_tool_prompt
from normail_work_output import normail_work_output
from tree_node import tree_node
from build_tree import build_tree
now_node=0
num=2
tree=[]
question="Find barbecue restaurants 1000 meters around Shandong University's Qingdao campus"
start_node = tree_node(0, [], question, 'null')
tree.append(start_node)
input = f"{question}.Generate {num} plan for me."
tools = get_tools()
prompt=get_work_prompt(get_description(tools),input,get_name(tools),tree[now_node].environment,num)
prompt =prompt.replace('\n', '\\n')
prompt =prompt.replace('\"', '\'')
ans=get_ans(prompt)
ans=normail_work_output(ans)
tree = build_tree(0, tree, ans)
while 1:
    while len(tree[now_node].child)==0:
        now_node=tree[now_node].father
        del tree[now_node].child[0]
    now_node=tree[now_node].child[0]
    one_tool=get_tools(one=True,name=tree[now_node].action["action"])
    tool_prompt=get_tool_prompt(get_description(one_tool),input,get_name(one_tool),tree[tree[now_node].father].environment,question)
    prompt = get_tool_prompt(get_description(one_tool), get_name(one_tool), tree[tree[now_node].father].environment,question)
        #if(error)
            #回到父节点，然后删除这条支路
        continue
    prompt=get_work_prompt(get_description(tools),input,get_name(tools),tree[now_node].environment,num)
    prompt =prompt.replace('\n', '\\n')
    prompt =prompt.replace('\"', '\'')
    ans=get_ans(prompt)
    ans=normail_work_output(ans)
    tree = build_tree(0, tree, ans)


    
    