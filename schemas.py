from pydantic import BaseModel,Field

# 用户输入模型
class StudentCreate(BaseModel):
    name: str = Field(...,min_length=2,max_length=5,description="学生姓名")
    age : int = Field(...,lt=100,gt=18,description="学生年龄")
    email : str = Field(...,min_length=7,max_length=21,description="学生邮箱")

# 数据库返回模型
class StudentResponse(BaseModel):
    id : int =Field(...,description="学生ID")
    name : str = Field(...,min_length=2,max_length=5,description="学生姓名")
    age : int = Field(...,lt=100,gt=18,description="学生年龄")
    email : str = Field(...,min_length=7,max_length=21,description="学生邮箱")

# 用户修改信息模型
class StudentUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=5, description="学生姓名")
    age: int = Field(..., lt=100, gt=18, description="学生年龄")
    email: str = Field(..., min_length=7, max_length=21, description="学生邮箱")
