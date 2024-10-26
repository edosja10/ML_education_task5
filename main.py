from datetime import datetime
from abc import ABC, abstractmethod

#Базовый класс для всех медиа-файлов
class MediaFile(ABC):
    def __init__(self, name: str, size: int, created_at: datetime, owner: str):
        self.name = name
        self.size = size
        self.created_at = created_at
        self.owner = owner

    @abstractmethod
    def save(self):
        """Сохранение файла"""
        pass

    @abstractmethod
    def delete(self):
        """Удаление файла"""
        pass

    @abstractmethod
    def convert(self, new_format: str):
        """Конвертация файла"""
        pass

#Класс для аудио-файлов
class AudioFile(MediaFile):
    def __init__(self, name: str, size: int, created_at: datetime, owner: str, duration: int, bitrate: int):
        super().__init__(name, size, created_at, owner)
        self.duration = duration  # Длительность аудио в секундах
        self.bitrate = bitrate  # Битрейт аудио в kbps

    def save(self):
        print(f"Сохранение аудио файла '{self.name}'")

    def delete(self):
        print(f"Удаление аудио файла '{self.name}'")

    def convert(self, new_format: str):
        print(f"Конвертация аудио файла '{self.name}' в формат {new_format}")

    def extract_features(self):
        """Извлечение фич из аудио-файла"""
        print(f"Извлечение фич из аудио файла '{self.name}'")

#Класс для видео-файлов
class VideoFile(MediaFile):
    def __init__(self, name: str, size: int, created_at: datetime, owner: str, resolution: str, framerate: int):
        super().__init__(name, size, created_at, owner)
        self.resolution = resolution  # Разрешение видео, например "1920x1080"
        self.framerate = framerate  # Количество кадров в секунду

    def save(self):
        print(f"Сохранение видео файла '{self.name}'")

    def delete(self):
        print(f"Удаление видео файла '{self.name}'")

    def convert(self, new_format: str):
        print(f"Конвертация видео файла '{self.name}' в формат {new_format}")

    def extract_keyframes(self):
        """Извлечение ключевых кадров"""
        print(f"Извлечение ключевых кадров из видео файла '{self.name}'")

#Класс для файлов изображений
class PhotoFile(MediaFile):
    def __init__(self, name: str, size: int, created_at: datetime, owner: str, resolution: str, color_depth: int):
        super().__init__(name, size, created_at, owner)
        self.resolution = resolution  # Разрешение фото, например "4000x3000"
        self.color_depth = color_depth  # Глубина цвета, например 24 бита

    def save(self):
        print(f"Сохранение фото файла '{self.name}'")

    def delete(self):
        print(f"Удаление фото файла '{self.name}'")

    def convert(self, new_format: str):
        print(f"Конвертация фото файла '{self.name}' в формат {new_format}")

#Поддержка хранения файлов в разных хранилищах
class CloudStorageMixin:
    def save(self):
        """Сохранение файла в облачное хранилище"""
        print(f"Сохранение файла '{self.name}' в облако")

    def delete(self):
        """Удаление файла из облачного хранилища"""
        print(f"Удаление файла '{self.name}' из облака")

class S3StorageMixin:
    def save(self):
        """Сохранение файла в S3 хранилище"""
        print(f"Сохранение файла '{self.name}' в S3-хранилище")

    def delete(self):
        """Удаление файла из S3-хранилища"""
        print(f"Удаление файла '{self.name}' из S3-хранилища")

# Использование для облачного хранилища
class CloudAudioFile(AudioFile, CloudStorageMixin):
    pass

class S3VideoFile(VideoFile, S3StorageMixin):
    pass

# Примеры действий с файлами
audio_file = CloudAudioFile(name="song.mp3", size=5000, created_at=datetime.now(), owner="User1", duration=300, bitrate=320)
audio_file.save()  # Сохранение аудио файла в облако
audio_file.extract_features()  # Извлечение фич

# Примеры действий с хранилищами
video_file = S3VideoFile(name="movie.mp4", size=2000000, created_at=datetime.now(), owner="User2", resolution="1920x1080", framerate=30)
video_file.save()  # Сохранение видео файла в S3-хранилище
video_file.convert("avi")  # Конвертация видео в avi