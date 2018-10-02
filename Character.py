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
	DeathSucces=0
	DeathFail=0
	
	def __init__(self,str=0,dex=0,con=0,int=0,wis=0,cha=0,name="character",Class=[["Fighter",1]],race="Human",inv=[],feat=[],lang=["common"],mon=[0,0,0,0],ab=[],spells=[],skills=[]):
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
			if values != None:
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
		for i in self.Class:
			value=i[0]+str(i[1])
			s+=value
			for v in self.Class[1:]:
				value=v[0]+str(v[1])
				s+=","
				s+=v
		s+=":"
		if len(self.Inventory)>0:
			s+=self.Inventory[0]
			for i in self.Inventory[1:]:
				s+=","
				s+=i
			s+=":"
		s+=str(self.Money[0])+","
		s+=str(self.Money[1])+","
		s+=str(self.Money[2])+","
		s+=str(self.Money[3])+":"
		s+=self.Languages[0]
		for i in self.Languages[1:]:
			s+=","+i
		s+=":"
		#abilities
		#skills
		#saves
		#feats
		#XP
		#HP
		#CurrentHP
		#background
		print(s)
	
	def takeDamage(self,Damage):
		self.CurrentHP-=Damage
		if self.CurrentHP<0:
			self.CurrentHP=0
		#check for 0 and do something
	
	def LongRest(self):
		self.CurrentHP=self.HP
	
	def ShortRest(self):
		return
	
	def LvlUp(self):
		return
		
class Create:
	
		
char=Character(inv=["stuff"])
char.out("t")
		
		
		
		