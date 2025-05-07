from searxng_wrapper import SearxngWrapper

if __name__ == "__main__":
    client = SearxngWrapper(
        base_url="https://gatotkaca.arosyihuddin.site",
        log_level="DEBUG"
    )

    result = client.search(
        q="SearXNG",
        language="auto",
        categories="social media",
        safesearch="off",
        page=1,
        time_range="all",
        enabled_engines=["bing__general"],
        disabled_engines=["google__general", "brave__general",
                          "duckduckgo__general", "qwant__general", "startpage__general"]
    )

    print(result)
