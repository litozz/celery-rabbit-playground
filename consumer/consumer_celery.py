import pika, sys, os
import logging
from orchestrator import app

@app.task
def consume(queue):
    credentials = pika.PlainCredentials(os.environ.get('CONSUMER_USER'), os.environ.get('CONSUMER_PASSWORD'))
    parameters = pika.ConnectionParameters(host='rabbitmq', credentials=credentials)
    connection = pika.BlockingConnection(parameters)

    print("Consumer connected successfully")

    channel = connection.channel()

    channel.queue_declare(queue=queue)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        consume.delay(os.environ.get('CONSUMER_QUEUE'))
    except KeyboardInterrupt:
        try:
            connection.close()
            sys.exit(0)
        except SystemExit:
            connection.close()
            os._exit(0)
