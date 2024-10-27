from flask import Blueprint, jsonify, request
from supabase_api.application.video_service_impl import get_video_service

video_api = Blueprint('user_api', __name__)

# Create a user
@video_api.route('/video', methods=['POST'])
async def upload_video():
    data = request.json  # The data to create a user (no logic needed here)
    video_service = await get_video_service()  # Get the service dynamically
    user = await video_service.upload_video(data)
    return jsonify(user), 201



