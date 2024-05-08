from typing import List, Dict
import datetime


class Anime:
    def __init__(self, id: int,
                 name: str,
                 descr: str,
                 genere: List,
                 airing_day: int,
                 season: str,
                 episode: str,
                 rating: float,
                 follower: int,
                 website_url: str,
                 crunchyroll_url: str):
        """Anime in the list

        Args:
            id (int): Unique id for the anime
            name (str): Title of the anime in English
            descr (str): Description of the anime
            genere (List): List of the genere of the anime
            airing_day (int): Hiring day of the week
            season (str): Last season or arch aired
            episode (str): Last episode aired
            rating (float): Rating of the anime
            follower (int): Number of follower for the anime
        """
        self._id = id
        self._name = name
        self._descr = descr
        self._genere = genere
        self._airing_day = airing_day
        self._season = season
        self._episode = episode
        self._rating = rating
        self._follower = follower
        self._website_url = website_url
        self._crunchyroll_url = crunchyroll_url

    @classmethod
    def to_anime(cls, anime_dict):
        def to_airing_date(timestamp: int):
            # Convert timestamp to datetime object
            dt_object = datetime.datetime.fromtimestamp(timestamp)
            # Get the day of the week (0: Monday, 1: Tuesday, ..., 6: Sunday)
            day_of_week = dt_object.weekday()
            # Return the abbreviated name of the day of the week
            return ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][day_of_week]
        url_crunchy = None
        url_webpage = None
        for link in anime_dict['media']['externalLinks']:
            if link['site'] == "Crunchyroll":
                url_crunchy = link["url"]
            elif link['site'] == "Official Site":
                url_webpage = link["url"]
        return cls(
            anime_dict['id'],
            anime_dict['media']['title']['english'],  # name
            anime_dict['media']['description'],  # descr
            anime_dict['media']['genres'],  # genere
            to_airing_date(anime_dict['airingAt']),  # airing_day
            None,  # season
            anime_dict['episode'],  # episode
            # rating
            anime_dict['media']['averageScore'] / \
            10 if anime_dict['media']['averageScore'] else None,
            anime_dict['media']['popularity'],   # follower
            url_webpage,   # url official webpage
            url_crunchy   # url official crunchyroll page
        )

    @property
    def name(self):
        return self._name

    @property
    def descr(self):
        return self._descr

    @property
    def genere(self) -> List:
        return self._genere

    @property
    def airing_day(self):
        return self._airing_day

    @property
    def season(self):
        return self._season

    @property
    def episode(self):
        return self._episode

    @property
    def rating(self):
        return self._rating

    @property
    def follower(self):
        return self._follower

    @property
    def website_url(self):
        return self._website_url

    @property
    def crunchyroll_url(self):
        return self._crunchyroll_url

    def to_dict(self) -> Dict:
        return {
            "id": self._id,
            "name": self._name,
            "descr": self._descr,
            "genere": self._genere,
            "airing_day": self._airing_day,
            "season": self._season,
            "episode": self._episode,
            "rating": self._rating,
            "follower": self._follower,
            "web_page": self.website_url,
            "cruncyroll_page": self._crunchyroll_url,
        }
