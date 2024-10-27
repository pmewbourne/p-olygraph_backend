from supabase_api.infrastructure.video_impl import SupabaseVideoRepository
from supabase_api.application.video_service_repository import VideoRepository

class VideoServiceImpl(VideoRepository):
    def __init__(self, video_repository: SupabaseVideoRepository):
        self.video_repository = video_repository

    async def upload_video(self, data):
        return await self.video_repository.upload_video(data)

# Factory function to get the video service with the repository implementation
async def get_video_service() -> VideoRepository:
    video_repository = SupabaseVideoRepository()
    return VideoServiceImpl(video_repository)
