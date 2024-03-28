import logging

def setup_logger():
    logger = logging.getLogger("dmu")
    logger.setLevel(logging.DEBUG)

    # Create a stream handler and set its level to INFO
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    # Define the log message format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(stream_handler)

    return logger

# Instantiate the logger in the setup_logger function
logger = setup_logger()
logger.info("Setting up logger...")