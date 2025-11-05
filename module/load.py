from module.log import get_logger
from module.job import sink_config
from sqlalchemy import text
import pandas as pd
import datetime

logging = get_logger()
def load(df, engine):
    df['etl_batch_time'] = datetime.datetime.now()
    key_column = sink_config['key_column']
    schema = sink_config['schema']
    table = sink_config['table']
    method = sink_config['method']
    with engine.begin() as conn:
        if method == "replace":
            # Full refresh
            df.to_sql(table, con=conn, if_exists="replace", index=False)
            logging.info(f"LOAD - Replaced table {table}")

        elif method == "append":
            # Avoid duplicates based on key column
            existing_ids = pd.read_sql(
                text(f"SELECT {key_column} FROM {schema}.{table}"),
                con=conn
            )[key_column].tolist()

            new_df = df[~df[key_column].isin(existing_ids)]
            if not new_df.empty:
                new_df.to_sql(table, con=conn, if_exists="append", index=False)
                logging.info(f"LOAD - Appended {len(new_df)} new rows to {table}")
            else:
                logging.info("LOAD - No new rows to append.")

        elif method == "insert":
            try:
                df.to_sql(table, con=conn, schema=schema, if_exists="append", index=False)
                logging.info(f"LOAD - Inserted {len(df)} rows into {schema}.{table} (no deduplication)")
            except Exception as e:
                logging.error(f"LOAD - Insert failed: {e}")

        else:
            logging.error("LOAD - Method must be either 'append' or 'replace'")
