"""
Program Name: Lab16_abdulladif1.py
Author: Abdulladif 
Purpose: Refactor the Chapter 17 'hn_submissions.py' idea to safely fetch and list popular
         Hacker News articles without crashing on missing JSON fields 
Date: 8/9/2025
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

import requests


HN_BASE = "https://hacker-news.firebaseio.com/v0"
TIMEOUT = 10  
MAX_ITEMS = 30  


def fetch_json(url: str) -> Optional[Dict[str, Any]]:
    """GET a URL and return JSON, handling network errors gracefully."""
    try:
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        print(f"[WARN] Request failed for {url}: {e}")
        return None
    except ValueError:
        print(f"[WARN] Invalid JSON from {url}")
        return None


def safe_item_field(item: Dict[str, Any], key: str, default: Any) -> Any:
    """Safely pull a field from an HN item, falling back to default if missing/None."""
    val = item.get(key, default)
    return default if val is None else val


def main() -> None:
    print("Fetching top Hacker News story IDs")
    ids_url = f"{HN_BASE}/topstories.json"
    ids = fetch_json(ids_url)

    if not isinstance(ids, list) or not ids:
        print("[ERROR] Could not retrieve top story IDs. Exiting.")
        return

    stories: List[Dict[str, Any]] = []
    print(f"Got {len(ids)} IDs. Fetching first {MAX_ITEMS} items\n")

    for i, story_id in enumerate(ids[:MAX_ITEMS], start=1):
        item_url = f"{HN_BASE}/item/{story_id}.json"
        item = fetch_json(item_url)
        if item is None:
            print(f"  {i:2d}. [SKIP] ID {story_id}: request/JSON error.")
            continue

        
        title = safe_item_field(item, "title", "[no title]")
        score = safe_item_field(item, "score", 0)
        comments = safe_item_field(item, "descendants", 0)  
        url = safe_item_field(item, "url", f"https://news.ycombinator.com/item?id={story_id}")

        
        try:
            score = int(score)
        except (TypeError, ValueError):
            score = 0
        try:
            comments = int(comments)
        except (TypeError, ValueError):
            comments = 0

        stories.append(
            {
                "id": story_id,
                "title": title,
                "score": score,
                "comments": comments,
                "url": url,
            }
        )

        print(f"  {i:2d}. OK  ID {story_id}  | comments={comments:3d}  score={score:3d}  title={title[:60]!r}")
        
        time.sleep(0.05)

    if not stories:
        print("\n[ERROR] No stories gathered. Nothing to display.")
        return

    
    stories.sort(key=lambda s: (s["comments"], s["score"]), reverse=True)

    print("\nTop stories by comments:")
    print("-" * 80)
    for rank, s in enumerate(stories, start=1):
        print(
            f"{rank:2d}. {s['title']}\n"
            f"    comments: {s['comments']} | score: {s['score']} | link: {s['url']}"
        )
    print("-" * 80)


if __name__ == "__main__":
    main()
