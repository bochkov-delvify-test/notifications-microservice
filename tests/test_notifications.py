from starlette.testclient import TestClient

from delvify.schemas import Email


def test_send_email_invalid_destination(client: TestClient, test_email: Email):
    request_body = {
        "destination": "Not email",
        "subject": test_email.subject,
        "body": test_email.body
    }
    response = client.post("/api/v1/notifications/email", json=request_body)
    assert response.status_code == 422
    assert len(response.json()["detail"]) > 0


def test_send_email_no_destination(client: TestClient, test_email: Email):
    request_body = {
        "subject": test_email.subject,
        "body": test_email.body
    }
    response = client.post("/api/v1/notifications/email", json=request_body)
    assert response.status_code == 422
    assert len(response.json()["detail"]) > 0


def test_send_email_no_subject(client: TestClient, test_email: Email):
    request_body = {
        "destination": test_email.destination,
        "body": test_email.body
    }
    response = client.post("/api/v1/notifications/email", json=request_body)
    assert response.status_code == 422
    assert len(response.json()["detail"]) > 0


def test_send_email_no_body(client: TestClient, test_email: Email):
    request_body = {
        "destination": test_email.destination,
        "subject": test_email.subject
    }
    response = client.post("/api/v1/notifications/email", json=request_body)
    assert response.status_code == 422
    assert len(response.json()["detail"]) > 0
