from confluent_kafka import Producer

from domain.repository import IPublisher


class KafkaProducer(IPublisher):
    def __init__(self, config: dict):
        self._config = config
        self._producer = None

    def send(self, topic: str, data: any, key: str = None) -> str:
        # Workaround to deal with Kafka producer multiprocessing issues
        if self._producer is None:
            self._producer = Producer(self._config)

        self._producer.produce(topic, key=key, value=data)
        self._producer.flush()

        return key
