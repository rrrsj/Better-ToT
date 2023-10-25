import json
import re
from get_tooles import get_tools,get_available_tools
from get_tools_description import get_description,get_name
from work_prompt import get_work_prompt
from test import get_ans
from tool_prompt import get_tool_prompt
from normail_tool_output import normail_tool_output
from normail_work_output import normail_work_output
from tree_node import tree_node
from build_tree import build_tree
from use_tool import use_tools
now_node=0
num=2
tree=[]
question="Calculate (1+1) *3/4"
start_node = tree_node(0, [], question, 'null')
tree.append(start_node)
input = f"{question}.Generate {num} plan for me."
tools = get_tools()
prompt=get_work_prompt(get_description(tools),input,get_name(tools),tree[now_node].environment,num)
prompt =prompt.replace('\n', '\\n')
prompt =prompt.replace('\"', '\'')
ans=get_ans(prompt)
while 1:
    try:
        ans=normail_work_output(ans)
        tree = build_tree(0, tree, ans)
        continue
    except:
        break
while 1:
    while len(tree[now_node].child)==0:
        now_node=tree[now_node].father
        del tree[now_node].child[0]
    if len(tree)==0:
        print("error")
        break
    maxnum=0
    maxposition=0
    for i in range(len(tree[now_node].child)):
        if tree[tree[now_node].child[i]].action["score"]>maxnum:
            maxnum=tree[tree[now_node].child[i]].action["score"]
            maxposition=i
    linshi=tree[now_node].child[0]
    tree[now_node].child[0]=i
    tree[now_node].child[i]=linshi
    now_node=tree[now_node].child[0]
    one_tool=get_tools(one=True,name=tree[now_node].action["action"])
    tool_prompt=get_tool_prompt(get_description(one_tool),get_name(one_tool),tree[tree[now_node].father].environment,question)
    prompt = prompt.replace('\n', '\\n')
    prompt = prompt.replace('\"', '\'')
    tool_output = get_ans(tool_prompt)
    while 1:
        try:
            print("111")
            tool_output=normail_tool_output(tool_output)
            break
        except:
            continue
    if "Final Answer" in tool_output["action"]:
        print(tool_output["action_input"])
    else:
        try:
            ans=use_tools(message=tool_output,tools_list=get_available_tools())
            tree[now_node].environment=tree[tree[now_node].father].environment+'\n'+ans
        except:
            now_node=tree[now_node].father
            del tree[now_node].child[0]
            continue
    prompt=get_work_prompt(get_description(tools),input,get_name(tools),tree[now_node].environment,num)
    prompt =prompt.replace('\n', '\\n')
    prompt =prompt.replace('\"', '\'')
    ans = get_ans(prompt)
    while 1:
        try:
            ans=normail_work_output(ans)
            tree = build_tree(0, tree, ans)
            continue
        except:
            break


    
    