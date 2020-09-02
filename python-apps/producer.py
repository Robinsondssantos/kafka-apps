from kafka import KafkaProducer


def main():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    print(producer.send('quickstart-events', b'ha'))


if __name__ == "__main__":
    main()