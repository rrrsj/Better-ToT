import json
import secrets
import requests
from key import api_key
def get_gpt_output(question,parent):
    headers = {
    'authority': 'ai-panda.xyz',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    'cookie': 'cf_chl_rc_m=1; cf_clearance=PQesPHRIMoe4waLJZxcfd6erYM_xUi3Z5NyBLkkY36c-1698027129-0-1-82be0d09.6250c9a2.d9d3dae8-0.2.1698027129',
    'origin': 'https://ai-panda.xyz',
    'referer': 'https://ai-panda.xyz/',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'token': '634ef20148465a6e1046a8cf44efec07',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
}
    data = f'{{"prompt":"{question}","parentMessageId":"{parent}","persona_id":"","options":{{"model":"gpt-3.5-turbo-16k","temperature":0.8,"presence_penalty":0,"frequency_penalty":0,"max_tokens":1888}}}}'
    response = requests.post('https://ai-panda.xyz/api/chat/completions', headers=headers,data=data)
    return response

def get_text(now):
    linshi=now.text
    list=linshi.split('\n')
    ans=''
    for i in range(0,len(list)-1,2):
        c=json.loads(list[i].encode('utf8').decode('utf8'))
        ans=ans+c['content']
    return ans
def generate_random_hex():
    random_bytes = secrets.token_bytes(16)
    hex_num = random_bytes.hex()
    return hex_num
def get_ans(question):
    output=get_gpt_output(question,str(generate_random_hex()))
    ans=get_text(output)
    return ans