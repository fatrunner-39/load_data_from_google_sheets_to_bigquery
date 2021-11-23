from google.cloud import bigquery
from google.oauth2 import service_account


def load_table_file(file_path, table_id):
    from google.cloud import bigquery
    # Авторизация сервисного аккаунта Google
    credentials = service_account.Credentials.from_service_account_file(
        'warm-melody-332118-4e7d0c4b29ec.json')
    # Создание клиента BigQuery
    client = bigquery.Client(credentials=credentials, project="warm-melody-332118")

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
    )

    # Считывание данных из загруженного файле
    with open(file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)

    job.result()

    # Заполнение таблицы BigQuery
    table = client.get_table(table_id)  # Make an API request.
    print(
        "Loaded {} rows and {} columns to {}".format(
            table.num_rows, len(table.schema), table_id
        )
    )
    return table

if __name__ == "__main__":
    load_table_file("data.csv", "warm-melody-332118.test_dataset.my_data")