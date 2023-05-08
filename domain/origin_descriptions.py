# Marvan Tennekoon (mt588), COMP6590 - Practical Project
from enum import Enum

class IgnoredBurial(Enum):
    IMPROPERLY_LAIRED = "an improperly laid to rest spirit, which could be appeased by performing a proper burial ritual"
    FORGOTTEN_GRAVE = "a restless ghost due to a forgotten grave, which can be pacified by cleaning and marking the grave"
    UNBURIED_BODY = "an angry spirit of an unburied body, which can be calmed by finding and burying the remains"


class AncientCurse(Enum):
    CURSED_OBJECT = "a powerful ancient curse, which can be broken by finding and destroying the cursed object"
    FORBIDDEN_ACT = "a deadly curse unleashed by a forbidden act, which can be lifted by making amends for the act"
    ANCIENT_ARTIFACT = "a malediction linked to an ancient artifact, which can be nullified by returning the artifact to its original location"


class UnethicalExperiment(Enum):
    GONE_AWRY = "an unethical experiment gone awry, which may be reversed by finding the scientist's notes and developing an antidote"
    MONSTROUS_CREATURES = "a failed experiment resulting in monstrous creatures, which can be neutralized by destroying the source of their mutation"
    RELEASED_PATHOGEN = "a dangerous experiment that released a pathogen, which can be contained by discovering a cure and administering it to the affected population"


class SupernaturalPortal(Enum):
    ACCIDENTAL_OPENING = "a supernatural portal accidentally opened, which can be closed by performing a sealing ritual"
    DIMENSIONAL_RIFT = "a dimensional rift connecting to another realm, which can be sealed by repairing the damaged energy ley lines"
    OTHERWORLDLY_GATEWAY = "an otherworldly gateway inadvertently activated, which can be shut down by finding and deactivating the artifact that opened it"


class ForbiddenRitual(Enum):
    DARK_FORCES = "a forbidden ritual that unleashed dark forces, which can be stopped by banishing the dark forces using a counter-ritual"
    MALEVOLENT_BEING = "a dark summoning that brought forth a malevolent being, which can be banished by completing a sacred ritual"
    SINISTER_ENERGIES = "an occult ceremony that invoked sinister energies, which can be dispelled by cleansing the area and performing a protective rite"
