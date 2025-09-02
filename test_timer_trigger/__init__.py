
import logging

import azure.functions as func


logging.basicConfig(
        level=getattr(logging, "INFO"),
        format="%(message)s",
    )
logger = logging.getLogger()

def main(mytimer: func.TimerRequest):
    logger.info("This is my trigger")

    if mytimer.past_due:
        logger.warning("Timer trigger function is running late")

    logger.info("Timer trigger function started")
