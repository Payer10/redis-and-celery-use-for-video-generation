from celery import shared_task
from moviepy.editor import ImageClip, ColorClip, concatenate_videoclips
import os

OUTPUT_DIR = "generated_videos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@shared_task
def create_videos_from_image(image_path):
    # image theke ekta video clip
    img_clip = ImageClip(image_path, duration=3)

    # fade transition
    fade_clip = img_clip.crossfadein(2)  # fade effect
    fade_out = ColorClip(size=img_clip.size, color=(0,0,0), duration=2)
    fade_video = concatenate_videoclips([img_clip, fade_out], method="compose")
    fade_path = os.path.join(OUTPUT_DIR, "fade_video.mp4")
    fade_video.write_videofile(fade_path, fps=24)

    # wipe transition (simulate by sliding black screen)
    wipe_out = ColorClip(size=img_clip.size, color=(0,0,0), duration=2).set_start(3).set_position(lambda t: (-img_clip.w*t/2,0))
    wipe_video = concatenate_videoclips([img_clip, wipe_out], method="compose")
    wipe_path = os.path.join(OUTPUT_DIR, "wipe_video.mp4")
    wipe_video.write_videofile(wipe_path, fps=24)

    return {
        "fade_video": fade_path,
        "wipe_video": wipe_path
    }
