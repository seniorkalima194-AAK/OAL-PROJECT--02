import importlib


def test_backend_main_exports_fastapi_app():
    module = importlib.import_module("backend.main")
    assert hasattr(module, "app")
