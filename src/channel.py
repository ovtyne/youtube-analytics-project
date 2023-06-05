import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.__channel_id = channel_id
        self.channel = Channel.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/{self.channel['items'][0]['snippet']['customUrl']}/{channel_id}"
        self.video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.subscriber_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.view_count = int(self.channel['items'][0]['statistics']['viewCount'])

    def __str__(self):
        """возвращает название и ссылку на канал по шаблону `<название_канала> (<ссылка_на_канал>)`"""
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        """складывает два канала между собой по кол-ву подписчиков"""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """вычитает два канала между собой по кол-ву подписчиков"""
        return other.subscriber_count - self.subscriber_count

    def __lt__(self, other):
        """сравнивает два канала между собой по кол-ву подписчиков (меньше = True)"""
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """сравнивает два канала между собой по кол-ву подписчиков (меньше или равно = True)"""
        return self.subscriber_count <= other.subscriber_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(
            json.dumps(self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute(), indent=2,
                       ensure_ascii=False))

    def to_json(self, filename):
        """сохраняет информацию о канале в файл filename"""
        with open(filename, "w") as file:
            json.dump(self.channel, file, indent=2)

    @property
    def channel_id(self):
        """возвращает id канала"""
        return self.channel_id

    @classmethod
    def get_service(cls):
        """возвращает экземпляр класса канал"""
        return cls.youtube
