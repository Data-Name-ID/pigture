from django.conf import settings

from config.celery import app
from core.vips import split_image, compress

@app.task
def process_image(image_path, image_id):
    split_image(
        image_path,
        settings.MEDIA_ROOT / f"tiles/{image_id}/tiles",
        256,
        75,
    )
    # compress(
    #     image_path,
    #     settings.MEDIA_ROOT,
    #     60,
    # )
