import os
from supabase import create_client, Client
from supabase_api.domain.video_repository import VideoRepository
import uuid
from datetime import datetime
from typing import Optional, Any




class SupabaseVideoRepository(VideoRepository):
    def __init__(self):
        # Fetch the Supabase credentials from environment variables
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_KEY')
        
        # Check if the environment variables are properly set
        if not supabase_url or not supabase_key:
            raise ValueError("Supabase URL or Key not set in environment variables")

        # Set up Supabase client
        self.client: Client = create_client(supabase_url, supabase_key)

    async def upload_video(self, data) -> Optional[Any]:
        # Upload the video file to the specified path in the Supabase bucket
        # Example: Using a unique ID and timestamp for each video
        path_on_supastorage = f"videos/{uuid.uuid4()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
        try:
            # Upload to the bucket "testbucket"
            response = self.client.storage.from_("videos").upload(
                path=path_on_supastorage,
                file=data,
                file_options={"content-type": "video/mp4"}  # Adjust content type as needed
            )
            return response  # Return response for further processing if needed

        except Exception as e:
            print(f"Error uploading video: {e}")
            return None
