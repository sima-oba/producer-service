from confluent_kafka import Producer

from domain.repository import IPublisher


class KafkaProducer(IPublisher):
    def __init__(self, config: dict):
        self._producer = Producer(config)

    def send(self, topic: str, data: any, key: str = None) -> str:
        self._producer.produce(topic, key=key, value=data)
        self._producer.flush()

        return key
