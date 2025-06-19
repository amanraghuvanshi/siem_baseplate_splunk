import yaml
from pathlib import Path

def load_rules():
    with open(Path(__file__).parent / "rules.yaml", "r") as rule_file:
        return yaml.safe_load(rule_file)["rules"]
    
def match_rules(log: dict, rule: dict) -> bool:
    for key, expected in rule.get("match", {}).items():
        if str(log.get(key, "")).lower() != str(expected).lower():
            return False
    return True