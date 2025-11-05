from pathlib import Path
from module.util import config_load
from module.log import get_logger
from module.args_parser import parser

logging = get_logger()
args = parser()
try:
    config_dir = Path(__file__).parent.parent / "configs"
    config_dir = config_dir / args.job_id
    config_dir = config_dir.with_suffix('.yml')

    config_dict = config_load(config_dir)

except Exception as exc:
    logging.error("JOB - Cannot initialize config: " + str(exc))
    raise exc

# Parse all config
transform_config = config_dict['TRANSFORM']
sink_config = config_dict['SINK'][0]