from module.log import  get_logger
from module.job import transform_config
import pandas as pd
logging = get_logger()
def transform(df):
    col_num = len(df.columns)
    for col in transform_config.get("drop_duplicate", []):
        if col in df.columns:
            df[col] = df.drop_duplicates(subset=[col])
    # assert df['fl_id'].notnull().all(), "Flight ID cannot be null"
    # assert (df['seat_f'] >= 0).all(), "Seat F count cannot be negative"
    is_null = []
    for i in range(len(df.index)):
        null_total = df.iloc[i].isnull().sum()
        if null_total == col_num-1:
            is_null.append(True)
        else:
            is_null.append(False)
    for col in transform_config.get("datetime_columns", []):
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    logging.info("TRANSFORM - Datetime type transformed")
    df['is_null_row'] = is_null
    logging.info("TRANSFORM - Add null row check")

    if transform_config.get("drop_full_null_rows"):
        df = df[df["is_null_row"] != True]
        logging.info("TRANSFORM - Null row dropped")

    return df