import pewn
import asyncio

option = pewn.Option(
    file_name="photo.png",
    folder="./photos"
)


async def main():
    result = await pewn.download_multiple(
        tuple(["https://picsum.photos/500/300" for _ in range(10)]), 
        option
    )
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
