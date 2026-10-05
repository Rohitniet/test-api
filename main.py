from fastapi import FastAPI
import requests

app = FastAPI(
    title="Network Test API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "FastAPI is running"
    }


@app.get("/test-internet")
def test_internet():
    try:
        response = requests.get(
            "https://www.google.com",
            timeout=10
        )

        return {
            "success": True,
            "status_code": response.status_code,
            "message": "Internet connection is working"
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@app.get("/test-gem")
def test_gem():
    try:
        response = requests.get(
            "https://bidplus.gem.gov.in/all-bids",
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/154.0.0.0 Safari/537.36"
                )
            },
            timeout=20
        )

        return {
            "success": True,
            "status_code": response.status_code,
            "message": "GeM is reachable",
            "response_start": response.text[:500]
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }