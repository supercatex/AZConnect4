import argparse

from logging import getLogger

from tools.lib.logger import setup_logger
from tools.config import Config

logger = getLogger(__name__)

CMD_LIST = ['self', 'opt', 'eval', 'play_gui']


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", help="what to do", choices=CMD_LIST)
    parser.add_argument("--new", help="run from new best model", action="store_true")
    parser.add_argument("--type", help="use normal setting", default="normal")
    parser.add_argument("--total-step", help="set TrainerConfig.start_total_steps", type=int)
    return parser


def setup(config: Config, args):
    config.opts.new = args.new
    if args.total_step is not None:
        config.trainer.start_total_steps = args.total_step
    config.resource.create_directories()
    setup_logger(config.resource.main_log_path)


def start():
    parser = create_parser()
    args = parser.parse_args()
    config_type = args.type

    config = Config(config_type=config_type)
    setup(config, args)

    logger.info(f"config type: {config_type}")

    if args.cmd == "self":
        from tools.worker import self_play
        return self_play.start(config)
    elif args.cmd == 'opt':
        from tools.worker import optimize
        return optimize.start(config)
    elif args.cmd == 'eval':
        from tools.worker import evaluate
        return evaluate.start(config)
    elif args.cmd == 'play_gui':
        from tools.play_game import gui
        return gui.start(config)


if __name__ == "__main__":
    config = Config(config_type="normal")

    from tools.worker import self_play
    self_play.start(config)

    from tools.worker import optimize
    optimize.start(config)

    from tools.worker import evaluate
    evaluate.start(config)