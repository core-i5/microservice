import pika, json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='app')

def callback(ch, method, properties, body):
    print('Received in app__')
    data = json.loads(body)
    print(data)

channel.basic_consume(queue='app', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()