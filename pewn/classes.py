from dataclasses import dataclass
from pewn.utils import raise_error
from typing import Union
from aiofiles import open as aiopen
from os import makedirs, path


@dataclass
class Option:
    """Option class.

    Init:
        file_name (str): File name.
        folder (str, list): Folder list or path-like string.
            Example: ["images", "random"] is ./images/random.
            Also you can use like this:
                "./images/random"

    Attributes:
        file_name (str): File name.
        folder (str): Converted folder.
    """

    def __init__(self, file_name: str, folder: Union[str, list] = "./") -> None:
        raise_error(file_name, "file_name", str)
        raise_error(folder, "folder", (list, str))

        self.file_name: str = file_name
        self.folder: str = f"./{'/'.join(folder)}" if isinstance(folder,
                                                                 list) else folder

        return None


@dataclass
class NotSavedData:
    """Not saved data class. If you don't add option when you use download function, You will get this class.

    Init:
        data (bytes): Data.
        url (str): URL for data.

    Attributes:
        data (bytes): Data.
        url (str): URL for data.
        size (int): Data size in byte.

    Public Functions:
        <NotSavedData>.write(options: Option) -> str
    """

    def __init__(self, data: bytes, url: str) -> None:
        raise_error(data, "data", bytes)
        raise_error(url, "url", str)

        self.data: bytes = data
        self.url: str = url
        self.size: int = data.__sizeof__()

        return None

    async def write(self, option: Option) -> str:
        """Write data to file.

        Parameters:
            option (Option): Option object.

        Returns:
            str: Saved path.
        """

        raise_error(option, "option", Option)

        if not path.isdir(option.folder):
            makedirs(option.folder)

        full_path = f"{option.folder}/{option.file_name}"
        async with aiopen(full_path, mode="wb") as file:
            await file.write(self.data)

        return full_path
