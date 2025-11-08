import logging
import azure.functions as func
import requests
from bs4 import BeautifulSoup
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("SummarizeNews function triggered.")

    try:
        req_body = req.get_json()
        url = req_body.get("url")

        if not url:
            return func.HttpResponse(
                "❌ Please provide a valid URL in the request body (JSON format: {\"url\": \"<article_url>\"})",
                status_code=400
            )

        logging.info(f"Fetching article from {url}")

        try:
            response = requests.get(url, timeout=10)
        except requests.exceptions.RequestException as e:
            return func.HttpResponse(f"⚠️ Network error: {e}", status_code=500)

        if response.status_code != 200:
            return func.HttpResponse(f"⚠️ Failed to fetch article. HTTP {response.status_code}", status_code=response.status_code)

        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        article_text = " ".join(paragraphs).strip()

        if not article_text:
            return func.HttpResponse("⚠️ No valid article text found. Try another URL.", status_code=500)

        # Simple summarization logic (extracts first 3 sentences)
        sentences = article_text.split(". ")
        summary = ". ".join(sentences[:3]) + "."

        return func.HttpResponse(json.dumps({"summary": summary}),mimetype="application/json",status_code=200)

    except Exception as e:
        logging.exception("Unexpected error occurred.")
        return func.HttpResponse(f"❌ Error: {str(e)}", status_code=500)
