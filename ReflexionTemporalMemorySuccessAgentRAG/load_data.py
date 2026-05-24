import os
import time
import base64
import requests
from io import BytesIO
from urllib.parse import urljoin

import pandas as pd
from pdf2image import convert_from_path
from PIL import Image
from pypdf import PdfReader

from chunking import chunk_text

# ------------------- ENV / CONFIG -------------------
PDF_FOLDER = os.getenv("PDF_FOLDER", "/path/to/pdfs")
CSV_PATH = os.getenv("CSV_PATH", "/path/to/judgments.csv")

# ✅ Prefix for links stored in CSV (temp_link)
BASE_URL = os.getenv("BASE_URL", "https://api.sci.gov.in/")

YANDEX_API_KEY = os.getenv("YANDEX_API_KEY")
YANDEX_IAM_TOKEN = os.getenv("YANDEX_IAM_TOKEN")
FOLDER_ID = os.getenv("YANDEX_FOLDER_ID")

OCR_LANGUAGES = os.getenv("OCR_LANGUAGES", "en,fr,es,pt").split(",")

MAX_DPI = int(os.getenv("MAX_DPI", "300"))
MAX_PIXELS = int(os.getenv("MAX_PIXELS", str(10000 * 10000)))
SLEEP_BETWEEN_REQUESTS = float(os.getenv("SLEEP_BETWEEN_REQUESTS", "0.5"))
RETRIES = int(os.getenv("RETRIES", "3"))
ENABLE_OCR_FALLBACK = os.getenv("ENABLE_OCR_FALLBACK", "0").strip() == "1"
import importlib.util
import os

# Compatibility wrapper: load implementation from src/load_data.py
_src_path = os.path.join(os.path.dirname(__file__), "src", "load_data.py")
spec = importlib.util.spec_from_file_location("_rtms_src_load_data", _src_path)
_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_mod)

for _name in dir(_mod):
    if not _name.startswith("_"):
        globals()[_name] = getattr(_mod, _name)

__all__ = [n for n in dir(_mod) if not n.startswith("_")]

