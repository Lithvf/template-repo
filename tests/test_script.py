import subprocess
import sys
from pathlib import Path


def test_script_output():
    script_path = Path(__file__).resolve().parent.parent / "src" / "script.py"
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True, check=True)
    assert result.stdout.strip() == "hello world"

