import sys
sys.path.append("..")  # Adds higher directory to python modules path.
from bot.runner import Runner
from bot.component import Component
from bot.config import config


if __name__ == '__main__':
    runner = Runner(config["CROSSBAR_APP_RUNNER"], Component)
    runner.start(Component)

