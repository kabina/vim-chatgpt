# vim_gpt_plugin.py

import openai

def chat_gpt(query):
    api_key = "API_KEY"  # 본인의 API 키로 대체
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=query,
        max_tokens=50,  # 원하는 출력 토큰 수 설정
        n = 1  # 생성할 응답 수
    )

    return response.choices[0].text

def chat_gpt_complete():
    current_line = vim.current.line
    prefix = current_line[vim.current.col - 1 :]
    query = current_line[: vim.current.col - 1]

    response = chat_gpt(query)

    vim.current.line = query + response
