import requests
from anime_up_updater.utils.logger import logger
from anime_up_updater.config.constants import graphql_query
import json
from anime_up_updater.functions.times import get_previous_monday_timestamp, get_next_sunday_timestamp, timestamp_to_datetime
import os
from datetime import datetime
import time

# Set the timeout value (in seconds)
timeout = 10000


def scrape_all(force_download=False):
    week_start = get_previous_monday_timestamp()
    week_end = get_next_sunday_timestamp()

    actual_day_start = datetime.fromtimestamp(
        week_start).strftime('%d')
    actual_day_end = datetime.fromtimestamp(
        week_end).strftime('%d')
    actual_month = datetime.now().month
    actual_year = datetime.now().year

    #  check if already available
    stored_file_path = f"./anime_up_updater/res/airing_anime_list_{actual_day_start}-{
        actual_day_end}_{actual_month}_{actual_year}.json"
    if not os.path.exists(stored_file_path):
        already_download = False
    else:
        print(f"The airing list already exists at: {stored_file_path}.")
        already_download = True

    if force_download or not already_download:
        has_next = True
        page_num = 0
        airing_anime = []
        while has_next:
            print("Actual anime list: ", len(airing_anime))
            has_next, data_page = scrape_single_page(
                w_start=week_start,
                w_end=week_end,
                page=page_num)
            airing_anime.extend(data_page)
            # Sleep for 5 seconds
            time.sleep(5)
            page_num += 1
        print("Storing for future usage")
        # Store the JSON response in the output file
        with open(stored_file_path, "w") as json_file:
            json.dump(airing_anime, json_file, indent=4)
    else:
        # Open the JSON file and load its contents into a variable
        with open(stored_file_path, "r") as json_file:
            airing_anime = json.load(json_file)

    return airing_anime


def scrape_single_page(w_start, w_end, page):
    logger.debug(
        f"Querying anime for start_date: {timestamp_to_datetime(w_start)} -- {w_start}")
    logger.debug(
        f"Querying anime for end_date: {timestamp_to_datetime(w_end)} -- {w_end}")
    logger.debug(f"Querying page: {page}")

    # GraphQL query and variables
    graphql_variables = {
        "weekStart": get_previous_monday_timestamp(),
        "weekEnd": get_next_sunday_timestamp(),
        "page": page
    }

    # Prepare the request headers
    headers = {
        "Content-Type": "application/json"
    }

    # Prepare the request payload
    payload = {
        "query": graphql_query,
        "variables": graphql_variables
    }

    # Send the POST request
    response = requests.post(
        "https://graphql.anilist.co/", headers=headers, json=payload, timeout=timeout)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response text as JSON
        response_json = response.json()
        has_next = response_json['data']['Page']['pageInfo']['hasNextPage']
        data_page = response_json['data']['Page']['airingSchedules']
        logger.debug(f"Found: {len(data_page)} elements")

    else:
        # Print an error message if the request failed
        raise RuntimeError(f"Failed to fetch data: {response.status_code}")
    logger.debug(f"---------------------------------")
    return has_next, data_page


# scrape_all()
# has_finished, result = scrape_single_page(1, store_result=True)
# logger.info(f'#{len(result)} Anime returned. HasNext: {has_finished}')
