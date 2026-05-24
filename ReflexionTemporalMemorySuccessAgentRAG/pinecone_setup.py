import importlib.util
import os

# Compatibility wrapper: load implementation from src/pinecone_setup.py
_src_path = os.path.join(os.path.dirname(__file__), "src", "pinecone_setup.py")
spec = importlib.util.spec_from_file_location("_rtms_src_pinecone_setup", _src_path)
_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_mod)

for _name in dir(_mod):
    if not _name.startswith("_"):
        globals()[_name] = getattr(_mod, _name)

__all__ = [n for n in dir(_mod) if not n.startswith("_")]
