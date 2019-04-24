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


