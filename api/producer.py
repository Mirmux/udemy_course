# import pika
#
# params = pika.URLParameters('amqps://nlaypuvn:3uVO7NSL0xygMLaS0qF9oMb9QzxBTDzR@snake.rmq2.cloudamqp.com/nlaypuvn')
#
# connection = pika.BlockingConnection(params)
#
# channel = connection.channel()
#
#
# def publish():
#     channel.basic_publish(exchange='', routing_key='admin', body='Flowers-Garden Service')
#
#
# print(" [x] Sent to data 'Category Service'")
