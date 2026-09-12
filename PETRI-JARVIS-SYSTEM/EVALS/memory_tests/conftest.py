import sys
from pathlib import Path

# Make scripts/build_index.py and scripts/search.py importable as plain
# modules from the tests without turning them into an installed package —
# keeps Phase 1 dependency-free (no setup.py/pyproject needed just to run
# the eval suite).
_SCRIPTS_DIR = Path(__file__).resolve().parents[2] / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))
