import requests
from urllib.parse import urlparse

class PhishingDetector:
    @staticmethod
    def check_url(url):
        try:
            response = requests.get(url, timeout=5)
            parsed_url = urlparse(url)
            return {
                "status_code": response.status_code,
                "domain": parsed_url.netloc,
                "is_secure": response.url.startswith("https://"),
                "suspicious_keywords": ["login", "signin", "verify"] if any(word in url.lower() for word in ["login", "signin", "verify"]) else []
            }
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
