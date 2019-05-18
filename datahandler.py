'''
from db import Session
from player import Player
from character import Character
from videogame import Videogame

def get_all_players(session):
    return session.query(Player).all()

def insert_player(session, player):
    session.add(player)

def get_all_characters(session):
    return session.query(Character).all()

def insert_character(session, character):
    session.add(character)
'''

from staginggame import StagingGame as G
from game import Game as Game

def insert_games(session, games):
  for game in games:
    session.add(game)
  session.commit()


def get_games(session):
  return session.query(Game).all()

def get_games_by_eventid(session, eventid):
  return session.query(Game).filter(Game.eventid == str(eventid)).all()