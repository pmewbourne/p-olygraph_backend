from abc import ABC, abstractmethod

class VideoRepository(ABC):
    @abstractmethod
    async def upload_video(self, data):
        pass
