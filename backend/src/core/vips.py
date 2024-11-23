from pathlib import Path

import pyvips


def split_image(
    img_path: str,
    output_dir: str,
    tile_size: int,
    quality: int,
) -> None:
    img_suffix = Path(img_path).suffix

    image = pyvips.Image.new_from_file(img_path)
    image.dzsave(
        output_dir,
        tile_size=tile_size,
        suffix=f".{img_suffix}[Q={quality}]",
    )


def compress(img_path: str, output_dir: str, quality: int) -> None:
    img_path = Path(img_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    image = pyvips.Image.new_from_file(str(img_path), access="sequential")
    output_path = output_dir / img_path.with_suffix(".jpg").name
    image.write_to_file(str(output_path), Q=quality)
