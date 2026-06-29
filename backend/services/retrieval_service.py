import os
import requests

WIKIPEDIA_API = "https://en.wikipedia.org/api/rest_v1/page/summary/"


def retrieve_sources(answer: str) -> list:
    """
    Basic retrieval: extracts key terms from answer,
    searches Wikipedia, returns source snippets.
    Returns a list of source dicts with title, url, snippet.
    """
    # Extract first 5 meaningful words as search term (simple approach)
    words = [w for w in answer.split() if len(w) > 4]
    query = " ".join(words[:5]) if words else answer[:50]

    sources = []

    try:
        # Wikipedia search API
        search_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "srlimit": 3
        }
        response = requests.get(search_url, params=params, timeout=5)
        data = response.json()

        for item in data.get("query", {}).get("search", []):
            title = item.get("title", "")
            snippet = item.get("snippet", "").replace("<span class=\"searchmatch\">", "").replace("</span>", "")
            url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
            sources.append({
                "title": title,
                "url": url,
                "snippet": snippet
            })

    except requests.RequestException:
        # If Wikipedia is unreachable, return empty list gracefully
        sources = []

    return sources