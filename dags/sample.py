from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


def greet():
    print("Hello from PythonOperator!")


def add_numbers(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")
    return result


with DAG(
    dag_id="sample_python_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    greet_task = PythonOperator(
        task_id="greet",
        python_callable=greet,
    )

    add_task = PythonOperator(
        task_id="add_numbers",
        python_callable=add_numbers,
        op_kwargs={"x": 3, "y": 5},
    )

    greet_task >> add_task