from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from expectations import expectation1, expectation2, expectation3, expectation4, expectation5,check_file

with DAG("expectation_dag", start_date=datetime(2022, 9, 6),
         schedule_interval="@daily", catchup=False) as dag:

    expectation_check_file = PythonOperator(
        task_id="check_file_read",
        python_callable=check_file
    )

    expectation_1 = PythonOperator(
        task_id="expect_values_in_set",
        python_callable=expectation1
    )

    expectation_2 = PythonOperator(
        task_id="expect_mean",
        python_callable=expectation2
    )

    expectation_3 = PythonOperator(
        task_id="expect_min",
        python_callable=expectation3
    )

    expectation_4 = PythonOperator(
        task_id="expect_exist",
        python_callable=expectation4
    )

    expectation_5 = PythonOperator(
        task_id="Expect_unique",
        python_callable=expectation5
    )
expectation_check_file >> [expectation_1, expectation_2, expectation_3, expectation_4, expectation_5]