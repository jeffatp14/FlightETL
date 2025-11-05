from argparse import ArgumentParser

def parser():
    parser = ArgumentParser(description='Directory Name')
    parser.add_argument('--job_id', type=str, help='Enter job id')
    args = parser.parse_args()

    return args