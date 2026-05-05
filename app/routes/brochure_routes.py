from flask import Blueprint

from app.controllers.brochure_controller import brochure_page, generate_brochure


brochure_bp = Blueprint("brochure", __name__,url_prefix="/api/")

brochure_bp.route("/sales-company-brochure", methods=["GET"])(brochure_page)
brochure_bp.route("/brochure/generate", methods=["POST"])(generate_brochure)
