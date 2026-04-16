from django.http import JsonResponse
from .tasks import create_videos_from_image

def generate_videos(request):
    image_path = "/home/payerahmed/Downloads/orang.jpg"  # তোমার image file path
    task = create_videos_from_image.delay(image_path)
    return JsonResponse({"task_id": task.id})
 