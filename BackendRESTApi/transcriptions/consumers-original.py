# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

RESPONSE_FROM_DEEP = {
  "raw_sentence": "My stomach aches",
  "deep_output": [
    {
        "category": "CC",
        "accuracy": 82.32
    },
    {
        "category": "PI",
        "accuracy": 79.32
    }
  ],
  "error_msg": "",
  "created": "2012-04-23T18:25:43.511Z"
}


class ClientConsumer(AsyncWebsocketConsumer):

    # Send signal to start deep engine
    async def _start_deep_engine(self, patient_id):
        pass

    async def connect(self):
        self.patient_id = self.scope['path'].split('/')[-2]
        self.patient_group_name = '{patient_id}_group'.format(patient_id=self.patient_id)

        # # Start deep learning module
        await self._start_deep_engine(self.patient_id)

        # Join channel 'group' where messages from deep learning module and
        # client can be shared
        await self.channel_layer.group_add(
            self.patient_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave channel group
        await self.channel_layer.group_discard(
            self.patient_group_name,
            self.channel_name
        )

    # Receive message from WebSocket(Client)
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        raw_sentence = text_data_json['raw_sentence']

        # Send message to room group
        await self.channel_layer.group_send(
            self.patient_group_name,
            {
                'type': 'propagate.input.to.deep',
                'raw_sentence': raw_sentence
            }
        )

    # Receive result from channel group
    async def propagate_result_to_client(self, event):
        result = event['result']

        # Send result to client
        await self.send(text_data=json.dumps(result))

    async def propagate_input_to_deep(self, event):
        pass


class DeepConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.patient_id = self.scope['path'].split('/')[-2]
        self.patient_group_name = '{patient_id}_group'.format(patient_id=self.patient_id)

        # Join channel 'group' where messages from deep learning module and
        # client can be shared
        await self.channel_layer.group_add(
            self.patient_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave channel group
        await self.channel_layer.group_discard(
            self.patient_group_name,
            self.channel_name
        )

    # Receive message from WebSocket(Deep learning module)
    async def receive(self, text_data):
        # TODO: change after integration with deep engine
        text_data = RESPONSE_FROM_DEEP

        text_data_json = json.dumps(text_data)
        result = text_data_json

        await self.channel_layer.group_send(
            self.patient_group_name,
            {
                'type': 'propagate.result.to.client',
                'result': result
            }
        )

    # Receive raw sentence from client group
    async def propagate_input_to_deep(self, event):
        raw_sentence = event['raw_sentence']

        # Send raw sentence to deep engine
        await self.send(text_data=json.dumps({
            'raw_sentence': raw_sentence
        }))

    async def propagate_result_to_client(self, event):
        pass
