from anime_up_updater.models.anime import Anime
from anime_up_updater.utils.logger import logger


def filter_dict(input_dict, fields_to_keep):
    # Create a copy of the input dictionary
    filtered_dict = input_dict.copy()

    # Iterate over the keys of the dictionary
    for key in list(filtered_dict.keys()):
        # If the key is not in the list of fields to keep, remove it from the dictionary
        if key not in fields_to_keep:
            del filtered_dict[key]

    return filtered_dict


def process(airing_anime):
    """Obtain a json compatible with the anime_up type:
    {
        "id": 1,
        "name": "tsukimichi - moonlit fantasy",
        "descr": "Makoto Misumi era solo un adolescente medio che all'improvviso fu convocato in un altro mondo come un eroe. 
                    Ma la dea di questo mondo lo definì brutto e gli tolse il suo status di eroe costringendolo a rimanere li 
                    in disparte ai bordi di quel mondo. Cosi' lui decide di vivere la sua esperienza al 100%. Questa e' la storia.",
        "genere": "Isekai",
        "airing_day": "Mon",
        "season": "2",
        "episode": "8",
        "rating": 4.9,
        "follower": 72200
        "website_url": ...,
        "cruncyrol_url": ...
    }
    """
    tv_anime_list = []
    for item in airing_anime:
        if (item['media']['format'] == "TV"):
            tv_anime_list.append(Anime.to_anime(item).to_dict())
    logger.debug(f"Filtered [TV anime] into: #{len(tv_anime_list)} items.")
    return tv_anime_list
