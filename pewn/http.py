from typing import Union
from pewn.classes import Option, NotSavedData
from pewn.utils import raise_error
from aiohttp import ClientSession
from aiofiles import open as aiopen
from os import makedirs, path
from asyncio import gather


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


async def download_multiple(urls: tuple, options: Union[tuple, Option] = None):
    """Download multiple file.

    Parameters:
        urls (tuple): List of URL that will be downloaded.
        options (tuple, Option): List of Option or only one Option object. [Optional]

    Returns:
        list (str): Saved paths.
        list (NotSavedData): List of NotSavedData object if you don't add options parameter.
    """

    raise_error(urls, "urls", tuple)

    results = ()

    if options is not None:
        raise_error(options, "option", (tuple, Option))

    if isinstance(options, tuple):
        results = await gather(*[
            download(url, opt) for url, opt in zip(urls, options)
        ])
    elif isinstance(options, Option):
        def change_file_name(option: Option, number: int):
            splitted_name = option.file_name.split('.')

            real_file_name = splitted_name[-2]
            real_file_name += f"_{number}"

            splitted_name[-2] = real_file_name

            return ".".join(splitted_name)

        results = await gather(*[
            download(url, opt) for url, opt in zip(urls, [Option(file_name=change_file_name(options, i + 1), folder=options.folder) for i, _ in enumerate(urls)])
        ])
    else:
        results = await gather(*[
            download(url) for url in urls
        ])

    return results
