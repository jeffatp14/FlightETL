from module.extractor import extract_source
from module.transformer import transform
from module.load import load
from module.client import Postgres
from module.args_parser import parser

if __name__ == "__main__":
    args = parser()

    client = Postgres()
    engine = client.get_engine()

    df = extract_source(args.job_id)
    transformed_df = transform(df)
    load(transformed_df, engine)
    client.close_connection()

