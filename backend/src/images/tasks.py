from pathlib import Path

from django.conf import settings

from config.celery import app
from core.vips import compress, split_image


@app.task
def process_image(image_path: str, image_id: int):
    image_path = Path(image_path).resolve()
    split_image(
        image_path,
        settings.TILES_ROOT / f"{image_id}/tiles",
        256,
        75,
    )
    # compress(
    #     image_path,
    #     settings.MEDIA_ROOT,
    #     60,
    # )
