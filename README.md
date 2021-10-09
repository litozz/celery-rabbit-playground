# Celery rabbitmq tutorial

This repo is about how to use queues to send-receive messages and Celery to manage tasks.

# How to running

Just clone the repo and run `docker-compose up`

# What are you running?

After running the above command a whole enviroment will be created. We will have a message producer that will randomly produce error, warning or success messages. Also will have a consumer for each type of message error. After running that you will see nothing but this environment also will provide an user interface for RabbitMQ that will allow you to see how messages are produced and how consumers are reading the messages from the different queries.

[Future] Each of these roles (producer and consumers) can be seen as tasks. Since Celery manages tasks we will learn how to manage Celery to orchestrate all these tasks.
