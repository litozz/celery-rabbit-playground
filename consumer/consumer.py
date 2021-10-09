import pika, sys, os

def main(queue):
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('172.23.0.2', credentials=credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue=queue)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main('warning')
    except KeyboardInterrupt:
        try:
            connection.close()
            sys.exit(0)
        except SystemExit:
            connection.close()
            os._exit(0)
