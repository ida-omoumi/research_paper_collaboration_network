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
    		f"SELECT authors.id, authors.first_name, authors.middle_name, authors.last_name, "
    		f"papers.paper_title, paper_author_xref.contribution "
   			f"FROM authors "
   		 	f"JOIN paper_author_xref ON authors.id = paper_author_xref.author_id "
   			f"JOIN papers ON papers.id = paper_author_xref.paper_id;"
)

		self.INSERT_AUTHOR = (
    	"INSERT INTO authors (first_name, middle_name, last_name) "
   		"VALUES (%s, %s, %s)"
		)

		self.UPDATE_AUTHOR = (
  		  "UPDATE authors SET first_name=%s, middle_name=%s, last_name=%s "
  		  "WHERE id=%s"
		)

		self.DELETE_AUTHOR = (
  		  "DELETE FROM authors WHERE id=%s"
		)

		self.INSERT_PAPER = (
    		f"INSERT INTO papers (paper_title, publication_year, category) "
   			f"VALUES (%s, %s, %s)"
		)

		self.UPDATE_PAPER = (
  		 	f"UPDATE papers SET paper_title=%s, publication_year=%s, category=%s"
  		  	f"WHERE id=%s"
		)

		self.DELETE_PAPER = (
  			f"DELETE FROM papers WHERE id=%s"
		)
		self.INSERT_AUTHOR_PAPER_LINK = (
    		f"INSERT INTO paper_author_xref (author_id, paper_id, contribution) "
    		f"VALUES (%s, %s, %s);"
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





	def insert_author(self, first_name, middle_name, last_name):
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.INSERT_AUTHOR, ([first_name, middle_name, last_name]))
					connection.commit()

					return cursor.lastrowid
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


	def update_author(self, author_id , first_name, middle_name, last_name):
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.UPDATE_AUTHOR, ([first_name, middle_name, last_name, author_id]))
					connection.commit()
				
					return cursor.rowcount
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


	def delete_author(self, author_id):
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor: 
					cursor.execute(self.DELETE_AUTHOR, ([author_id]))
					connection.commit()
					return cursor.rowcount
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')




	def insert_paper(self, paper_title, publication_year, category):
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.INSERT_PAPER, ([paper_title, publication_year, category]))
					connection.commit()

					return cursor.lastrowid
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



	def update_paper(self, paper_id , paper_title, publication_year, category):
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.UPDATE_PAPER
					, ([paper_title, publication_year, category, paper_id]))
					connection.commit()
				
					return cursor.rowcount
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



	def delete_paper(self, paper_id):
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor: 
					cursor.execute(self.DELETE_PAPER, ([paper_id]))
					connection.commit()
					return cursor.rowcount
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


	def link_author_to_paper(self, author_id, paper_id, contribution):
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor: 
					cursor.execute(
               		self.INSERT_AUTHOR_PAPER_LINK,
                	([author_id, paper_id, contribution]))
					connection.commit()
					return cursor.rowcount
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
