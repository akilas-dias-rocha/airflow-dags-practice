from airflow.sdk import dag, task
from pendulum import datetime

@dag(
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    description="DAG to check data",
    owner="data_engineering",
    tags=["example"],
    max_consecutive_failed_dag_runs=3,
)

def check_dag():
    
    @task.bash
    def create_file():
        return 'echo "Hi there!" >/tmp/dummy'
    
    @task.bash
    def check_file_exists():
        return 'test -f /tmp/dummy'

    @task
    def read_file():
        print(open('/tmp/dummy', 'rb').read())

    create_file() >> check_file_exists() >> read_file()

check_dag()