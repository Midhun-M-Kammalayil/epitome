#from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group


class PollCat(models.Model):
	PCAT_CAT = models.CharField(max_length=100)                            # the category of the poll
	def __str__(self):
		return self.PCAT_CAT


class Polls(models.Model):
	P_CODE = models.CharField(max_length=200)                              # the code of the poll
	P_TITLE = models.CharField(max_length=200)                             # the title of the poll
	P_SHRBODY = models.CharField(max_length=300)                           # the short body of the poll
	P_BODY = models.CharField(max_length=1000)                             # the body (main text) of the poll
	P_CREATION = models.DateTimeField(default = timezone.now())            # the creation date and time of the poll
	P_STARTDT = models.DateTimeField()                                     # the starting date and time of the poll
	P_ENDDT = models.DateTimeField()                                       # the ending date and time of the poll
	P_DURATION = models.IntegerField(default=0)                            # the duration of the poll
	P_CODE2 = models.CharField(max_length=200, blank = True)               # the code2 of the poll (protocol number, approval number)
	USER_CREATORID = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # the user (admin) who created the poll
	UGRP_GROUPID = models.ForeignKey(Group, on_delete=models.DO_NOTHING)   # the group of the user that created the poll
	PCAT_CAT = models.ForeignKey(PollCat, on_delete=models.DO_NOTHING)     # the category of the poll
	def __str__(self): 
		return "%s %s" % (self.P_TITLE, self.P_SHRBODY)


class PollChoice(models.Model):
	polls = models.ForeignKey(Polls, related_name='PChoice', on_delete=models.DO_NOTHING)  # key to Polls table
	PCHOICE_CHOICE = models.CharField(max_length=100)                                      # the vote choice
	PCHOICE_VOTES = models.IntegerField(default=0)                                         # the number of votes
	def __str__(self):
		return self.PCHOICE_CHOICE


class Voter(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	Polls = models.ForeignKey(Polls, on_delete=models.DO_NOTHING)


class Issues(models.Model):
	IS_CODE = models.CharField(max_length=200)                             # the code of the issue
	IS_TITLE = models.CharField(max_length=200)                            # the title of the issue
	IS_SHRBODY = models.CharField(max_length=300)                          # the short body of the issue
	IS_BODY = models.CharField(max_length=1000)                            # the body (main text) of the issue
	IS_CREATION = models.DateTimeField(default = timezone.now())           # the creation date and time of the issue
	IS_CODE2 = models.CharField(max_length=200, blank = True)              # the code2 of the issue (protocol number, approval number)
	USER_CREATORID = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # the user (admin) who created the issue
	UGRP_GROUPID = models.ForeignKey(Group, on_delete=models.DO_NOTHING)   # the group of the user that created the issue
	def __str__(self): 
		return "%s %s" % (self.IS_TITLE, self.IS_SHRBODY)


class Evidence(models.Model):
	E_FLD1 = models.CharField(max_length=1000)                             # What has happened?
	E_FLD2 = models.CharField(max_length=1000)                             # Why is it important?
	E_FLD3 = models.CharField(max_length=1000)                             # Who has been affected?
	E_FLD4 = models.CharField(max_length=1000)                             # How and why did it happen?
	E_FLD5 = models.CharField(max_length=1000)                             # Where did it occur?
	E_FLD6 = models.CharField(max_length=1000)                             # When did it occur?
	E_FLD7 = models.CharField(max_length=1000)                             # How much is the cost?
	E_FLD8 = models.CharField(max_length=1000)                             # How long did it last?
	Issue = models.ForeignKey(Issues, on_delete=models.DO_NOTHING)         # key to Issues table
