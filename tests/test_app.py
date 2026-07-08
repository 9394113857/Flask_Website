# ============================================================
# 🧪 FLASK APPLICATION BASIC TEST
#
# Purpose:
#
# - Verify Flask application can start
# - Verify root endpoint is reachable
# - Used by GitHub Actions CI
#
# ============================================================


import pytest

from app import create_app




# ============================================================
# 🔧 CREATE TEST CLIENT
#
# This creates an isolated Flask test environment.
#
# ============================================================

@pytest.fixture
def client():


    app = create_app(testing=True)


    app.config.update(
        TESTING=True
    )


    with app.test_client() as client:

        yield client






# ============================================================
# ❤️ HEALTH CHECK TEST
#
# Expected:
#
# GET /
#
# Response:
# HTTP 200
#
# ============================================================

def test_home_page(client):


    response = client.get("/")


    assert response.status_code == 200