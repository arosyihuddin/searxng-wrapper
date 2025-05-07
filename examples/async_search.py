from searxng_wrapper import SearxngWrapper


async def main():
    client = SearxngWrapper(
        base_url="https://gatotkaca.arosyihuddin.site",
        log_level="DEBUG"
    )

    result = await client.asearch(
        q="SearXNG",
        language="all",
        categories="general",
        safesearch="off",
        page=1,
        max_results=1,
        time_range="month",
        enabled_engines=["bing__general"],
        disabled_engines=["google__general", "brave__general",
                          "duckduckgo__general", "qwant__general", "startpage__general"]
    )
    print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
