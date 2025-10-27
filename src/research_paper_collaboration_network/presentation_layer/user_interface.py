"""Implements the applicatin user interface."""

from research_paper_collaboration_network.application_base import ApplicationBase
from research_paper_collaboration_network.service_layer.app_services import AppServices
import inspect
import json

class UserInterface(ApplicationBase):
    """UserInterface Class Definition."""
    def __init__(self, config:dict)->None:
        """Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
        self.DB = AppServices(config)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')
        query = 'SELECT * FROM Papers;'
        results = self.DB.query_dosomething(query)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:Query line works!')





    def start(self):
        """Start main user interface."""
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: User interface started!')
        query = 'SELECT * FROM Papers;'
        results = self.DB.query_dosomething(query)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:Query line works!')
        for row in results:
            self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: Row: {row}')