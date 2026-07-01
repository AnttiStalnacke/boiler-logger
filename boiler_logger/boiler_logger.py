"""Boiler logger
Class is intended to monitor a boiler.

It is written to run on a raspberry Pi 5 and initially it will only log the state changes on a pin which is toggled
when the auger motor is turned on.

It is intended to start automatically upon boot of the raspberry Pi.

Registered triggers trig logging of all sources.

gpiozero and signal seems to be the way to go.
"""
from pathlib import Path
import logging
import datetime

AUGER_PIN = 5 # Pin number of pin toggled
LOG_FOLDER = Path(__file__).parent.resolve() / "log"
DATE_TIME = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
MEAS_LOG_PATH = LOG_FOLDER / f"boiler_measurement_log_{DATE_TIME}.log"
logger = logging.getLogger(__name__)

class BoilerLogger:
    def __init__(self, log_folder):
        logger.info("Initializing boiler logger")

        # Check that a /log folder exists and if not create it
        log_folder.mkdir(parents=True, exist_ok=True)

        # Create a measurement log file (main log file should be created in main)
        self._meas_logger = logging.getLogger("_boiler_meas_logger")
        self._meas_logger.setLevel(logging.INFO)
        self._meas_logger.propagate = False
        if self._meas_logger.handlers: 
            raise ValueError("Meas loggers hander alraedy set")
        logger.info("Meas log handler not set, setting it.")
        handler = logging.FileHandler(MEAS_LOG_PATH)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        self._meas_logger.addHandler(handler)
        self._meas_logger.info("This should be in the meas log.") # Just for testing 

        # Register triggers
        # Register sources
        pass
    def run(self):
        # Enable interrupt on AUGER_PIN and register callback.
        print("Hello from class!")

    def auger_callback(self):
        # Log a line to the log
        pass 