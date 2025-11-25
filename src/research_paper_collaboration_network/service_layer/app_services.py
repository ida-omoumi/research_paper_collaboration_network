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

    def get_all_papers(self)->List:
        """Returns a list of papers from the persistence layer."""

        try:
            results = self.DB.select_all_papers()
            return results
        
        except Exception as e:
            self._logger.log_error(f'{inspect. currentframe().f_code.co_name}:It works!')

    def get_all_authors_with_papers(self)->List:
        """Returns joined list of authors and their papers."""

        try:
            results = self.DB.select_all_authors_with_papers()
            return results
        
        except Exception as e:
            self._logger.log_error(f'{inspect. currentframe().f_code.co_name}:It works!')


    def create_author(self, first_name, middle_name, last_name):
        try:
            return self.DB.insert_author(first_name, middle_name, last_name)
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

    def update_author(self, author_id, first_name, middle_name, last_name):
        try:
            return self.DB.update_author(author_id, first_name, middle_name, last_name)
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

    def delete_author(self, author_id):
        try:
            return self.DB.delete_author(author_id)
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

    
""" def get_all_authors_as_json(self)->List:
        # Returns a list of authors from the persistence layer.

"""
"""
     try:
            results = self.DB.select_all_authors()
            return json.dumps(results)
    

        except Exception as e:
            self._logger.log_error(f'{inspect. currentframe().f_code.co_name}:It works!')
 """ 