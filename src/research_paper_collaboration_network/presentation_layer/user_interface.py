"""Implements the applicatin user interface."""

from research_paper_collaboration_network.application_base import ApplicationBase
from research_paper_collaboration_network.service_layer.app_services import AppServices
import inspect
import json
import sys
from prettytable import PrettyTable

class UserInterface(ApplicationBase):
    """UserInterface Class Definition."""
    def __init__(self, config:dict)->None:
        """Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
        self.app_services = AppServices(config)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')






    def display_menu(self):
        print(f'\n\n\t\tResearch Paper Network')
        print()
        print(f'\t1.List of authors')
        print(f'\t2.List of papers')
        print(f'\t3.List of authors and their papers')
        print(f'\t6.Exit')
    def process_menu_choice(self):
        menu_choice = input("\tSelection: ")
        match menu_choice[0]:
            case '1': self.list_authors()
            case '2': self.list_papers()
            case '3': self.list_authors_with_papers()
            case '6': sys.exit()

    def list_authors(self):
        try:
            results = self.app_services.get_all_authors()
            table = PrettyTable()
            table.field_names = ['ID', 'First Name', 'Middle Name', 'Last Name']
            for row in results:
                table.add_row( [row[0], row[1], row[2], row[3]])
            print(table)

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

    def list_papers(self):
        try:
            results = self.app_services.get_all_papers()
            table = PrettyTable()
            table.field_names = ['ID', 'Title', 'Year', 'Catergory']
            for row in results:
                table.add_row( [row[0], row[1], row[2], row[3]])
            print(table)

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

    def list_authors_with_papers(self):
        try:
            results = self.app_services.get_all_authors_with_papers()
            table = PrettyTable()
            table.field_names = ['ID', 'First Name', 'Middle Name', 'Last Name', 
            'Paper Title', 'Contribution']
            for row in results:
                table.add_row( [
                    row[0], row[1], row[2], row[3],row[4], f"{row[5]}%" #contribution
                                ])
            print(table)

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')




    def start(self):
        """Start main user interface."""
        while True:
            self.display_menu()
            self.process_menu_choice()
    