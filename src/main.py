"""Entry point for the Employee Training Application."""

import json
from argparse import ArgumentParser
from research_paper_collaboration_network.presentation_layer.user_interface import UserInterface
from research_paper_collaboration_network.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
from research_paper_collaboration_network.service_layer.app_services import AppServices 


def main():
	"""Entry point."""
	args = configure_and_parse_commandline_arguments()

	if args.configfile:
		config = None
		with open(args.configfile, 'r') as f:
			config = json.loads(f.read())

	ui = UserInterface(config)
	ui.start()
	#db = MySQLPersistenceWrapper(config)
	#results = db.select_all_authors()
	#print(results)	


	app_services = AppServices(config)
	results = app_services.get_all_authors()

	# for row in results:
#		print(f'{row[0]} {row[1]} {row[2]} {row[3]}')		

#	print()
	#print(f'{app_services.get_all_authors_as_json()}')
		


def configure_and_parse_commandline_arguments():
	"""Configure and parse command-line arguments."""
	parser = ArgumentParser(
	prog='main.py',
	description='Start the application with a configuration file.',
	epilog='POC: Your Name | your@email')

	parser.add_argument('-c','--configfile',
					help="Configuration file to load.",
					required=True)
	args = parser.parse_args()
	return args



if __name__ == "__main__":
	main()