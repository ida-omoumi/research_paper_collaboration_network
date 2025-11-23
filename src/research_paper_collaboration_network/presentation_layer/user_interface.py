"""Implements the applicatin user interface."""

from research_paper_collaboration_network.application_base import ApplicationBase
from research_paper_collaboration_network.service_layer.app_services import AppServices
import inspect
import json
import sys

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
        print(f'\t1.Author List')
        print(f'\t6.Exit')
    def process_menu_choice(self):
        menu_choice = input("\tSelection")
        match menu_choice[0]:
            case '1': self.list_authors()
            case '6': sys.exit

    def list_authors(self):
        try:
            results = self.app_services.get_all_authors()
            print(results)

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

    def start(self):
        """Start main user interface."""

        self.display_menu()
    