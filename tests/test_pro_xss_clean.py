"""Tests for pro-xss-clean."""

import pytest
from pro_xss_clean import clean


class TestClean:
    """Test suite for clean."""

    def test_basic(self):
        """Test basic usage."""
        result = clean("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            clean("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = clean(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
