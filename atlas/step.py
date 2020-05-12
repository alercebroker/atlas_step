from apf.core.step import GenericStep
from apf.producers import KafkaProducer

import logging
import pandas as pd
import numpy as np

from apf.db.sql import get_or_create, get_session
from apf.db.sql.models import Classification, Classifier, Class, AstroObject, Taxonomy


class Atlas(GenericStep):
    """Verification Description

    Parameters
    ----------
    consumer : GenericConsumer
        Description of parameter `consumer`.
    **step_args : type
        Other args passed to step (DB connections, API requests, etc.)

    """

    def __init__(self, consumer=None, config=None, level=logging.INFO, **step_args):

        if self.config.get("PRODUCER_CONFIG", None):
            self.producer = KafkaProducer(self.config["PRODUCER_CONFIG"])
        else:
            self.producer = None

        self.session = get_session(config["DB_CONFIG"])

    def execute(self, message):
        pass