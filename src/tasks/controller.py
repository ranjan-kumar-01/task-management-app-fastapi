from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.tasks.dtos import TaskSchema
from src.tasks.models import TaskModel


def create_task(body: TaskSchema, db: Session) -> TaskModel:
    """
    Create a new task and save it to the database.
    """
    # Convert the Pydantic model into a dictionary.

    data = body.model_dump()

    # Create a new SQLAlchemy model instance.
    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"],
    )

    try:
        # Add the new task to the current database session.
        db.add(new_task)
        # Save the changes to the database.
        db.commit()
        # Refresh the object so it contains the latest database values
        db.refresh(new_task)
    except Exception:
        # if error occurred after commit(), rollback is useful.
        db.rollback()
        raise

    return new_task


def get_task(db: Session) -> list[TaskModel]:
    # Fetch all task records.
    tasks = db.query(TaskModel).all()
    return tasks


def get_one_task(task_id: int, db: Session) -> TaskModel:
    """
    Return a single task by its ID.
    """

    # Fetch the task using its primary key.
    one_task = db.get(TaskModel, task_id)

    # Stop the request if the task does not exist.
    if not one_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return one_task


def update_task(body: TaskSchema, task_id: int, db: Session) -> TaskModel:
    """
    Update an existing task.
    """

    # Find the task that needs to be updated.
    one_task = db.get(TaskModel, task_id)

    if not one_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    # Convert the Pydantic model into a dictionary.
    data = body.model_dump()

    # Update each field dynamically.
    # This avoids writing a separate assignment for every field.
    for key, value in data.items():
        setattr(one_task, key, value)

    # SQLAlchemy is already tracking one_task, so db.add() is not required here.
    db.commit()

    # Refresh the object with the latest database values.
    db.refresh(one_task)

    return one_task


def delete_task(task_id: int, db: Session) -> None:
    """
    Delete a task by its ID.
    """

    # Find the task that needs to be deleted.
    one_task = db.get(TaskModel, task_id)

    if not one_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    # Mark the task for deletion.
    db.delete(one_task)

    # Save the deletion to the database.
    db.commit()
