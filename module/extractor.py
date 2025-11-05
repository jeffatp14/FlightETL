from pathlib import Path
import pandas as pd
import io
import csv

def extract_source(config_file):
    data_source = Path(__file__).parent.parent / 'source'
    data = f'{data_source}/{config_file}'
    df = pd.read_csv(data)
    # df.info()

    # Malformed CSV read as a quoted text -> resulting column total is just 1
    if len(df.columns) == 1:
        cleaned_lines = []
        with open(data, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                # remove outer quotes only if both ends have them
                if line.startswith('"') and line.endswith('"'):
                    line = line[1:-1]
                # replace double double-quotes with single quotes
                line = line.replace('""', '"')
                cleaned_lines.append(line)

        cleaned_text = "\n".join(cleaned_lines)

        # Use csv.Sniffer to detect delimiter automatically
        dialect = csv.Sniffer().sniff(cleaned_text.split("\n")[0])
        sep = dialect.delimiter if dialect.delimiter else ','

        df = pd.read_csv(io.StringIO(cleaned_text), sep=sep, engine="python")
        # df.info()
    return df

