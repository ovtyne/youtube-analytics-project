import os

from googleapiclient.discovery import build


class Video:
    """Класс для видео"""
    def __init__(self, video_id):
        """Экземпляр инициализируется по id видео, остальное подтягивается по API"""
        self.video_id = video_id
        api_key: str = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=video_id
                                                    ).execute()
        self.video_title: str = video_response['items'][0]['snippet']['title']  # название видео
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']  # количество просмотров
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']  # количество лайков
        self.comment_count: int = video_response['items'][0]['statistics']['commentCount']  # количество комментариев
        self.url_video = f"https://www.youtube.com/channel/{self.video_id}"  # адрес видео

    def __str__(self):
        """Возвращает наздвание канала"""
        return f"{self.video_title}"


class PLVideo(Video):
    """Класс плейлиста видео"""
    def __init__(self, video_id, playlist_id: str):
        """Инициализируется по id видео и id плей-листа"""
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                                 part='contentDetails',
                                                                 maxResults=50,
                                                                 ).execute()
