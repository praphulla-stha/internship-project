import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def make_request(method, url, **kwargs):
    try:
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()
        logger.info(f"{method} request to {url} successful")
        return response.json()
    except requests.RequestException as e:
        logger.error(f"{method} request to {url} failed: {e}")
        return {"error": str(e), "status_code": getattr(e.response, "status_code", None)}