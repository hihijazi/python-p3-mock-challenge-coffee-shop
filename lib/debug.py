#!/usr/bin/env python3
import ipdb
from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")


    c1 = Coffee("Starbucks")
    c2 = Coffee("Costa")    
    c3 = Coffee("Dunkin")  

    ca = Customer("Caleb")
    cb = Customer("Beth")
    cc = Customer("Carl")

    o1 = Order(ca, c1, 5)
    o2 = Order(cb, c1, 3)
    o3 = Order(cc, c2, 2)
    
ipdb.set_trace()
