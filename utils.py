from langchain.chains.question_answering.map_rerank_prompt import output_parser

from prompt_template import system_template_text,user_template_text
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from xiaohongshu_model import XiaoHongShu

def generate_xiaohongshu(theme,openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system",system_template_text),
        ("user",user_template_text)
    ])
    model = ChatOpenAI(model="deepseek/deepseek-r1:free",api_key=openai_api_key,base_url="https://openrouter.ai/api/v1")
    output_parser = PydanticOutputParser(pydantic_object=XiaoHongShu)       #指定输出格式
    chain = prompt | model | output_parser           #提示 | 模型 | 输出
    result = chain.invoke({
        "parser_instructions":output_parser.get_format_instructions(),  #指定特定输出格式
        "theme":theme
    })                                       #链 传入变量
    return result

#print(generate_xiaohongshu("深度学习","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",))
