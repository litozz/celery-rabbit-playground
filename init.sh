#!/bin/sh

# Create Rabbitmq user
( rabbitmqctl wait --timeout 60 $RABBITMQ_PID_FILE ; \
rabbitmqctl add_user $RABBITMQ_PRODUCER_USER $RABBITMQ_PRODUCER_PASSWORD 2>/dev/null ; \
rabbitmqctl set_user_tags $RABBITMQ_USER administrator ; \
rabbitmqctl set_permissions -p / $RABBITMQ_PRODUCER_USER  ".*" ".*" ".*" ; \
echo "*** User '$RABBITMQ_PRODUCER_USER' with password '$RABBITMQ_PRODUCER_PASSWORD' completed. ***" ) &

( rabbitmqctl wait --timeout 60 $RABBITMQ_PID_FILE ; \
rabbitmqctl add_user $RABBITMQ_ERROR_USER $RABBITMQ_ERROR_PASSWORD 2>/dev/null ; \
rabbitmqctl set_user_tags $RABBITMQ_ERROR_USER administrator ; \
rabbitmqctl set_permissions -p / $RABBITMQ_ERROR_USER  ".*" ".*" ".*" ; \
echo "*** User '$RABBITMQ_ERROR_USER' with password '$RABBITMQ_ERROR_PASSWORD' completed. ***" ) &

( rabbitmqctl wait --timeout 60 $RABBITMQ_PID_FILE ; \
rabbitmqctl add_user $RABBITMQ_WARNING_USER $RABBITMQ_WARNING_PASSWORD 2>/dev/null ; \
rabbitmqctl set_user_tags $RABBITMQ_WARNING_USER administrator ; \
rabbitmqctl set_permissions -p / $RABBITMQ_WARNING_USER  ".*" ".*" ".*" ; \
echo "*** User '$RABBITMQ_WARNING_USER' with password '$RABBITMQ_WARNING_PASSWORD' completed. ***") &

( rabbitmqctl wait --timeout 60 $RABBITMQ_PID_FILE ; \
rabbitmqctl add_user $RABBITMQ_SUCCESS_USER $RABBITMQ_SUCCESS_PASSWORD 2>/dev/null ; \
rabbitmqctl set_user_tags $RABBITMQ_SUCCESS_USER administrator ; \
rabbitmqctl set_permissions -p / $RABBITMQ_SUCCESS_USER  ".*" ".*" ".*" ; \
echo "*** User '$RABBITMQ_SUCCESS_USER' with password '$RABBITMQ_SUCCESS_PASSWORD' completed. ***") &

rabbitmq-server
