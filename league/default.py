from enum import Enum
from typing import Tuple

import nextcord

from . import Constructor, Driver, Track


def HEX_TO_RGB(h: str) -> Tuple[int]:
    h = h[2:] if h.startswith("0x") else h
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


class Constructors(Enum):
    RED_BULL = Constructor("Oracle Red Bull Racing", nextcord.Colour.from_rgb(*HEX_TO_RGB("0x515ece")),
                           description="The default \"Oracle Red Bull Racing\" Formula 1 constructor"
                           )
    FERRARI = Constructor("Scuderia Ferrari", nextcord.Colour.from_rgb(*HEX_TO_RGB("0xed1c24")),
                          description="The default \"Scuderia Ferrari\" Formula 1 constructor"
                          )
    MERCEDES = Constructor("Mercedes-AMG Petronas F1 Team", nextcord.Colour.from_rgb(*HEX_TO_RGB("0x37bdad")),
                           description="The default \"Mercedes-AMG Petronas F1 Team\" Formula 1 constructor"
                           )
    ALPINE = Constructor("BWT Alpine F1 Team", nextcord.Colour.from_rgb(*HEX_TO_RGB("0x1e68cd")),
                         description="The default \"BWT Alpine F1 Team\" Formula 1 constructor"
                         )
    MCLAREN = Constructor("McLaren F1 Team", nextcord.Colour.from_rgb(*HEX_TO_RGB("0xf158020")),
                          description="The default \"McLaren F1 Team\" Formula 1 constructor"
                          )
    ALFA_ROMEO = Constructor("Alfa Romeo F1 Team ORLEN", nextcord.Colour.from_rgb(*HEX_TO_RGB("0xb12039")),
                             description="The default \"Alfa Romeo F1 Team ORLEN\" Formula 1 constructor"
                             )
    ASTON_MARTIN = Constructor("Aston Martin Aramco Cognizant F1 Team",
                               nextcord.Colour.from_rgb(*HEX_TO_RGB("0x206b63")),
                               description="The default \"Aston Martin Aramco Cognizant F1 Team\" Formula 1 constructor"
                               )
    HAAS = Constructor("Haas F1 Team", nextcord.Colour.from_rgb(*HEX_TO_RGB("0xb6babd")),
                       description="The default \"Haas F1 Team\" Formula 1 constructor"
                       )
    ALPHA_TAURI = Constructor("Scuderia AlphaTauri", nextcord.Colour.from_rgb(*HEX_TO_RGB("0x4b698e")),
                              description="The default \"Scuderia AlphaTauri\" Formula 1 constructor"
                              )
    WILLIAMS = Constructor("Williams Racing", nextcord.Colour.from_rgb(*HEX_TO_RGB("0x1597d3")),
                           description="The default \"Williams Racing\" Formula 1 constructor"
                           )


class Drivers(Enum):
    LECLERC = Driver("Charles", "Leclerc", default_constructor=Constructors.FERRARI.value)
    SAINZ = Driver("Carlos", "Sainz", default_constructor=Constructors.FERRARI.value)
    HAMILTON = Driver("Lewis", "Hamilton", default_constructor=Constructors.MERCEDES.value)
    RUSSELL = Driver("George", "Russell", default_constructor=Constructors.MERCEDES.value)
    VERSTAPPEN = Driver("Max", "Verstappen", default_constructor=Constructors.RED_BULL.value)
    PEREZ = Driver("Sergio", "Perez", default_constructor=Constructors.RED_BULL.value)
    NORRIS = Driver("Lando", "Norris", default_constructor=Constructors.MCLAREN.value)
    RICCIARDO = Driver("Daniel", "Ricciardo", default_constructor=Constructors.MCLAREN.value)
    VETTEL = Driver("Sebastian", "Vettel", default_constructor=Constructors.ASTON_MARTIN.value)
    STROLL = Driver("Lance", "Stroll", default_constructor=Constructors.ASTON_MARTIN.value)
    ALONSO = Driver("Fernando", "Alonso", default_constructor=Constructors.ALPINE.value)
    OCON = Driver("Esteban", "Ocon", default_constructor=Constructors.ALPINE.value)
    TSUNODA = Driver("Yuki", "Tsunoda", default_constructor=Constructors.ALPHA_TAURI.value)
    GASLY = Driver("Pierre", "Gasly", default_constructor=Constructors.ALPHA_TAURI.value)
    BOTTAS = Driver("Valterri", "Bottas", default_constructor=Constructors.ALFA_ROMEO.value)
    ZHOU = Driver("Guanyu", "Zhou", default_constructor=Constructors.ALFA_ROMEO.value)
    MAGNUSSEN = Driver("Kevin", "Magnussen", default_constructor=Constructors.HAAS.value)
    SCHUMACHER = Driver("Mick", "Schumacher", default_constructor=Constructors.HAAS.value)
    LATIFI = Driver("Nicholas", "Latifi", default_constructor=Constructors.WILLIAMS.value)
    ALBON = Driver("Alexander", "Albon", default_constructor=Constructors.WILLIAMS.value)


class Tracks(Enum):
    BAHRAIN = Track("Bahrain International Circuit", "Bahrain", 5_412)
    SAUDI_ARABIA = Track("Jeddah Corniche Circuit", "Saudi Arabia", 6_174)
    AUSTRALIA = Track("Albert Park Circuit", "Australia", 5_278)
    EMILIA_ROMAGNA = Track("Autodromo Enzo e Dino Ferrari", "Italy", 4_909)
    MIAMI = Track("Miami International Autodrome", "USA", 5_412)
    SPAIN = Track("Circuit de Barcelona-Catalunya", "Spain", 4_675)
    MONACO = Track("Circuit de Monaco", "Monaco", 3_337)
    AZERBAIJAN = Track("Baku City Circuit", "Azerbaijan", 6_003)
    CANADA = Track("Circuit Gilles-Villeneuve", "Canada", 4_361)
    GREAT_BRITAIN = Track("Silverstone Circuit", "UK", 5_891)
    AUSTRIA = Track("Red Bull Ring", "Austria", 4_318)
    FRANCE = Track("Circuit Paul Ricard", "France", 5_842)
    HUNGARY = Track("Hungaroring", "Hungary", 4_381)
    BELGIUM = Track("Circuit de Spa-Francorchamps", "Belgium", 7_004)
    THE_NETHERLANDS = Track("Circuit Zandvoort", "The Netherlands", 4_259)
    ITALY = Track("Autodromo Nazionale Monza", "Italy", 5_793)
    SINGAPORE = Track("Marina Bay Street Circuit", "Singapore", 5_063)
    JAPAN = Track("Suzuka International Racing Course", "Japan", 5_807)
    USA = Track("Circuit of The Americas", "USA", 5_513)
    MEXICO = Track("Autódromo Hermanos Rodríguez", "Mexico", 4_304)
    BRAZIL = Track("Autódromo José Carlos Pace", "Brazil", 4_309)
    ABU_DHABI = Track("Yas Marina Circuit", "Abu Dhabi", 5_281)
    CHINA = Track("Shanghai International Circuit", "China", 4_603)
    PORTUGAL = Track("Algarve International Circuit", "Portugal", 4_592)
