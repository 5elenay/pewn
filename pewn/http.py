from typing import Union
from pewn.classes import Option, NotSavedData
from pewn.utils import raise_error
from aiohttp import ClientSession
from aiofiles import open as aiopen
from os import makedirs, path


async def download(url: str, option: Option = None) -> Union[str, NotSavedData]:
    """Download data from URL.

    Parameters:
        url (str): URL for fetch and download.
        option (Option): Option object. [Optional]

    Returns:
        str: Saved path.
        NotSavedData: NotSavedData object if you don't add option parameter.
    """

    raise_error(url, "url", str)

    write_file = False
    full_path = None

    if option is not None:
        raise_error(option, "option", Option)
        write_file = True

    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()

            if write_file:
                if not path.isdir(option.folder):
                    makedirs(option.folder)

                full_path = f"{option.folder}/{option.file_name}"
                async with aiopen(full_path, mode="wb") as file:
                    await file.write(data)

    return full_path or NotSavedData(data, url)
