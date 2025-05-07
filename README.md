# 🕵️‍♂️ `searxng-wrapper` Documentation

`searxng-wrapper` is a simple async/sync Python library for interacting with [SearXNG](https://searxng.org), a privacy-respecting metasearch engine that supports JSON-based APIs.

## 📦 Installation

Install via `pip`:

```bash
pip install searxng-wrapper
```

To self-host your own SearXNG instance, you can use Docker. Alternatively, use a public instance listed at:

🔗 [https://searx.space](https://searx.space)

## 🚀 Usage

### ✅ Async (Recommended)

```python
from searxng_wrapper import SearxngWrapper
import asyncio

async def main():
    client = SearxngWrapper(
        base_url="https://gatotkaca.arosyihuddin.site",
    )

    result = await client.asearch(
        q="SearXNG"
    )
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

### ✅ Sync

```python
from searxng_wrapper import SearxngWrapper

if __name__ == "__main__":
    client = SearxngWrapper(
        base_url="https://gatotkaca.arosyihuddin.site",
    )

    result = client.search(
        q="SearXNG"
    )

    print(result)
```

## 📌 Important Parameters

| Parameter          | Type        | Default     | Description                                                            |
| ------------------ | ----------- | ----------- | ---------------------------------------------------------------------- |
| `q`                | `str`       | -           | The search query                                                       |
| `language`         | `str`       | `"auto"`    | Result language (`"auto"`, `"en"`, `"id"`, etc.)              |
| `categories`       | `str`       | `"general"` | Search category (`"general"`, `"science"`, `"it"`, etc.)               |
| `page`             | `int`       | `1`         | Search result page                                                     |
| `safesearch`       | `str`       | `"off"`     | Adult content filter (`"off"`, `"moderate"`, `"strict"`)               |
| `time_range`       | `str`       | `"all"`     | Time range (`"day"`, `"week"`, `"month"`, `"year"`, `"all"`)           |
| `max_results`      | `int`       | `None`      | Return only the top N results from the selected page |
| `enabled_engines`  | `List[str]` | `None`      | Force-enable specific search engines                                   |
| `disabled_engines` | `List[str]` | `None`      | Force-disable specific search engines                                  |

## 🛑 Got a 403 Error? Here's the Fix

If you receive a **403 Forbidden** error, your SearXNG instance likely does **not support JSON requests by default**.

### ✅ How to Enable JSON Support

1. Open the `settings.yml` file on your SearXNG server. The file is typically located at:

```bash
/etc/searxng/settings.yml
```

2. Enable the JSON output format by updating the `search:` section:

```yaml
search:
  format:
    - html   # default
    - json   # add this line to enable JSON responses
```

3. Save the file and restart your SearXNG instance:

```bash
docker restart container_name
```

📌 Or simply use a public instance that already supports JSON. You can find one at: [https://searx.space](https://searx.space)

---

## 🤝 Contributing

Contributions are very welcome! Feel free to fork the repository, submit pull requests for new features, bug fixes, or improvements to this documentation.

---
