import asyncio
import json
import os
import pytest
import websocket
from channels.testing import WebsocketCommunicator
from .consumers import ClientConsumer


@pytest.mark.asyncio
async def test_frontend_can_test_temporarily_before_deep_integration():
    patient_id = 'abc123'
    client_URL = f'/ws/v1/transcriptions/client/{patient_id}/'
    client_communicator = WebsocketCommunicator(ClientConsumer, client_URL)
    connected, subprotocol = await client_communicator.connect()
    assert connected

    text_data = {
        "raw_sentence": "My stomach aches",
    }

    # client send text to deep learning and check if deep engine got it
    await client_communicator.send_to(text_data=json.dumps(text_data))
    response = await client_communicator.receive_from()
    response = json.loads(response)
    assert 'deep_output' in response

    await client_communicator.disconnect()
