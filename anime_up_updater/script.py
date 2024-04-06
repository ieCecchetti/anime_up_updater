import argparse
from anime_up_updater.utils.logger import logger
from anime_up_updater.functions import scraper
import json
import ptvsd


ptvsd.enable_attach(address=('localhost', 5678))
ptvsd.wait_for_attach()

def store_in_db(db_conn_str, data):
    logger.info(
        f"Storing #{len(data)} data in mongo database at: {db_conn_str}")
    pass


def store_as_json(out_path, data):
    logger.info(f"Storing data in File at: {out_path}")
    # Store the JSON response in the output file
    with open(out_path, "w") as json_file:
        json.dump(data, json_file, indent=4)


def main():
    print("Welcome to anime parser")

    parser = argparse.ArgumentParser(description='Description of your script')
    parser.add_argument('--db_conn_str', type=str,
                        help='Path to the db where to store the data')
    parser.add_argument('--output-file', type=str,
                        help='Path to the output file to store the data')
    # Parse the arguments
    args = parser.parse_args()

    # Scrape content
    airing_anime = scraper.scrape_all()

    # Check which options are selected
    if args.db_conn_str:
        store_in_db(args.db_conn_str, airing_anime)
    if args.output_file:
        store_as_json(args.output_file, airing_anime)
    else:
        print("No action selected for storing the obtained data..")

    print("Process finished successfully")


if __name__ == "__main__":
    main()
