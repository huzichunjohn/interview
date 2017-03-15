#/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def generate_random_number():
    return random.sample(range(10), 3)

def consume():
    total = 0
    count = 0

    while True:
        number = yield
        count += len(number)
        total += sum(number)
        print "The average is {}".format(total / float(count))

def produce(consumer):
    while True:
        number = generate_random_number()
        print "Produced {}".format(number)
        consumer.send(number)
        yield

if __name__ == "__main__":
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)

    for _ in range(10):
        print "Producing ..."
        next(producer)
