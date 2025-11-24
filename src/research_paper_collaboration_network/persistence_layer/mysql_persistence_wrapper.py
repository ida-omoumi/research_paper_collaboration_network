"""Defines the MySQLPersistenceWrapper class."""

from research_paper_collaboration_network.application_base import ApplicationBase
from mysql import connector
from mysql.connector.pooling import (MySQLConnectionPool)
import inspect
import json
from typing import List

class MySQLPersistenceWrapper(ApplicationBase):
	"""Implements the MySQLPersistenceWrapper class."""

	def __init__(self, config:dict)->None:
		"""Initializes object. """
		self._config_dict = config
		self.META = config["meta"]
		self.DATABASE = config["database"]
		super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')

		# Database Configuration Constants
		self.DB_CONFIG = {}
		self.DB_CONFIG['database'] = \
			self.DATABASE["connection"]["config"]["database"]
		self.DB_CONFIG['user'] = self.DATABASE["connection"]["config"]["user"]
		self.DB_CONFIG['password'] = self.DATABASE["connection"]["config"]["password"]
		self.DB_CONFIG['host'] = self.DATABASE["connection"]["config"]["host"]
		self.DB_CONFIG['port'] = self.DATABASE["connection"]["config"]["port"]

		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: DB Connection Config Dict: {self.DB_CONFIG}')

		# Database Connection
		self._connection_pool = \
			self._initialize_database_connection_pool(self.DB_CONFIG)
		

		# SQL Query Constants

		self.SELECT_ALL_AUTHORS = (
   			f"SELECT authors.id, authors.first_name, authors.middle_name, authors.last_name "
   			f"FROM authors;"
)

		self.SELECT_ALL_PAPERS = (
    		f"SELECT papers.id, papers.paper_title, papers.publication_year, papers.category "
    		f"FROM papers;"
)

		self.SELECT_ALL_AUTHORS_WITH_PAPERS = (
    		"SELECT authors.id, authors.first_name, authors.middle_name, authors.last_name, "
    		"papers.paper_title, paper_author_xref.contribution "
   			 "FROM authors "
   		 	"JOIN paper_author_xref ON authors.id = paper_author_xref.author_id "
   			 "JOIN papers ON papers.id = paper_author_xref.paper_id;"
)



	
	




	# MySQLPersistenceWrapper Methods

	def select_all_authors(self)->List:
		"""Returns a list of authors."""
		cursor = None
		results = None
		
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_AUTHORS)
					results = cursor.fetchall()
		
			return results

		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')
			
	def select_all_papers(self)->List:
		"""Returns a list of papers."""
		cursor = None
		results = None
		
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_PAPERS)
					results = cursor.fetchall()
		
			return results

		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



	def select_all_authors_with_papers(self)->List:
		"""Returns joined list of authors and their papers."""
		cursor = None
		results = None
		
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_AUTHORS_WITH_PAPERS)
					results = cursor.fetchall()
		
			return results

		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')







		##### Private Utility Methods #####

	def _initialize_database_connection_pool(self, config:dict)->MySQLConnectionPool:
		"""Initializes database connection pool."""
		try:
			self._logger.log_debug(f'Creating connection pool...')
			cnx_pool = \
				MySQLConnectionPool(pool_name = self.DATABASE["pool"]["name"],
					pool_size=self.DATABASE["pool"]["size"],
					pool_reset_session=self.DATABASE["pool"]["reset_session"],
					**config)
			self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: Connection pool successfully created!')
			return cnx_pool
		except connector.Error as err:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem creating connection pool: {err}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Check DB cnfg:\n{json.dumps(self.DATABASE)}')
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Problem creating connection pool: {e}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Check DB conf:\n{json.dumps(self.DATABASE)}')
