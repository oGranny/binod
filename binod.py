#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2020 Granny
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import turtle
from turtle import *
import time

i = 0
screensize(5000,5000)
while True:
	print(position())
	home()
	# ~ speed(6)
	# ~ right(90)
	# ~ forward(200)
	# ~ left(90)
	# ~ forward(20)
	# ~ left(90)
	# ~ forward(200)
	# ~ left(90)
	# ~ forward(20)
	# ~ left(180)
	# ~ right(90)
	# ~ forward(200)
	# ~ left(90)
	# ~ forward(20)
	# ~ circle(50, 180)
	# ~ right(180)
	# ~ circle(50, 180)
	# ~ left(90)
	# ~ forward(200)
	# ~ left(90)
	# ~ forward(20)
	# ~ circle(50, 180)
	# ~ right(180)
	# ~ circle(50, 180)
	# ~ forward(20)
	# ~ right(180)
	penup()
	#~~~~~~~~~~~~B~~~~~~~~~~~#
	#############I############
	forward(100)
	pendown()
	forward(100)
	right(90)
	forward(20)
	right(90)
	forward(40)
	left(90)
	forward(160)
	left(90)
	forward(40)
	right(90)
	forward(20)
	right(90)
	forward(100)
	right(90)
	forward(20)
	right(90)
	forward(40)
	left(90)
	forward(160)
	left(90)
	forward(40)
	right(90)
	forward(20)
	penup()
	
	############I#############
	
	#~~~~~~~~~~~N~~~~~~~~~~~~#
	
	right(90)
	forward(200)
	
			
			
	i += 1
	print(f"looped {i} times")
	penup()
	time.sleep(20000000)
	# ~ break
