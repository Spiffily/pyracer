#!/bin/env python3

##Modual Imports#######
from math import *
import pygame
from time import *
from random import *
#######################

class GUI():
    def __init__():
        ### Pygame Setup#######
        wd=1200
        ht=600
        pygame.init()
        win = pygame.display.set_mode((wd,ht))
        #######################


#### Line Node ######
class linenode:
    def __init__(self,pos,num):
        self.pos=pos
        self.num=num
        self.slope=linenode.slope(self)
    def drawroads(self):
        if self.num!=0:
                pygame.draw.line(win,(255,200,200),roads['NODE_'+str(self.num-1)].pos,self.pos,3)
    def slope(self):
        if self.num!=0:
            x1,y1=roads['NODE_'+str(self.num-1)].pos
            x2,y2=self.pos
            if x2!=x1:
                slp=-((y1-y2)/(x1-x2))
                return(slp)
            else:
                if y1<y2:
                    return(-256)
                else:
                    return(256)
        else:
            return(0)
#######################

######Curve Node########
class curvenode:
    def __init__(self,pos,num):
        self.pos=pos
        self.num=num
        self.startangle=curvenode.calcStartAngle(self)
        self.endangle=curvenode.calcEndAngle(self)
        self.radius=curvenode.calcRadius(self)
        self.center=curvenode.calcCenter(self)
        self.slope=curvenode.slope(self)
    #######################################Raw INFO##########################################
    def theta1(self):                  ################## angle of previous line
        theta1=atan(roads['NODE_'+str(self.num-1)].slope)
        return(theta1)
    def theta2(self):                  ################## angle of pnt-pnt as to the plane
        if self.num!=0:
            x1,y1=roads['NODE_'+str(self.num-1)].pos
            x2,y2=self.pos
            if x2!=x1:
                slp=-((y1-y2)/(x1-x2))
                theta2=atan(slp)
                return(theta2)
            else:
                if y1<y2:
                    return(atan(-256))
                else:
                    return(atan(256))
        else:
            return(0)
    def theta3(self):            ###################### angle of pnt-pnt as to theta1
        theta3=curvenode.theta2(self)-curvenode.theta1(self)
        return(theta3)
    def Chordlen(self):          ###################### Length of pnt-pnt
        x1,y1=self.pos
        x2,x2=roads['NODE_'+str(self.num-1)].pos
        dist=abs(sqrt((x1-x2)**2+(y1-y2)**2))
        return(dist)
    def theta4(self):
        theta3=curvenode.theta3(self)
        theta4=pi-(2*(theta3-(pi/2)))
        return(theta4)
    ##################################################################################################
    ####################################Tranlated INFO################################################
    def startangle(self):
        theta1=curvenode.theta1(self)
        if theta1>0:
            startangle=theta1-(pi/2)
        else:
            startangle=theta1+(pi/2)
        return(startangle)
    def endangle(self):
        theta3=curvenode.theta3(self)
        theta4=pi-(2*(theta3-(pi/2)))
        endangle=theta4+self.startangle
        return(endangle)


    def drawroads(self):
        x1,y1=roads['NODE_'+str(self.num-1)].pos
        x2,y2=self.pos
        ##### Defining Rect from node to Node ####
        if x1>x2:
            x3=x2
            x4=x1
        else:
            x3=x1
            x4=x2
        if y1>y2:
            y3=y2
            y4=y1
        else:
            y3=y1
            y4=y2
        ###########################################
        pygame.draw.arc(win,(255,200,200),((x3,y3),(x4-x3,y4-y3)),0,2*pi,3)



########################

####Fnct Click #########
def MouseToRoads(RNum,Rtype):
    if event.type == pygame.MOUSEBUTTONDOWN:
            place1=pygame.mouse.get_pos()
            realcords=zoomcalc(place1)
            if Rtype=='line':
                roads['NODE_'+str(RNum)]=linenode(realcords,RNum)
            if Rtype=='curve':
                roads['NODE_'+str(RNum)]=curvenode(realcords,RNum)
            RNum=RNum+1
    return(RNum)
#######################

#######zoom calc########
def zoomcalc(clickcords):
    x,y=clickcords
    finalcords=(x,y)
    return(finalcords)
#######################

#####Draw Roads########
def FDraw():
    for a in roads:
        roads[a].drawroads()
def FDraw2():
    if len(roads)!=0:
        end=len(roads)-1
        pygame.draw.line(win,(0,200,200),roads['NODE_'+str(end)].pos,pygame.mouse.get_pos(),3)
#######################

#### Pre Vars #########
RoadNum=0
roads={}
roadplace1=0
DrawVar='line'
####While loop#########
run = True
while run:
    #######Refresh the screen###
    pygame.display.update()
    pygame.draw.rect(win,(25,25,25),(0,0,wd,ht))
    pygame.draw.arc(win,(0,255,255),(50,50,150,150),3*pi/2,0,3)
    #######Draw roads############
    FDraw()                                                                                 ####### Line 39
    if DrawVar!='none':
        FDraw2()                                                                            ####### Line 39
    ############ Keys pressed###
    keys=pygame.key.get_pressed()
    if keys[pygame.K_l]:
        DrawVar='line'
    if keys[pygame.K_c]:
        DrawVar='curve'
    if keys[pygame.K_ESCAPE]:
        DrawVar='none'
    ############################
    for event in pygame.event.get():
        if DrawVar=='line':
            #######Mouse Click for Drawing roads####
            RoadNum=MouseToRoads(RoadNum,'line')                                                  ####### Line 29
            #####Curve########
        elif DrawVar=='curve':
            RoadNum=MouseToRoads(RoadNum,'curve')                          ##### Place holder
            #######None#########
        else:
            dump=0

        ######Exit Program#########
        if event.type == pygame.QUIT:
            run = False
        ################
#######################
