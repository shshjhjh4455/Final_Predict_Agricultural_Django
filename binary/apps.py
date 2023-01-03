import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    name = "api"
    MODEL_FILE = os.path.join(
        settings.MODEL, "xgb_baechoo_bin_classify_jinhyeok.pickle"
    )
    model = joblib.load(MODEL_FILE)