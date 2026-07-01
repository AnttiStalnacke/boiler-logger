from pathlib import Path
from boiler_logger import BoilerLogger
import logging

LOG_FOLDER = Path(__file__).parent.resolve() / "log"
LOG_FILE_PATH = LOG_FOLDER / "boiler_logger.log"
logger = logging.getLogger(__name__)

def main():

    # Create log folder if it does not exist
    LOG_FOLDER.mkdir(parents=True, exist_ok=True)
    
    # Setup main logging here
    logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    logger.info("============== Program started Initializing boiler logger ==============")
    logger.info("Initializing boiler logger")
    bl = BoilerLogger(LOG_FOLDER)
    logger.info("Running boiler logger")
    bl.run()


if __name__ == "__main__":
    main()