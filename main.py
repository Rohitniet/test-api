@app.get("/test-internet")
def test_internet():
    import requests

    r = requests.get("https://www.google.com", timeout=10)

    return {
        "status": r.status_code
    }