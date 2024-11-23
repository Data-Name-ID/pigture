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
        suffix=f".{img_path.suffix}[Q={quality}]",
    )


def compress(
    img_path: str,
    output_dir: str,
) -> None:
    img_path = Path(img_path)
    output_dir = Path(output_dir)
    image = pyvips.Image.new_from_file(img_path)

    image.write_to_file(
        output_dir / img_path.stem + img_path.suffix,
        predictor="horizontal",
        compression="deflate",
    )
