import pika
import random
import logging
import os

credentials = pika.PlainCredentials(os.environ.get('PRODUCER_USER'), os.environ.get('PRODUCER_PASSWORD'))
parameters = pika.ConnectionParameters(host='rabbitmq', credentials=credentials)
connection = pika.BlockingConnection(parameters)

print("Producer connected successfully")

channel = connection.channel()

channel.queue_declare(queue='success')
channel.queue_declare(queue='warning')
channel.queue_declare(queue='error')

QUEUE_MAPPING = {
    0: {'queue': 'success', 'body': 'Everything OK' },
    1: {'queue': 'warning', 'body': 'Warning here!' },
    2: {'queue': 'error', 'body': 'An error happened and needs attention' }
}



def main():
    message_data = QUEUE_MAPPING[random.randint(0,2)]
    print(f"Generated {message_data['queue']} message")
    channel.basic_publish(exchange='', routing_key=message_data['queue'], body=message_data['body'])


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        try:
            connection.close()
            sys.exit(0)
        except SystemExit:
            connection.close()
            os._exit(0)
