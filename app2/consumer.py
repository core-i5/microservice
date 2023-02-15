import pika, json
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app2.settings")
django.setup()
from core.models import User

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='app2')

def callback(ch, method, properties, body):
    print('Received in app2__')
    data = json.loads(body)
    print(data)
    if properties.content_type == 'user_created':
        user = User(id=data['id'], name=data['name'], age=data['age'], fever=data['fever'], body_pain=data['body_pain'], runny_nose = data['runny_nose'], diff_breath=data['diff_breath'])
        user.save()
        print("user created")

    elif properties.content_type == 'user_updated':
        user = User.objects.get(id=data['id'])
        user.name = data['name']
        user.age=data['age']
        user.fever=data['fever']
        user.body_pain=data['body_pain']
        user.runny_nose = data['runny_nose']
        user.diff_breath=data['diff_breath']
        user.save()
        print("user updated")

    elif properties.content_type == 'user_deleted':
        user = User.objects.get(id=data)
        user.delete()
        print("user deleted")
    

channel.basic_consume(queue='app2', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()