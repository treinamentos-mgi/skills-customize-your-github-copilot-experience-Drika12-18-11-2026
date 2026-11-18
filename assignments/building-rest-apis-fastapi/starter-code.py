from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
import uvicorn


class TaskInput(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""
    completed: bool = False


class Task(TaskInput):
    id: int


app = FastAPI(title="Task API")
tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    # TODO: Return all tasks stored in the collection.
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Return the requested task or raise HTTPException with status 404.
    pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput):
    global next_task_id
    # TODO: Create a task, store it, increment next_task_id, and return it.
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput):
    # TODO: Replace an existing task or raise HTTPException with status 404.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Delete an existing task or raise HTTPException with status 404.
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
