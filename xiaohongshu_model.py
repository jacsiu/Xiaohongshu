from pydantic import BaseModel, Field
from typing import List
class XiaoHongShu(BaseModel):
    titles:List[str] = Field(description="小红书的五个标题",min_items=1,max_items=10)
    content:str = Field(description="小红书的正文内容")