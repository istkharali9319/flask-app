from pathlib import Path

from flask import jsonify, request, send_from_directory

from app.services.ai_service import AiService


PROJECT_ROOT = Path(__file__).resolve().parents[2]
BROCHURE_DIR = PROJECT_ROOT / "sales-company-brochure"


def brochure_page():
    return send_from_directory(BROCHURE_DIR, "index.html")


def generate_brochure():
    payload = request.get_json(silent=True) or {}
    prompt = (payload.get("prompt") or "").strip()
    provider = (payload.get("provider") or "static").strip()

    if not prompt:
        return jsonify(
            {
                "success": False,
                "message": "Prompt is required.",
                "errors": ["Please enter a brochure prompt."],
            }
        ), 422

    brochure_html = AiService.generate_brochure_html(prompt, provider)

    return jsonify(
        {
            "success": True,
            "message": "Brochure generated successfully.",
            "data": {
                "prompt": prompt,
                "provider": provider,
                "html": brochure_html,
            },
        }
    ), 200
