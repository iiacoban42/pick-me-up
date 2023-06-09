"""Websocket entry endpoint (example)"""
import json
from channels.generic.websocket import WebsocketConsumer

class EchoConsumer(WebsocketConsumer):
    """
    A sample websocket consumer, as demo to use for new things!
    """
    def connect(self):
        self.accept()
        self.send("Connected to websocket")

    def receive(self, text_data=None, bytes_data=None):
        self.send(json.dumps({
            'context': 'echo',
            'text': text_data
        }))
