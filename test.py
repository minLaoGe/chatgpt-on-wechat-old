import openai
import requests
import json

params =  {
            "model": "gpt-3.5-turbo",  # 对话模型的名称
            "temperature": 0.9,  # 值在[0,1]之间，越大表示回复越具有不确定性
            # "max_tokens":4096,  # 回复最大的字符数
            "top_p": 1,
            "frequency_penalty": 0.0,  # [-2,2]之间，该值越大则更倾向于产生不同的内容
            "presence_penalty": 0.0,  # [-2,2]之间，该值越大则更倾向于产生不同的内容
            "request_timeout": 60,  # 请求超时时间，openai接口默认设置为600，对于难问题一般需要较长时间
            "timeout": 60,  # 重试超时时间，在这个时间内，将会自动重试
        }

api_key='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'
messages=[{"role":"user","content":"Hello"},{"role":"assistant","content":"Hello! How can I assist you today?"},{"role":"user","content":"Do you love me"},{"role":"assistant","content":"As an AI language model, I don't have emotions, so I don't have the capacity to love. However, I'm here to assist and provide helpful information to you. How can I assist you today?"},{"role":"user","content":"python中参数这些代表什么：   *args, **kwargs"}]
openai.proxy='http://localhost:8087/gateway/distribute'
# response = openai.ChatCompletion.create(
#     api_key=api_key, messages=messages, **params
# )
print("messages=",messages)
print("params=",params)

data = params
data['messages'] = messages
data['api_key'] = '1111'
headers = {
    'Content-Type': 'application/json',
    'client-id': '83475kj2',
    'people-desuka': 'robots'
    # 如果还有其他的headers，你可以在这里添加
}

distributeUrl= 'http://localhost:8087/gateway/distribute/openAI/v1/chat/completions'
# 发送POST请求
response = requests.post(distributeUrl, headers=headers, data=json.dumps(data))
res = json.loads(response.text)
response2= res['data']
last={
                "total_tokens": response2["usage"]["total_tokens"],
                "completion_tokens": response2["usage"]["completion_tokens"],
                "content": response2['choices'][0]["message"]["content"],
            }
print(last);
# print(response)