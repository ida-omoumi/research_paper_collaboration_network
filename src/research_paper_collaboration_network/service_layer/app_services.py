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


    
    def create_paper(self, paper_title, publication_year, category):
        try:
            return self.DB.insert_paper(paper_title, publication_year, category)
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')




    def update_paper(self, paper_id, paper_title, publication_year, category):
        try:
            return self.DB.update_paper(paper_id, paper_title, publication_year, category)
            
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')




    def delete_paper(self, paper_id):
        try:
            return self.DB.delete_paper(paper_id)
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



    def link_author_to_paper(self, author_id, paper_id, contribution):
        try:
            return self.DB.link_author_to_paper(author_id, paper_id, contribution)
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')




    def update_author_paper_link(self, author_id, paper_id, contribution):
        try:
            return self.DB.update_author_paper_link(author_id, paper_id, contribution)
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


    def delete_author_paper_link(self, author_id, paper_id):
        try:
            return self.DB.delete_author_paper_link( author_id, paper_id)
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



    def get_authors_by_contribution(self, paper_id):
        try:
            return self.DB.select_authors_by_contribution(paper_id)
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


    def get_paper_by_id(self, paper_id):
        try:
            return self.DB.select_paper_by_id(paper_id)
        except Exception as e:
            self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: {e}")
       



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