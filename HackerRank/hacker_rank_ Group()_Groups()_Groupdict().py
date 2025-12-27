import re
task = input()

cases = set(re.findall(r"([a-zA-Z0-9])", task))
cases = "".join(cases)

pattern = f"([{cases}])(?=\\1+)"

matches = re.search(pattern, task)

print(matches.group(1) if matches and matches.group(1) else "-1")