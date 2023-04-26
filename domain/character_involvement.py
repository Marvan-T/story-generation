from enum import Enum


class CharacterInvolvement(Enum):
    PROTAGONIST = "protagonist"
    INVOLVED_IN_ORIGIN = "involved in the horror origin"
    WITNESS = "witness"
    TRIED_TO_STOP = "tried to stop the event"
    INDIRECTLY_AFFECTED = "indirectly affected by the event"
    KNOW_A_SECRET = "know a secret about the event"
    VICTIM = "victim"
