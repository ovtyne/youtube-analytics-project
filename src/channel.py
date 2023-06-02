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
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(
            json.dumps(self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute(), indent=2,
                       ensure_ascii=False))

    def to_json(self, filename):
        with open(filename, "w") as file:
            json.dump(self.channel, file, indent=2)

    @property
    def channel_id(self):
        return self.channel_id

    @classmethod
    def get_service(cls):
        return cls.youtube
