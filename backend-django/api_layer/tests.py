import pytest as pytest
from channels.testing import WebsocketCommunicator
from config.asgi import application


@pytest.mark.asyncio
async def test_websocket():
    communicator = WebsocketCommunicator(application, "/ws/status/")
    communicator_visitor = WebsocketCommunicator(application, "/ws/status/")

    connected, _ = await communicator.connect()
    assert connected is True
    connected_visitor, _ = await communicator_visitor.connect()
    assert connected_visitor is True

    await communicator.send_json_to({"type": "broadcast.echo", "message": "Hello there!"})

    response = await communicator_visitor.receive_json_from(timeout=3)
    assert response["value"] == "expected_value"
    await communicator.disconnect()
