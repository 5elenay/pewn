import pewn
import asyncio

option = pewn.Option(
    file_name="photo_2.png",
    folder="./random"
)

loop = asyncio.get_event_loop()
loop.run_until_complete(pewn.download("https://picsum.photos/500/300", option))
