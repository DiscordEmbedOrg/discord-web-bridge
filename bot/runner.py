import asyncio
from autobahn.asyncio.wamp import ApplicationRunner
import sys
import time
from bot.component import Component
import ssl


class Runner:
    """
    Create a crossbar service
    """
    def __init__(self, crossbarConfig, component):
        self._config = crossbarConfig
        self._component = component

    def setup_runner(self):
        runner = ApplicationRunner(**self._config, ssl=ssl.SSLContext())
        return runner

    @staticmethod
    def check_event_loop():
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            asyncio.set_event_loop(asyncio.new_event_loop())

    def reconnect(self):
        """
        Handle reconnect logic if connection to crossbar is lost
        """
        connect_attempt = 0
        max_retries = 0  # 0 = infinite
        runner = self.setup_runner()
        while True:
            connect_attempt += 1
            if connect_attempt == max_retries:
                print("Max retries reached; stopping service")
                sys.exit(1)

            print("Waiting 5 seconds")
            time.sleep(5)
            self.check_event_loop()
            try:
                runner.run(self._component)
            except RuntimeError as error:
                print(error)
            except ConnectionRefusedError as error:
                print(error)
            except ConnectionError as error:
                print(error)
            except KeyboardInterrupt:
                print("User initiated shutdown")
                asyncio.get_event_loop().stop()
                sys.exit(1)
            finally:
                pass

    def start(self, start_loop=True):
        """
        Start a crossbar service
        """
        runner = self.setup_runner()
        if start_loop:
            try:
                runner.run(self._component)
            except KeyboardInterrupt:
                print("User initiated shutdown")
                asyncio.get_event_loop().stop()
                sys.exit(1)
            self.check_event_loop()
            self.reconnect()
        else:
            return runner.run(self._component, start_loop=False)

if __name__ == '__main__':
    config = {
        "crossbar": {
            "url": "wss://crosku.herokuapp.com/ws",
            "realm": "realm1"
        }
    }

    runner = Runner(config["crossbar"], Component)
    runner.start()