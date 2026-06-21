import yaml
import json

# Read YAML
with open("knowledge_base/gate_cse/dbms.yaml", "r") as f:
    yaml_data = yaml.safe_load(f)

print("YAML DATA:")
print(yaml_data)

# Read JSON
with open("question_bank/gate_cse/dbms.json", "r") as f:
    json_data = json.load(f)

print("\nJSON DATA:")
print(json_data)