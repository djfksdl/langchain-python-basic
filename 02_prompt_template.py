from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 평가를 위한 프롬프트 템플릿을 정의합니다. 사용자의 리뷰를 기반으로 점수 범위를 정하템플릿을 작성합니다.
prompt_template = "이 음식 리뷰 '{review}'에 대해 '{rating1}'점부터 '{rating2}'점까지의 평가를 해주세요."
prompt = PromptTemplate(
    input_variables=["review", "rating1", "rating2"], template=prompt_template
)

# temperature 속성을 설정하여, 낮은 값은 보다 일관된 결과를, 높은 값은 다양한 결과를 생성하도록 합니다.
openai = ChatOpenAI(model="gpt-3.5-turbo",
                    api_key=OPENAI_API_KEY, temperature=0.7)

# | 기호를 사용하여 프롬프트와 llm을 연결할 수 있습니다.(체인으로 엮음)
chain = prompt | openai # LCEL 이란걸 알아야함. |로 묶어준다.

# 사용자의 리뷰에 대한 평가를 요청합니다.
try:
    response = chain.invoke({ # 키 : 벨류 형태로 떄리면 결과를 받을 수 있다. 
        "review": "사과네 피자 치킨을 전부 남겼습니다!", # 일부러 사과를 씀. 이름인지 제대로 인식할수있는지 봄.
        "rating1": "1",
        "rating2": "5"
    })
    print(f"평가 결과: {response}") 
except Exception as e:
    print(f"Error: {e}")
