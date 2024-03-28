import argparse
from anime_up_updater.utils.logger import logger
from anime_up_updater.functions import scraper
import json


def main():
    parser = argparse.ArgumentParser(description='Description of your script')
    parser.add_argument('-s', '--db_conn_str',
                        help='Path to the db where to store the data')
    parser.add_argument(
        '-o', '--output-file', help='Path to the output file to store the data')

    # Parse the arguments
    args = parser.parse_args()

    # Scrape content
    airing_anime = scraper.scrape_all()

    # Check which options are selected
    if args.db_conn_str:
        logger.info(f"Storing data in database at: {args.db_conn_str}")
    if args.output_file:
        logger.info(f"Storing data in File at: {args.output_file}")
        # Store the JSON response in the output file
        with open(args.output_file, "w") as json_file:
            json.dump(airing_anime, json_file, indent=4)


if __name__ == "__main__":
    main()
