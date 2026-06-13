from airflow.sdk import dag, task, chain
from pendulum import datetime

@dag(
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    description="A simple DAG example",
    tags=["example"],
    max_consecutive_failed_dag_runs=3,
)

def my_dag():
    
    @task
    def task_a():
        print("Hello from Task A!")

    @task
    def task_b():
        print("Hello from Task B!")

    @task
    def task_c():
        print("Hello from Task C!")

    @task
    def task_d():
        print("Hello from Task D!")

    @task
    def task_e():
        print("Hello from Task E!")

chain(task_a() >> [task_b(), task_c()], [task_d(), task_e()])


my_dag()