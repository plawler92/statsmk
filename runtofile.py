import smashtest as s
import json

for i in range(1, 40):
  with open(f"data/smashdata-{i}.json", "w") as f:
    #f.write(s.write_to_file(s.eventSlug, i, 25))
    data = s.write_to_file(s.eventSlug, i, 25)
    json.dump(data, f)