import pytest

if __name__ == "__main__":
    # pytest.main(["-v", "tests"])
    pytest.main(["-k", "contact_us", "-v", "-s"])