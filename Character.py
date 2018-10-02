#!/usr/bin/env python3


classSaveDict=dict()

class Character:
	Str=0
	Dex=0
	Con=0
	Int=0
	Wis=0
	Cha=0
	Name=""
	Class=[["",0]]
	Race=""
	Inventory=[]
	Feats=[]
	Languages=[]
	Money=[[0],[0],[0],[0]]
	Abilities=[]
	Spells=[]
	Skills=[]
	Saves= set()
	XP=0
	speed=30
	AC=0
	HP=0
	CurrentHP=0
	Background=""
	Proficency=""
	
	def __init__(self,str=0,dex=0,con=0,int=0,wis=0,cha=0,name="character",Class=[["Fighter",1]],race="Human",inv=[],feat=[],lang=["common"],mon=[[0],[0],[0],[0]],ab=[],spells=[],skills=[]):
		self.Str=str
		self.Dex=dex
		self.Con=con
		self.Int=int
		self.Wis=wis
		self.Cha=cha
		self.Name=name
		self.Class=Class
		self.Race=race
		self.Inventory=inv
		self.Feats=feat
		self.Languages=lang
		self.Money=mon
		self.Abilities=ab
		self.Spells=spells
		self.Skills=skills
		for i in self.Class:
			values=classSaveDict.get(i[0])
			for v in values:
				self.Saves.add(v)
	
	def out(self,fileName):
		s=""
		s+=(self.Name+":")
		s+=str(self.Str)+":"
		s+=str(self.Dex)+":"
		s+=str(self.Con)+":"
		s+=str(self.Int)+":"
		s+=str(self.Wis)+":"
		s+=str(self.Cha)+":"
		s+=self.Race+":"
	
	def LongRest(self):
		return
	def ShortRest(self):
		return
	def LvlUp(self):
		return
		
		
		
		