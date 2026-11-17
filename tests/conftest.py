import pytest
from copy import deepcopy
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def fresh_activities():
    """
    Provide a fresh copy of activities for each test.
    This ensures test isolation so changes in one test don't affect others.
    """
    return deepcopy(activities)


@pytest.fixture
def app_with_fresh_state(fresh_activities, monkeypatch):
    """
    Replace the app's activities with a fresh copy before each test.
    Uses pytest's monkeypatch to safely replace the module-level activities dict.
    """
    import src.app
    monkeypatch.setattr(src.app, "activities", fresh_activities)
    return app
