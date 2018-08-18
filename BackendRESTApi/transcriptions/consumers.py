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

        # Start deep learning module
        #TODO: need to confirm websocket with deep before allowing frontend connection
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
        text_data = RESPONSE_FROM_DEEP

        text_data_json = json.dumps(text_data)
        result = text_data_json

        await self.send(text_data=json.dumps(result))
