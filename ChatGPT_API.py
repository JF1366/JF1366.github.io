# References 
# https://platform.openai.com/docs/api-reference/chat/create
# https://platform.openai.com/docs/guides/chat/introduction

# 方法1：
import openai
import os

def GptTest():
    openai.proxy = "Your proxy"
    openai.api_key = 'Your OPENAI_API_KEY'
    # openai.api_key = os.getenv("OPENAI_API_KEY") # 也可以通过环境变量

    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=input("请输入你的问题:"),
        temperature=1,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    print(response.choices[0].text)


if __name__ == '__main__':
    for x in range(10000):
        GptTest()

# 方法2：
# import requests
#
# proxies = {
#     "http": "Your proxy",
#     "https": "Your proxy"
# }
#
#
# def GPT4API(messages, temperature=0.1):
#     # API接口的URL
#     url = "Your url"
#     api_key = "Your key(It is not OPENAI_API_KEY)"
#
#     # 设置请求头
#     headers = {
#         "Content-Type": "application/json",
#         "api-key": api_key
#     }
#
#     # 请求的数据
#     data = {
#         "messages": messages,
#         "temperature": temperature
#     }
#
#     # 发送POST请求
#     response = requests.post(url=url, headers=headers, json=data, proxies=proxies)
#
#     # 检查响应状态
#     if response.status_code == 200:
#         return response.json()["choices"][0]["message"]["content"].strip()
#     else:
#         print(f"Error: {response.status_code}")
#         print(response.text)
#         return None
#
#
# def get_system_prompt():
#     return "hello"
#
#
# if __name__ == "__main__":
#     print("请输入你的问题: ")
#     print(GPT4API([{"role": "system", "content": get_system_prompt()}], 0))
