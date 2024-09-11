import pytest
import sys
sys.path.append(r'C:\TTD\src')
from src.string_calculator import add


def test_empty_string_returns_zero():
    assert add("")==0