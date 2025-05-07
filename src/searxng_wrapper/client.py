import requests
import asyncio
import aiohttp
from .types import Language, SafeSearch, SAFESEARCH_MAP, Category, SearchResponse, EngineName, TimeRange
from urllib.parse import urljoin
from .core import setup_logger, logging_level
from typing import Optional, List


class SearxngWrapper:
    def __init__(
        self,
        base_url: str = "http://localhost:8888",
        save_logs: bool = False,
        log_level: logging_level = "INFO"
    ):
        self.base_url: str = urljoin(base_url, "/search")
        self.logger = setup_logger(log_level, save_logs)

    def search(
        self,
        q: str,
        language: Optional[Language] = "auto",
        categories: Optional[Category] = "general",
        page: Optional[int] = 1,
        safesearch: Optional[SafeSearch] = "off",
        time_range: Optional[TimeRange] = "all",
        max_results: Optional[int] = None,
        enabled_engines: Optional[List[EngineName]] = None,
        disabled_engines: Optional[List[EngineName]] = None
    ) -> SearchResponse:
        params = {
            "q": q,
            "format": "json",
            "lenguage": language,
            "categories": categories,
            "page": page,
            "safesearch": SAFESEARCH_MAP[safesearch],
            "time_range": None if time_range == "all" else time_range,
        }

        if disabled_engines:
            params["disabled_engines"] = ",".join(disabled_engines)

        if enabled_engines:
            params["enabled_engines"] = ",".join(enabled_engines)

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
            "Accept": "application/json",
        }

        try:
            response = requests.get(
                self.base_url, params=params, headers=headers)
            response.raise_for_status()
            self.logger.info(f"Response status code: {response.status_code}")
            results = response.json()
            return SearchResponse(
                query=q,
                number_of_results=results["number_of_results"],
                results=results["results"][:max_results]
            )

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {e}")

    async def asearch(
        self,
        q: str,
        language: Language,
        categories: Category,
        page: int,
        safesearch: SafeSearch = "off",
        time_range: Optional[TimeRange] = "all",
        max_results: Optional[int] = None,
        enabled_engines: Optional[List[EngineName]] = None,
        disabled_engines: Optional[List[EngineName]] = None
    ) -> SearchResponse:
        params = {
            "q": q,
            "format": "json",
            "lenguage": language,
            "categories": categories,
            "page": page,
            "safesearch": SAFESEARCH_MAP[safesearch],
            "time_range": None if time_range == "all" else time_range,
        }

        if disabled_engines:
            params["disabled_engines"] = ",".join(disabled_engines)

        if enabled_engines:
            params["enabled_engines"] = ",".join(enabled_engines)

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
            "Accept": "application/json",
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.base_url, params=params, headers=headers) as resp:
                    resp.raise_for_status()
                    self.logger.info(
                        f"Response status code: {resp.status}")
                    data = await resp.json()
                    return SearchResponse(
                        query=q,
                        number_of_results=data["number_of_results"],
                        results=data["results"][:max_results]
                    )
        except aiohttp.ClientError as e:
            self.logger.error(f"Request failed: {e}")
