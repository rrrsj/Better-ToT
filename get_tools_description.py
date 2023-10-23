def get_description(tools):
    ans=''
    for i in tools:
        tool_name=i["name"]
        tool_use=i["description"]
        tool_parameter=''
        for key in i['parameters']['properties']:
            tool_parameter=tool_parameter+key+f"(type:{i['parameters']['properties'][key]['type']}"+f"parameter description:{i['parameters']['properties'][key]['description']}),"
        ans=ans+f"Tool's name:{tool_name},\
    Tool description:{tool_use},\
    Tool's parameters:{tool_parameter}.\\n"
    return ans
def get_name(tools):
    ans=''
    for i in tools:
        ans=ans+i["name"]+','
    ans=ans[:-2]
    return ans