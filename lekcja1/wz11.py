#!/usr/bin/env python3
import math as m
góra=   [" ___________________________"]
funkcje=["|alpha|  30  |  45  |  60  |"]
dół =   ["***************************"]
sin= [" sin  | " + str(round(m.sin(m.radians(30)),2))+"  |"+
str(round(m.sin(m.radians(45)),2))+"  |"+ str(round(m.sin(m.radians(60)),2))+"  |"]
cos= [" cos  | " + str(round(m.cos(m.radians(30)),2))+" |"+
str(round(m.cos(m.radians(45)),2))+"  |"+ str(round(m.cos(m.radians(60)),2))+"   |"]
tg= [" tan  | " + str(round(m.tan(m.radians(30)),2))+" |"+
str(round(m.tan(m.radians(45)),2))+"   |"+ str(round(m.tan(m.radians(60)),2))+"  |"]
ctg= [" tan  | " + str(round(1/m.tan(m.radians(30)),2))+" |"+
str(round(1/m.tan(m.radians(45)),2))+"   |"+ str(round(1/m.tan(m.radians(60)),2))+"  |"]
print(f"{góra}\n{funkcje}\n{dół} \n{sin}\n{dół}\n{cos}\n{dół}\n{tg}\n{dół}\n{ctg}\n{dół}")