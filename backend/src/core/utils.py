import asyncio
import aiofiles
from PIL import Image
from io import BytesIO


async def compress_image(input_path: str, output_path: str, quality: int):
    async with aiofiles.open(input_path, "rb") as f:
        image_data = await f.read()

    image = Image.open(BytesIO(image_data))

    # Сохраняем изображение с указанным качеством
    output_buffer = BytesIO()
    image.save(output_buffer, format='JPEG', quality=quality)
    output_buffer.seek(0)

    # Асинхронно записываем сжатое изображение
    async with aiofiles.open(output_path, "wb") as f:
        await f.write(output_buffer.getvalue())


# Пример использования
async def main():
    await compress_image("image.jpg", "image1.jpg", 50)


# Запуск асинхронной функции
asyncio.run(main())
