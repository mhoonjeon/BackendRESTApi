# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
from BackendRESTApi.deeplearning.wrapper import Classifier
import json


class ClientConsumer(AsyncWebsocketConsumer):

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

    # Receive message from WebSocket(Client)
    async def receive(self, text_data):
        raw_sentence = json.loads(text_data)['raw_sentence']

        clf = Classifier()
        result = clf.inference(raw_sentence)
        await self.send(text_data=json.dumps(result))
