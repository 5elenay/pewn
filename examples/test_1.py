import pewn
import asyncio

option = pewn.Option(
    file_name="photo_1.png",
    folder="./random"
)


async def main():
    result = await pewn.download("https://picsum.photos/500/300")
    await result.write(option)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
