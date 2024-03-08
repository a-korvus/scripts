"""Implementation of an Internet crawler.

The script collects all links from specified sites.
It is possible to set the penetration depth.
"""

import aiofiles
import asyncio
import shutil
from aiohttp import ClientSession, ClientTimeout
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from pathlib import Path, PosixPath
from typing import Coroutine


class Crowler:
    """The links parser."""

    def __init__(self) -> None:
        """Class constructor."""
        self.__timeout: int = 1
        self.__file_path: PosixPath | None = None

    async def __get_content(self, client: ClientSession, url: str) -> None:
        """Get content from the site."""
        try:
            async with client.get(url=url, timeout=self.__timeout) as response:
                content: bytes = await response.read()
            soup: BeautifulSoup = BeautifulSoup(
                markup=content,
                features="lxml",
            )
            all_tags_a: ResultSet = soup.find_all(name="a")
            await self.__parse_links(url, all_tags_a)
        except Exception as _ex:
            print(f"{_ex}")
            pass

    async def __parse_links(self, url: str, links_set: ResultSet) -> None:
        """Parse all the links from the site."""
        for item in links_set:
            item_url: str = item.get("href")

            link: None | str = None
            if item_url and item_url.startswith("https://"):
                link = item_url
            elif item_url and item_url.startswith("/"):
                link = url + item_url[1:]

            if link:
                await self.__write_to_file(link, self.__file_path)

    async def __write_to_file(
        self, content: str, file_path: PosixPath
    ) -> None:
        """Write a link to the file."""
        async with aiofiles.open(file_path, mode='a') as file:
            await file.write(content + "\n")

    async def __get_all_links(self, urls: list, timeout: int) -> list:
        """Get all the links from the site."""
        async with ClientSession(timeout=ClientTimeout(timeout)) as client:
            tasks: list[Coroutine] = [
                self.__get_content(client=client, url=url)
                for url in urls
            ]

            return await asyncio.gather(*tasks)

    def run(
        self,
        urls: list,
        file_dir_path: PosixPath,
        file_name: str,
        timeout_client: int = 2,
        timeout_session: int = 10,
        depth: int = 3,
    ) -> None:
        """Run the asynchronous client."""
        if depth < 1:
            raise ValueError("Depth must be greater than zero")
        if not isinstance(file_dir_path, PosixPath):
            raise ValueError("File dir path must be a PosixPath object.")
        if not isinstance(file_name, str):
            raise ValueError("File name must be a string object.")
        if not isinstance(timeout_client, int) \
                or not isinstance(timeout_session, int):
            raise ValueError("Timeout must be an integer object.")

        counter = 1
        self.__timeout = timeout_client

        while counter <= depth:
            if counter > 1:
                with open(self.__file_path, "r") as file:
                    urls = file.read().strip().split("\n")

            self.__file_path = file_dir_path / f"{counter}_{file_name}"
            self.__file_path.touch()

            asyncio.run(self.__get_all_links(urls, timeout_session))
            counter += 1

        result_file: PosixPath = file_dir_path / file_name
        result_file.touch()

        with open(result_file, "a") as result_file:
            for file_links in file_dir_path.iterdir():
                if file_links.name != file_name:
                    with open(file_links, "r") as file:
                        result_file.write(file.read())

                    file_links.unlink()

        print("The crawler has completed its work.")


if __name__ == "__main__":
    base_dir: PosixPath = Path(__file__).resolve().parent
    file_dir_path: PosixPath = base_dir / "files"
    if file_dir_path.exists():
        shutil.rmtree(file_dir_path)
    file_dir_path.mkdir()

    main_links: list[str] = [
        "https://skillbox.ru/",
        "https://skillfactory.ru/",
        "https://gb.ru/"
    ]

    crowler = Crowler()
    crowler.run(
        urls=main_links,
        file_dir_path=file_dir_path,
        file_name="result.txt",
        timeout_session=20,
        timeout_client=5,
    )
