def test_voice_endpoint(client):
    response = client.post(
        "/api/voice/",
        json={"audio_base64": "dGVzdA=="}
    )

    assert response.status_code == 200
    assert "transcript" in response.json()