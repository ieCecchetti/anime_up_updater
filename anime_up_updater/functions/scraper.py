import requests
from anime_up_updater.utils.logger import logger
from anime_up_updater.config.constants import graphql_query
import json
from anime_up_updater.functions.times import get_previous_monday_timestamp, get_next_sunday_timestamp, timestamp_to_datetime

# Set the timeout value (in seconds)
timeout = 2000


def scrape_all():
    has_next = True
    page_num = 1
    airing_anime = []
    while has_next:
        has_next, data_page = scrape_single_page(page=page_num)
        airing_anime.extend(data_page)
        page_num += 1

    return airing_anime


def scrape_single_page(page, store_result=False):
    # GraphQL query and variables
    graphql_variables = {
        "weekStart": get_previous_monday_timestamp(),
        "weekEnd": get_next_sunday_timestamp(),
        "page": page
    }
    logger.debug(f"Querying anime for start_date: {
        timestamp_to_datetime(graphql_variables['weekStart'])}")
    logger.debug(f"Querying anime for end_date: {
        timestamp_to_datetime(graphql_variables['weekEnd'])}")
    logger.debug(f"Querying page: {graphql_variables['page']}")
    logger.debug(f"---------------------------------")

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
        if store_result:
            # Store the JSON response in the output file
            with open(f"../res/airing_anime_list_{graphql_variables['weekStart']}_{page}.json", "w") as json_file:
                json.dump(data_page, json_file, indent=4)
    else:
        # Print an error message if the request failed
        raise RuntimeError(f"Failed to fetch data: {response.status_code}")
    return has_next, data_page


# scrape_all()
# has_finished, result = scrape_single_page(1, store_result=True)
# logger.info(f'#{len(result)} Anime returned. HasNext: {has_finished}')
