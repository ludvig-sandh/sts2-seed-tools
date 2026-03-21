from act import Act
from room_type import RoomType

from typing import List
from dataclasses import dataclass, field


@dataclass
class EncounterMetadata:
    name: str
    roomtype: RoomType
    is_weak: bool = False
    tags: list[str] = field(default_factory=list)

ENCOUNTER_METADATA = {
    "AxebotsNormal": EncounterMetadata(name="AxebotsNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "BattlewornDummyEventEncounter": EncounterMetadata(name="BattlewornDummyEventEncounter", roomtype=RoomType.MONSTER, is_weak=False),
    "BowlbugsNormal": EncounterMetadata(name="BowlbugsNormal", roomtype=RoomType.MONSTER, is_weak=False, tags=['Workers']),
    "BowlbugsWeak": EncounterMetadata(name="BowlbugsWeak", roomtype=RoomType.MONSTER, is_weak=True, tags=['Workers']),
    "BygoneEffigyElite": EncounterMetadata(name="BygoneEffigyElite", roomtype=RoomType.ELITE, is_weak=False),
    "ByrdonisElite": EncounterMetadata(name="ByrdonisElite", roomtype=RoomType.ELITE, is_weak=False),
    "CeremonialBeastBoss": EncounterMetadata(name="CeremonialBeastBoss", roomtype=RoomType.BOSS, is_weak=False),
    "ChompersNormal": EncounterMetadata(name="ChompersNormal", roomtype=RoomType.MONSTER, is_weak=False, tags=['Chomper']),
    "ConstructMenagerieNormal": EncounterMetadata(name="ConstructMenagerieNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "CorpseSlugsNormal": EncounterMetadata(name="CorpseSlugsNormal", roomtype=RoomType.MONSTER, is_weak=False, tags=['Slugs']),
    "CorpseSlugsWeak": EncounterMetadata(name="CorpseSlugsWeak", roomtype=RoomType.MONSTER, is_weak=True, tags=['Slugs']),
    "CubexConstructNormal": EncounterMetadata(name="CubexConstructNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "CultistsNormal": EncounterMetadata(name="CultistsNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "DecimillipedeElite": EncounterMetadata(name="DecimillipedeElite", roomtype=RoomType.ELITE, is_weak=False),
    "DenseVegetationEventEncounter": EncounterMetadata(name="DenseVegetationEventEncounter", roomtype=RoomType.MONSTER, is_weak=False),
    "DeprecatedEncounter": EncounterMetadata(name="DeprecatedEncounter", roomtype=RoomType.MONSTER, is_weak=False),
    "DevotedSculptorWeak": EncounterMetadata(name="DevotedSculptorWeak", roomtype=RoomType.MONSTER, is_weak=True),
    "DoormakerBoss": EncounterMetadata(name="DoormakerBoss", roomtype=RoomType.BOSS, is_weak=False),
    "EntomancerElite": EncounterMetadata(name="EntomancerElite", roomtype=RoomType.ELITE, is_weak=False),
    "ExoskeletonsNormal": EncounterMetadata(name="ExoskeletonsNormal", roomtype=RoomType.MONSTER, is_weak=False, tags=['Exoskeletons']),
    "ExoskeletonsWeak": EncounterMetadata(name="ExoskeletonsWeak", roomtype=RoomType.MONSTER, is_weak=True, tags=['Exoskeletons']),
    "FabricatorNormal": EncounterMetadata(name="FabricatorNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "FakeMerchantEventEncounter": EncounterMetadata(name="FakeMerchantEventEncounter", roomtype=RoomType.MONSTER, is_weak=False),
    "FlyconidNormal": EncounterMetadata(name="FlyconidNormal", roomtype=RoomType.MONSTER, is_weak=False, tags=['Mushroom', 'Slimes']),
    "FogmogNormal": EncounterMetadata(name="FogmogNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "FossilStalkerNormal": EncounterMetadata(name="FossilStalkerNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "FrogKnightNormal": EncounterMetadata(name="FrogKnightNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "FuzzyWurmCrawlerWeak": EncounterMetadata(name="FuzzyWurmCrawlerWeak", roomtype=RoomType.MONSTER, is_weak=True, tags=['Crawler']),
    "GlobeHeadNormal": EncounterMetadata(name="GlobeHeadNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "GremlinMercNormal": EncounterMetadata(name="GremlinMercNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "HauntedShipNormal": EncounterMetadata(name="HauntedShipNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "HunterKillerNormal": EncounterMetadata(name="HunterKillerNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "InfestedPrismsElite": EncounterMetadata(name="InfestedPrismsElite", roomtype=RoomType.ELITE, is_weak=False),
    "InkletsNormal": EncounterMetadata(name="InkletsNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "KaiserCrabBoss": EncounterMetadata(name="KaiserCrabBoss", roomtype=RoomType.BOSS, is_weak=False),
    "KnightsElite": EncounterMetadata(name="KnightsElite", roomtype=RoomType.ELITE, is_weak=False, tags=['Knights']),
    "KnowledgeDemonBoss": EncounterMetadata(name="KnowledgeDemonBoss", roomtype=RoomType.BOSS, is_weak=False),
    "LagavulinMatriarchBoss": EncounterMetadata(name="LagavulinMatriarchBoss", roomtype=RoomType.BOSS, is_weak=False),
    "LivingFogNormal": EncounterMetadata(name="LivingFogNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "LouseProgenitorNormal": EncounterMetadata(name="LouseProgenitorNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "MawlerNormal": EncounterMetadata(name="MawlerNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "MechaKnightElite": EncounterMetadata(name="MechaKnightElite", roomtype=RoomType.ELITE, is_weak=False),
    "MysteriousKnightEventEncounter": EncounterMetadata(name="MysteriousKnightEventEncounter", roomtype=RoomType.MONSTER, is_weak=False),
    "MytesNormal": EncounterMetadata(name="MytesNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "NibbitsNormal": EncounterMetadata(name="NibbitsNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "NibbitsWeak": EncounterMetadata(name="NibbitsWeak", roomtype=RoomType.MONSTER, is_weak=True, tags=['Nibbit']),
    "OvergrowthCrawlers": EncounterMetadata(name="OvergrowthCrawlers", roomtype=RoomType.MONSTER, is_weak=False, tags=['Shrinker', 'Crawler']),
    "OvicopterNormal": EncounterMetadata(name="OvicopterNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "OwlMagistrateNormal": EncounterMetadata(name="OwlMagistrateNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "PhantasmalGardenersElite": EncounterMetadata(name="PhantasmalGardenersElite", roomtype=RoomType.ELITE, is_weak=False),
    "PhrogParasiteElite": EncounterMetadata(name="PhrogParasiteElite", roomtype=RoomType.ELITE, is_weak=False),
    "PunchConstructNormal": EncounterMetadata(name="PunchConstructNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "PunchOffEventEncounter": EncounterMetadata(name="PunchOffEventEncounter", roomtype=RoomType.MONSTER, is_weak=False),
    "QueenBoss": EncounterMetadata(name="QueenBoss", roomtype=RoomType.BOSS, is_weak=False),
    "RubyRaidersNormal": EncounterMetadata(name="RubyRaidersNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "ScrollsOfBitingNormal": EncounterMetadata(name="ScrollsOfBitingNormal", roomtype=RoomType.MONSTER, is_weak=False, tags=['Scrolls']),
    "ScrollsOfBitingWeak": EncounterMetadata(name="ScrollsOfBitingWeak", roomtype=RoomType.MONSTER, is_weak=True, tags=['Scrolls']),
    "SeapunkWeak": EncounterMetadata(name="SeapunkWeak", roomtype=RoomType.MONSTER, is_weak=True, tags=['Seapunk']),
    "SewerClamNormal": EncounterMetadata(name="SewerClamNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "ShrinkerBeetleWeak": EncounterMetadata(name="ShrinkerBeetleWeak", roomtype=RoomType.MONSTER, is_weak=True, tags=['Shrinker']),
    "SkulkingColonyElite": EncounterMetadata(name="SkulkingColonyElite", roomtype=RoomType.ELITE, is_weak=False),
    "SlimedBerserkerNormal": EncounterMetadata(name="SlimedBerserkerNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "SlimesNormal": EncounterMetadata(name="SlimesNormal", roomtype=RoomType.MONSTER, is_weak=False, tags=['Slimes']),
    "SlimesWeak": EncounterMetadata(name="SlimesWeak", roomtype=RoomType.MONSTER, is_weak=True, tags=['Slimes']),
    "SlitheringStranglerNormal": EncounterMetadata(name="SlitheringStranglerNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "SludgeSpinnerWeak": EncounterMetadata(name="SludgeSpinnerWeak", roomtype=RoomType.MONSTER, is_weak=True),
    "SlumberingBeetleNormal": EncounterMetadata(name="SlumberingBeetleNormal", roomtype=RoomType.MONSTER, is_weak=False, tags=['Workers']),
    "SnappingJaxfruitNormal": EncounterMetadata(name="SnappingJaxfruitNormal", roomtype=RoomType.MONSTER, is_weak=False, tags=['Mushroom']),
    "SoulFyshBoss": EncounterMetadata(name="SoulFyshBoss", roomtype=RoomType.BOSS, is_weak=False),
    "SoulNexusElite": EncounterMetadata(name="SoulNexusElite", roomtype=RoomType.ELITE, is_weak=False),
    "SpinyToadNormal": EncounterMetadata(name="SpinyToadNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "TerrorEelElite": EncounterMetadata(name="TerrorEelElite", roomtype=RoomType.ELITE, is_weak=False),
    "TestSubjectBoss": EncounterMetadata(name="TestSubjectBoss", roomtype=RoomType.BOSS, is_weak=False),
    "TheArchitectEventEncounter": EncounterMetadata(name="TheArchitectEventEncounter", roomtype=RoomType.MONSTER, is_weak=False),
    "TheInsatiableBoss": EncounterMetadata(name="TheInsatiableBoss", roomtype=RoomType.BOSS, is_weak=False),
    "TheKinBoss": EncounterMetadata(name="TheKinBoss", roomtype=RoomType.BOSS, is_weak=False),
    "TheLostAndForgottenNormal": EncounterMetadata(name="TheLostAndForgottenNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "TheObscuraNormal": EncounterMetadata(name="TheObscuraNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "ThievingHopperWeak": EncounterMetadata(name="ThievingHopperWeak", roomtype=RoomType.MONSTER, is_weak=True, tags=['Thieves']),
    "ToadpolesNormal": EncounterMetadata(name="ToadpolesNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "ToadpolesWeak": EncounterMetadata(name="ToadpolesWeak", roomtype=RoomType.MONSTER, is_weak=True),
    "TunnelerNormal": EncounterMetadata(name="TunnelerNormal", roomtype=RoomType.MONSTER, is_weak=False, tags=['Burrower', 'Workers']),
    "TunnelerWeak": EncounterMetadata(name="TunnelerWeak", roomtype=RoomType.MONSTER, is_weak=True, tags=['Burrower']),
    "TurretOperatorWeak": EncounterMetadata(name="TurretOperatorWeak", roomtype=RoomType.MONSTER, is_weak=True),
    "TwoTailedRatsNormal": EncounterMetadata(name="TwoTailedRatsNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "VantomBoss": EncounterMetadata(name="VantomBoss", roomtype=RoomType.BOSS, is_weak=False),
    "VineShamblerNormal": EncounterMetadata(name="VineShamblerNormal", roomtype=RoomType.MONSTER, is_weak=False),
    "WaterfallGiantBoss": EncounterMetadata(name="WaterfallGiantBoss", roomtype=RoomType.BOSS, is_weak=False),
}

class EncounterDB:
    @staticmethod
    def get_encounters_for_act(act: Act) -> List[str]:
        match act:
            case Act.OVERGROWTH:
                return [
                    "BygoneEffigyElite",
                    "ByrdonisElite",
                    "CeremonialBeastBoss",
                    "CubexConstructNormal",
                    "FlyconidNormal",
                    "FogmogNormal",
                    "FuzzyWurmCrawlerWeak",
                    "InkletsNormal",
                    "MawlerNormal",
                    "NibbitsNormal",
                    "NibbitsWeak",
                    "OvergrowthCrawlers",
                    "PhrogParasiteElite",
                    "RubyRaidersNormal",
                    "ShrinkerBeetleWeak",
                    "SlimesNormal",
                    "SlimesWeak",
                    "SlitheringStranglerNormal",
                    "SnappingJaxfruitNormal",
                    "TheKinBoss",
                    "VantomBoss",
			        "VineShamblerNormal"
                ]
            case Act.UNDERDOCKS:
                return [
                    "CorpseSlugsNormal",
                    "CorpseSlugsWeak",
                    "CultistsNormal",
                    "LivingFogNormal",
                    "FossilStalkerNormal",
                    "GremlinMercNormal",
                    "HauntedShipNormal",
                    "LagavulinMatriarchBoss",
                    "SkulkingColonyElite",
                    "PhantasmalGardenersElite",
                    "PunchConstructNormal",
                    "SeapunkWeak",
                    "SewerClamNormal",
                    "SludgeSpinnerWeak",
                    "SoulFyshBoss",
                    "TerrorEelElite",
                    "ToadpolesNormal",
                    "ToadpolesWeak",
                    "TwoTailedRatsNormal",
                    "WaterfallGiantBoss"
                ]
            case Act.HIVE:
                return [
                    "BowlbugsNormal",
                    "BowlbugsWeak",
                    "ChompersNormal",
                    "DecimillipedeElite",
                    "EntomancerElite",
                    "ExoskeletonsNormal",
                    "ExoskeletonsWeak",
                    "HunterKillerNormal",
                    "KaiserCrabBoss",
                    "InfestedPrismsElite",
                    "KnowledgeDemonBoss",
                    "LouseProgenitorNormal",
                    "MytesNormal",
                    "OvicopterNormal",
                    "SlumberingBeetleNormal",
                    "SpinyToadNormal",
                    "TheInsatiableBoss",
                    "TheObscuraNormal",
                    "ThievingHopperWeak",
                    "TunnelerNormal",
                    "TunnelerWeak"
                ]
            case Act.GLORY:
                return [
                    "AxebotsNormal",
                    "ConstructMenagerieNormal",
                    "DevotedSculptorWeak",
                    "DoormakerBoss",
                    "FabricatorNormal",
                    "FrogKnightNormal",
                    "GlobeHeadNormal",
                    "KnightsElite",
                    "MechaKnightElite",
                    "OwlMagistrateNormal",
                    "QueenBoss",
                    "ScrollsOfBitingNormal",
                    "ScrollsOfBitingWeak",
                    "SlimedBerserkerNormal",
                    "SoulNexusElite",
                    "TestSubjectBoss",
                    "TheLostAndForgottenNormal",
                    "TurretOperatorWeak"
                ]
            
        raise ValueError("Got nonexistent act")


    @staticmethod
    def get_metadata_for_encounter(encounter: str) -> EncounterMetadata:
        try:
            return ENCOUNTER_METADATA[encounter]
        except LookupError:
            raise ValueError(f"Unknown encounter: {encounter}")
        
    @staticmethod
    def get_weak_encounters(act: Act) -> List[str]:
        all_encounters = EncounterDB.get_encounters_for_act(act)
        
        def is_weak_monster(encounter: str):
            metadata = EncounterDB.get_metadata_for_encounter(encounter)
            return metadata.is_weak and metadata.roomtype == RoomType.MONSTER

        return [encounter for encounter in all_encounters if is_weak_monster(encounter)]
        
    @staticmethod
    def get_regular_encounters(act: Act) -> List[str]:
        all_encounters = EncounterDB.get_encounters_for_act(act)
        
        def is_regular_monster(encounter: str):
            metadata = EncounterDB.get_metadata_for_encounter(encounter)
            return not metadata.is_weak and metadata.roomtype == RoomType.MONSTER

        return [encounter for encounter in all_encounters if is_regular_monster(encounter)]
        
    @staticmethod
    def get_elite_encounters(act: Act) -> List[str]:
        all_encounters = EncounterDB.get_encounters_for_act(act)
        
        def is_elite(encounter: str):
            metadata = EncounterDB.get_metadata_for_encounter(encounter)
            return metadata.roomtype == RoomType.ELITE

        return [encounter for encounter in all_encounters if is_elite(encounter)]
        
    @staticmethod
    def get_boss_encounters(act: Act) -> List[str]:
        all_encounters = EncounterDB.get_encounters_for_act(act)
        
        def is_boss(encounter: str):
            metadata = EncounterDB.get_metadata_for_encounter(encounter)
            return metadata.roomtype == RoomType.BOSS

        return [encounter for encounter in all_encounters if is_boss(encounter)]