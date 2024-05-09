import argparse
from anime_up_updater.utils.logger import logger
from anime_up_updater.functions import scraper
from anime_up_updater.functions.filter import process
import json
import os
from pymongo import MongoClient


def store_in_db(data, db_conn_str, database_name, collection_name):
    """Store anime list in Mongo database. In case database_name and collection_name are not passed
    The default one will be used: [database='anime_up'][collection=`airing_anime`]

    Args:
        data (_type_): airing anime dictionary
        db_conn_str (_type_): connection string to connect the database
        database_name (_type_): database name
        collection_name (str, optional): collection name where to store data. 
    """
    database_name = database_name if database_name else "anime_up"
    collection_name = collection_name if collection_name else "airing_anime"
    logger.info(
        f"Storing data in mongo collection `{collection_name}` at: {db_conn_str}/{database_name}")
    # Connect to MongoDB
    client = MongoClient(db_conn_str)
    # Access a database
    db = client[database_name]
    # Access a collection (create it if it doesn't exist)
    collection = db[collection_name]
    # Insert the array of dictionaries into the collection
    collection.insert_many(data)
    # Close the connection
    client.close()
    logger.info(
        f"Stored #{len(data)} data into mongo")


def store_as_json(out_path, data):
    """Store the data in a certain file specified in input

    Args:
        out_path (_type_): path to the file. The name of the file can be specified or not. In case its not then it 
        will be setted by default as `airing_anime.json`
        data (_type_): airing anime dictionary
    """
    if ".json" not in out_path:
        out_path = os.path.join(
            out_path, "airing_anime.json")
    # Store the JSON response in the output file
    with open(out_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"File stored at: {out_path}")


def main():
    print("Welcome to anime parser")

    parser = argparse.ArgumentParser(description='Description of your script')
    parser.add_argument('--db-conn-str', type=str,
                        help='Path to the mongo db where to store the data')
    parser.add_argument('--database', type=str,
                        help='Database name in case of db storage')
    parser.add_argument('--collection', type=str,
                        help='Collection name in case of db storage')
    parser.add_argument('--output-file', type=str,
                        help='Path to the output file to store the data')
    parser.add_argument(
        '--filter-result', help='Custom filter data (with model:Anime class)')
    parser.add_argument(
        '--debug-mode', help='Enable debug mode', action='store_true')

    # Parse the arguments
    args = parser.parse_args()

    if args.debug_mode:
        import ptvsd
        ptvsd.enable_attach(address=('localhost', 5678))
        ptvsd.wait_for_attach()

    # Scrape content
    airing_anime = scraper.scrape_all()

    if args.filter_result:
        print("[v] Filter for results is enabled..")
        airing_anime = process(airing_anime)

    # Check which options are selected
    if args.db_conn_str:
        store_in_db(airing_anime, args.db_conn_str,
                    args.database, args.collection)
    if args.output_file:
        store_as_json(args.output_file, airing_anime)
    else:
        print("No action selected for storing the obtained data..")

    print("Process finished successfully")


if __name__ == "__main__":
    main()
