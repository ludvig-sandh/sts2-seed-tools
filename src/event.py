from act import Act

from typing import List

class EventDB:
    @staticmethod
    def get_events_for_act(act: Act) -> List[str]:
        match act:
            case Act.OVERGROWTH:
                return [
                    "AromaOfChaos",
                    "ByrdonisNest",
                    "DenseVegetation",
                    "JungleMazeAdventure",
                    "LuminousChoir",
                    "MorphicGrove",
                    "SapphireSeed",
                    "SunkenStatue",
                    "TabletOfTruth",
                    "UnrestSite",
                    "Wellspring",
                    "WhisperingHollow",
                    "WoodCarvings"
                ]
            case Act.UNDERDOCKS:
                return [
                    "AbyssalBaths",
                    "DrowningBeacon",
                    "EndlessConveyor",
                    "PunchOff",
                    "SpiralingWhirlpool",
                    "SunkenStatue",
                    "SunkenTreasury",
                    "DoorsOfLightAndDark",
                    "TrashHeap",
                    "WaterloggedScriptorium"
                ]
            case Act.HIVE:
                return [
                    "Amalgamator",
                    "Bugslayer",
                    "ColorfulPhilosophers",
                    "ColossalFlower",
                    "FieldOfManSizedHoles",
                    "InfestedAutomaton",
                    "LostWisp",
                    "SpiritGrafter",
                    "TheLanternKey",
                    "ZenWeaver"
                ]
            case Act.GLORY:
                return [
                    "BattlewornDummy",
                    "GraveOfTheForgotten",
                    "HungryForMushrooms",
                    "Reflections",
                    "RoundTeaParty",
                    "Trial",
                    "TinkerTime"
                ]
            
        raise ValueError("Got nonexistent act")

    @staticmethod
    def get_shared_events() -> List[str]:
        return [
            "BrainLeech",
            "CrystalSphere",
            "DollRoom",
            "FakeMerchant",
            "PotionCourier",
            "RanwidTheElder",
            "RelicTrader",
            "RoomFullOfCheese",
            "SelfHelpBook",
            "SlipperyBridge",
            "StoneOfAllTime",
            "Symbiote",
            "TeaMaster",
            "TheFutureOfPotions",
            "TheLegendsWereTrue",
            "ThisOrThat",
            "WarHistorianRepy",
            "WelcomeToWongos"
        ]
