class PlayList:
    """Класс плей-листа"""
    def __init__(self, playlist_id):
        """инициализируется _id_ плейлиста"""
        self.id = playlist_id
        self.title = ''
        self.url = ''
        self.total_duration = None #datetime.timedelta

    def total_seconds(self):
        pass

    def show_best_video(self):
        pass

