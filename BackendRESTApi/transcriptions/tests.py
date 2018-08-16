import asyncio
import json
import os
import pytest
import websocket
from channels.testing import WebsocketCommunicator
from .consumers import ClientConsumer, DeepConsumer


@pytest.mark.asyncio
async def test_client_consumer_can_connect():
    patient_id = 'abc123'
    client_URL = f'/ws/v1/transcriptions/client/{patient_id}/'
    client_communicator = WebsocketCommunicator(ClientConsumer, client_URL)
    connected, subprotocol = await client_communicator.connect()
    assert connected

    text_data = {
        "raw_sentence": "My stomach aches",
    }

    # Suppose deep learning module is connected
    deep_URL = f'/ws/v1/transcriptions/deep/{patient_id}/'
    deep_communicator = WebsocketCommunicator(DeepConsumer, deep_URL)
    connected, subprotocol = await deep_communicator.connect()
    assert connected


    # client send text to deep learning and check if deep engine got it
    await client_communicator.send_to(text_data=json.dumps(text_data))
    response = await deep_communicator.receive_from()
    response = json.loads(response)
    assert 'My stomach aches' == response['raw_sentence']

    # deep engine send result back to client
    # TODO: need to be changed after integration with deep engine
    text_data = {'trigger': 'temp'}
    await deep_communicator.send_to(text_data=json.dumps(text_data))
    response = await client_communicator.receive_from()
    response = json.loads(response)
    assert 'deep_output' in response

    await client_communicator.disconnect()
    await deep_communicator.disconnect()
