#!/usr/bin/env python3

# -*- coding: utf-8 -*-
#
#  binod.py
#  
#  Copyright 2020 oGranny
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
screensize(2000,2000)
while True:
	home()
	speed(1)
	right(90)
	forward(200)
	left(90)
	forward(20)
	left(90)
	forward(200)
	left(90)
	forward(20)
	left(180)
	right(90)
	forward(200)
	left(90)
	forward(20)
	circle(50, 180)
	right(180)
	circle(50, 180)
	left(90)
	forward(200)
	left(90)
	forward(20)
	circle(50, 180)
	right(180)
	circle(50, 180)
	forward(20)
	right(180)
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
	forward(150)
	pendown()
	right(90)
	forward(200)
	left(90)
	forward(20)
	left(90)
	forward(150)
	right(160)
	forward(160)
	left(70)
	forward(20)
	left(90)
	forward(200)
	left(90)
	forward(20)
	left(90)
	forward(150)
	right(160)
	forward(160)
	left(70)
	forward(20)
	penup()
	############N#############
	
	#~~~~~~~~~~~O~~~~~~~~~~~~#

	right(180)
	forward(135)
	right(90)
	forward(100)
	pendown()
	circle(100, 360)
	penup()
	forward(80)
	left(90)
	forward(100)
	pendown()
	circle(80, 360)
	penup()
	############O##############
	
	#~~~~~~~~~~~D~~~~~~~~~~~~~#
	right(90)
	forward(20)
	left(90)
	forward(150)
	pendown()
	right(180)
	forward(20)
	right(90)
	forward(200)
	right(90)
	forward(20)
	penup()
	right(90)
	forward(200)
	pendown()
	left(90)
	circle(100, 180)
	left(90)
	penup()
	forward(20)
	pendown()
	forward(160)
	left(90)
	circle(80, 180)
	#############D############



	i += 1
	print(f"looped {i} times")
	penup()
	# ~ break
