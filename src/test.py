from save_manager import SaveManager
from act import Act
from main import start_run


bosses = {
    "A": "VantomBoss",
    "B": "WaterfallGiantBoss",
    "C": "CeremonialBeastBoss",
    "D": "WaterfallGiantBoss",
    "E": "TheKinBoss",
    "F": "LagavulinMatriarchBoss",
    "G": "TheKinBoss",
    "H": "CeremonialBeastBoss",
    "J": "CeremonialBeastBoss",
    "K": "LagavulinMatriarchBoss",
    "L": "LagavulinMatriarchBoss"
}

first_acts = {
    "A": Act.OVERGROWTH,
    "B": Act.UNDERDOCKS,
    "C": Act.OVERGROWTH,
    "D": Act.UNDERDOCKS,
    "E": Act.OVERGROWTH,
    "F": Act.UNDERDOCKS,
    "G": Act.OVERGROWTH,
    "H": Act.OVERGROWTH,
    "J": Act.OVERGROWTH,
    "K": Act.UNDERDOCKS,
    "L": Act.UNDERDOCKS
}

first_relics_from_elites = {
    "A": "GamblingChip",
    "B": "StoneCracker",
    "C": "BloodVial"
}

if __name__ == "__main__":
    progress = SaveManager.load_progress_save_file()
    for seed in bosses.keys():
        run_state = start_run(seed, progress)
        act1 = run_state.acts[0]
        assert act1 == first_acts[seed]
        assert run_state.boss_per_act[act1] == bosses[seed]
    print("Test succeeded")