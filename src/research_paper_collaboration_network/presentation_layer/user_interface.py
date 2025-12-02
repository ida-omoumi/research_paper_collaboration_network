"""Implements the applicatin user interface."""

from research_paper_collaboration_network.application_base import ApplicationBase
from research_paper_collaboration_network.service_layer.app_services import AppServices
import inspect
import json
import sys
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
from prettytable.colortable import Theme
print([t for t in dir(Theme) if t.isupper()])


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
        print(f'\ta.List of authors')
        print(f'\tb.List of papers')
        print(f'\tc.List of authors and their papers')
        print(f'\td.Add Author')
        print(f'\te.Update Author')
        print(f'\tf.Delete Author')
        print(f'\tg.Add Paper')
        print(f'\th.Update Paper')
        print(f'\ti.Delete Paper')
        print(f'\tj.Link Author to Paper')
        print(f'\tk.Update Author-Paper Link')
        print(f'\tl.Delete Author-Paper Link')
        print(f'\tm.List Authors Sorted by Contribution')
        print(f'\tq.Exit')
    def process_menu_choice(self):
        menu_choice = input("\tSelection: ")
        match menu_choice[0]:
            case 'a': self.list_authors()
            case 'b': self.list_papers()
            case 'c': self.list_authors_with_papers()
            case 'd': self.add_author()
            case 'e': self.update_author_ui()
            case 'f': self.delete_author_ui()
            case 'g': self.add_paper()
            case 'h': self.update_paper_ui()
            case 'i': self.delete_paper_ui()
            case 'j': self.link_author_to_paper_ui()
            case 'k': self.update_author_paper_link_ui()
            case 'l': self.delete_author_paper_link_ui()
            case 'm': self.view_authors_by_contribution_ui()
            case 'q': sys.exit()
            case _: print(f'\n\n\t\t!!! Invalid Selection !!!')
            

    def list_authors(self):
        try:
            results = self.app_services.get_all_authors()
            table = ColorTable(theme=Themes.EARTH)
            table.field_names = ['ID', 'First Name', 'Middle Name', 'Last Name']
            for row in results:
                table.add_row( [row[0], row[1], row[2], row[3]])
            print(table)

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



    def list_papers(self):
        try:
            results = self.app_services.get_all_papers()
            table = ColorTable(theme=Themes.EARTH)
            table.field_names = ['ID', 'Title', 'Year', 'Catergory']
            for row in results:
                table.add_row( [row[0], row[1], row[2], row[3]])
            print(table)

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



    def list_authors_with_papers(self):
        try:
            results = self.app_services.get_all_authors_with_papers()
            table = ColorTable(theme=Themes.EARTH)
            table.field_names = ['ID', 'First Name', 'Middle Name', 'Last Name', 
            'Paper Title', 'Contribution']
            for row in results:
                table.add_row( [
                    row[0], row[1], row[2], row[3],row[4], f"{row[5]}%" #contribution
                                ])
            print(table)

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


    def add_author(self):
        first = input(f"\n\n\t\tFirst name: ")
        middle = input(f"\n\n\t\tMiddle name (optional): ")
        last = input(f"\n\n\t\tLast name: ")

        new_id = self.app_services.create_author(first, middle, last)
        if new_id:
            print(f"\n\n\t\tAuthor added with ID {new_id}")
        else:
            print(f"\n\n\t\tError adding author.")



    def update_author_ui(self):
        author_id = input(f"Enter author ID to update: ")
        first = input(f"New first name: ")
        middle = input(f"New middle name: ")
        last = input(f"New last name: ")

        rows = self.app_services.update_author(author_id, first, middle, last)
        if rows > 0:
            print(f"\n\n\t\tAuthor updated successfully.")
        else:
            print(f"\n\n\t\tNo author updated (ID may not exist).")



    def delete_author_ui(self):
        author_id = input(f"\n\n\t\tEnter author ID to delete: ")

        rows = self.app_services.delete_author(author_id)
        if rows > 0:
            print(f"\n\n\t\tAuthor deleted successfully.")
        else:
            print(f"\n\n\t\tAuthor not found.")
 




    def add_paper(self):
        title = input(f"Paper title: ")
        year = input(f"Publication year: ")
        category = input(f"Category: ")

        if not year.isdigit():
            print(f"\n\n\t\tYear must be a number.")
            return

        new_id = self.app_services.create_paper(title, int(year), category)
        if new_id:
            print(f"\n\n\t\tPaper added with ID {new_id}")
        else:
            print(f"\n\n\t\tError adding paper.")



    def update_paper_ui(self):
        paper_id = input(f"\n\n\t\tEnter paper ID to update: ")
        title = input(f"\n\n\t\tNew paper title: ")
        year = input(f"\n\n\t\tNew publication date (YYYY): ")
        category = input(f"\n\n\t\tNew category: ")

        if not year.isdigit():
            print(f"\n\n\t\tYear must be a number.")
            return

        rows = self.app_services.update_paper(paper_id, title, int(year), category)
        if rows > 0:
            print(f"\n\n\t\tPaper updated successfully.")
        else:
            print(f"\n\n\t\tNo paper updated (ID may not exist).")



    def delete_paper_ui(self):
        paper_id = input(f"\n\n\t\tEnter paper ID to delete: ")

        rows = self.app_services.delete_paper(paper_id)
        if rows > 0:
            print(f"\n\n\t\tPaper deleted successfully.")
        else:
            print(f"\n\n\t\tPaper not found.")





    def link_author_to_paper_ui(self):
        author_id = input(f"\n\n\t\tEnter Author ID: ")
        if not author_id.isdigit():
            print(f"\n\n\t\tInvalid Author ID. Must be a number.")
            return
        author_id = int(author_id)
        
        paper_id = input(f"\n\n\t\tEnter Paper ID: ")
        if not paper_id.isdigit():
            print(f"\n\n\t\tInvalid Paper ID. Must be a number.")
            return
        author_id = int(paper_id)
        
        contribution = input(f"\n\n\t\tContribution percentage (0-100): ").replace("%", "")

        if not contribution.isdigit():
            print(f"\n\n\t\tContribution must be a number.")
            return
        
        contribution = int(contribution)
        
        new_id = self.app_services.link_author_to_paper(author_id, paper_id, contribution)

        if new_id:
            print(f"\n\n\t\tAuthor successfully linked to paper!")
        else:
             print(f"\n\n\t\tError linking.")






    def update_author_paper_link_ui(self):
        author_id = input(f"\n\n\t\tEnter Author ID: ")
        paper_id = input(f"\n\n\t\tEnter Paper ID: ")

        if not (author_id.isdigit() and paper_id.isdigit()):
            print(f"\n\n\t\tInvalid Author or Paper ID. Must be a number.")
            return
            
        author_id = int(author_id)
        paper_id = int(paper_id)

        contribution = input(f"\n\n\t\tNew Contribution percentage (0-100): ")

        if not contribution.isdigit():
            print(f"\n\n\t\tContribution must be a number.")
            return
        
        contribution = int(contribution)
        
        rows = self.app_services.link_author_to_paper(author_id, paper_id, contribution)

        if rows > 0:
            print(f"\n\n\t\tSuccessfully updated!")
        else:
            print(f"\n\n\t\tError updating.")




    def update_author_paper_link_ui(self):
        author_id = input(f"\n\n\t\tEnter Author ID: ")
        paper_id = input(f"\n\n\t\tEnter Paper ID: ")

        if not (author_id.isdigit() and paper_id.isdigit()):
            print(f"\n\n\t\tInvalid Author or Paper ID. Must be a number.")
            return
            
        author_id = int(author_id)
        paper_id = int(paper_id)

        contribution = input(f"\n\n\t\tNew Contribution percentage (0-100): ")

        if not contribution.isdigit():
            print(f"\n\n\t\tContribution must be a number.")
            return
        
        contribution = int(contribution)
        
        rows = self.app_services.link_author_to_paper(author_id, paper_id, contribution)

        if rows > 0:
            print(f"\n\n\t\tSuccessfully updated!")
        else:
            print(f"\n\n\t\tError updating.")





    def delete_author_paper_link_ui(self):
        author_id = input(f"\n\n\t\tEnter Author ID: ")
        paper_id = input(f"\n\n\t\tEnter Paper ID: ")

        if not (author_id.isdigit() and paper_id.isdigit()):
            print(f"\n\n\t\tInvalid Author or Paper ID. Must be a number.")
            return
            
        author_id = int(author_id)
        paper_id = int(paper_id)
        
        rows = self.app_services.delete_author_paper_link(author_id, paper_id)

        if rows > 0:
            print(f"\n\n\t\tSuccessfully deleted!")
        else:
            print(f"\n\n\t\tError deleting.")



    def view_authors_by_contribution_ui(self):
        paper_id = input(f"\n\n\t\tEnter Paper ID: ")
        if not paper_id.isdigit():
            print(f"\n\n\t\tInvalid Paper ID. Must be a number.")
            return
            
        paper_id = int(paper_id)

        paper_info =  self.app_services.get_paper_by_id(paper_id)
        if not paper_info:
            print(f"\n\n\t\tPaper not found.")
            return
        
        """paper id, title, year, category"""
        paper_title = paper_info[0][1]

        results = self.app_services.get_authors_by_contribution(paper_id)
        if not results:
            print(f"No authors linked to this paper.")
            return
        
        print(f"\nPaper {paper_id}: {paper_title}")
        print("Authors ordered by contribution:\n")

        from prettytable import PrettyTable

        table = ColorTable(theme=Themes.LAVENDER)
        table.field_names = ['Author ID', 'First Name', 'Middle Name', 'Last Name', 'Contribution %']

        for row in results:
            table.add_row([
            row[0], row[1], row[2], row[3], f"{row[4]}%"
        ])
            

        print(table)
            
        










    def start(self):
        """Start main user interface."""
        while True:
            self.display_menu()
            self.process_menu_choice()
    