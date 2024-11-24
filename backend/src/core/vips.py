from pathlib import Path

import pyvips


def split_image(
    img_path: Path,
    output_dir: Path,
    tile_size: int,
    quality: int,
) -> None:
    output_dir.parent.mkdir(parents=True, exist_ok=True)

    image = pyvips.Image.new_from_file(img_path, access="sequential")
    image.dzsave(
        output_dir,
        tile_size=tile_size,
        suffix=f".webp[Q={quality}]",
    )
