from fastapi import FastAPI

from crud import get_students, create_student, get_student_by_id, del_student,update_student

from schemas import StudentResponse, StudentCreate, StudentUpdate

app = FastAPI()


@app.get("/students",response_model=list[StudentResponse])
# response_model 作用：接口返回的数据,应该是一个Student对象做成的列表
def read_students():

    students = get_students()

    return students


@app.post("/students")
def add_student(student: StudentCreate):
    student_id = create_student(
        student.name,
        student.age,
        student.email
    )
    return {
        "message": "创建成功",
        "id": student_id
    }


@app.get("/students/{student_id}",response_model=StudentResponse)
def read_student(student_id:int):

    student = get_student_by_id(student_id)

    return student


@app.delete("/students/{student_id}")
def remove_id(student_id: int):

    result = del_student(student_id)

    if result == 0:
        return {"message":"学生不存在"}

    return {"message":"删除成功"}


@app.put("/students/{student_id}")
def edit_student(student_id:int,student:StudentUpdate):

    result = update_student(
        student_id,
        student.name,
        student.age,
        student.email,

    )

    if result == 0:
        return {"message":"学生不存在"}

    return {"message":"修改成功"}