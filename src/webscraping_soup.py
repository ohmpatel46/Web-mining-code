# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 21:35:47 2021

@author: ohmpa
"""

from bs4 import BeautifulSoup
import requests
page = requests.get("https://www.flipkart.com/nike-revolution-4-running-shoes-men/p/itma13031f395b74?pid=SHOFS5GQWZJXN43R&lid=LSTSHOFS5GQWZJXN43RDBRUQ8&marketplace=FLIPKART&sattr[]=color&sattr[]=size&st=size&otracker=hp_omu_Men%252527s%252BFootwear%252B_4_12.dealCard.OMU_YEM63DW5737L_7")
soup = BeautifulSoup(page.content, 'html.parser')

def retrieve_name():
    x=soup.find(class_="B_NuCI")
    print("The name of the product is: "+x.text.strip())

def retrieve_price():
    x=soup.find(class_="_30jeq3 _16Jk6d")
    print("The price of the product is: "+x.text.strip())

def retrieve_discount():
    x=soup.find(class_="_3Ay6Sb _31Dcoz pZkvcx").find("span")
    print("The discount on the product is: "+x.text.strip())

def retrieve_image():
    x=soup.find_all('img',class_="_2r_T1I _396QI4")
    for img in x:
        print("The discount on the product is: "+img['src'])
    
retrieve_name();
retrieve_price();
retrieve_discount();
retrieve_image();

