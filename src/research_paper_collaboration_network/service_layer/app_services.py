"""Implements AppServices Class."""

from research_paper_collaboration_network.application_base import ApplicationBase
from research_paper_collaboration_network.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
import inspect
from typing import List
import json

class AppServices(ApplicationBase):
    """AppServices Class Definition."""
    def __init__(self, config:dict)->None:
        self.config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__,
                         logfile_prefix_name=self.META["log_prefix"])
        self.DB = MySQLPersistenceWrapper(config)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')

    
    def get_all_authors(self)->List:
        """Returns a list of authors from the persistence layer."""

        try:
            results = self.DB.select_all_authors()
            return results
        
        except Exception as e:
            self._logger.log_error(f'{inspect. currentframe().f_code.co_name}:It works!')
    
    def get_all_authors_as_json(self)->List:
        """Returns a list of authors from the persistence layer."""

        try:
            results = self.DB.select_all_authors()
            return json.dumps(results)
    

        except Exception as e:
            self._logger.log_error(f'{inspect. currentframe().f_code.co_name}:It works!')
    