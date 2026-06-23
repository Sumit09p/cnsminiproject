# ip_enrich.py
import json, urllib.request
CACHE: dict[str, dict] = {}

def fetch_ipinfo(ip: str) -> dict:
    if not ip:
        return {}
    if ip in CACHE:
        return CACHE[ip]
    # Use the JSON endpoint (returns country ISO code) for testing
    url = f"https://ipinfo.io/{ip}/json"
    try:
        with urllib.request.urlopen(url, timeout=4) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="ignore"))
            # ipinfo json returns: ip, hostname?, city, region, country, loc, org, postal, timezone
            org = data.get("org") or ""           # e.g., "AS16509 Amazon.com, Inc."
            asn = org.split()[0] if org.startswith("AS") else None
            as_name = " ".join(org.split()[1:]) if org.startswith("AS") else None
            norm = {
                "ip": data.get("ip") or ip,
                "asn": asn,
                "as_name": as_name,
                "country": data.get("country"),        # ISO code like "US" or "DE"
                "country_code": data.get("country"),   # reuse for template
            }
            CACHE[ip] = norm
            return norm
    except Exception:
        return {}

def enrich_hops(received_hops: list[dict]) -> list[dict]:
    for hop in received_hops:
        info = fetch_ipinfo(hop.get("ip", ""))
        hop["ipinfo"] = info
    return received_hops
