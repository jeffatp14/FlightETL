import yaml
from module.args_parser import parser

def task_load():
    args = parser()
    directory_path = args.job_id
    return directory_path
def config_load(config_path):
     config = yaml.safe_load(open(config_path))
     return config