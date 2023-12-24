import json, requests, os

valid = 0

if os.path.exists('utils/output.txt'):
    os.remove('utils/output.txt')

with open("utils/config.json", "r") as file:
    data = json.load(file)

try:
    with open("utils/" + data.get("main", {}).get("settings", {}).get("Links"), "r") as file:
        lines = file.readlines()

    if len(lines) <= 0:
        print('Error: Please check your links file! Not load proxy links')
    else:
        print(f"Loaded links: {len(lines)} : Checked 0/{len(lines)}")
        with open('utils/output.txt', "w") as output_file:
            for line in lines:
                try:
                    response = requests.get(line.strip())
                    if response.status_code == 200:
                        content = response.text
                        output_file.write(content)
                        valid += 1

                        print(f'{line.strip()} : 200 Successful : {valid}/{len(lines)}')
                    else:
                        print(f'{line.strip()} : Not valid')
                except Exception as e:
                    print(f"Error: {e}")

except FileNotFoundError:
    print('Error: Please check your links file! File not found')
