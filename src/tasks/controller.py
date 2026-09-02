from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException


def create_task(body: TaskSchema, db: Session):
    data = body.model_dump()
    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"],
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
    # return {"status": "Task created successfully", "data": new_task}


def get_task(db: Session):
    tasks = db.query(TaskModel).all()
    return tasks
    # return {"status": "Task getting successfully", "data": tasks}


def get_one_task(task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        return HTTPException(404, detail="task id is incorrect")
    return one_task
    # return {"status": "Task fetched successfully", "data": one_task}


def update_task(body: TaskSchema, task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="task id is incorrect")

    # one_task.title = body.title
    # one_task.description = body.description
    # one_task.is_completed = body.is_completed
    #    ==> poor way for huge data <==

    body = body.model_dump()
    for key, value in body.items():
        setattr(one_task, key, value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    return one_task
    # return {"status": "Task updated successfully", "updated data": one_task}


def delete_task(task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="task id is incorrect")
    db.delete(one_task)
    db.commit()
    return None
    # return {"status": "Task deleted successfully", "deleted data": one_task}
