from tools.config import Config
from tools.worker import self_play
from tools.worker import optimize
from dotenv import load_dotenv, find_dotenv
import os
import sys
from tools.lib.logger import setup_logger


def setup(config: Config, args):
    config.opts.new = args.new
    if args.total_step is not None:
        config.trainer.start_total_steps = args.total_step
    config.resource.create_directories()
    setup_logger(config.resource.main_log_path)


if find_dotenv():
    load_dotenv(find_dotenv())

_PATH_ = os.path.dirname(os.path.dirname(__file__))

if _PATH_ not in sys.path:
    sys.path.append(_PATH_)

config = Config(config_type="normal")
setup(config, args)

# self_play.start(config)
optimize.start(config)
