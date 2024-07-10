def loot_command(loot, commands):
    treasur_chest = loot.split('|')

    for command in commands:
        parts = command.split()
        action = parts[0]

        if action == "Loot":
            items = parts[1:]
            for item in items:
                if item not in treasur_chest:
                    treasur_chest.insert(0, item)

        elif action == "Drop":
            index = int(parts[1])
            if 0 <= index < len(treasur_chest):
                item = treasur_chest.pop(index)
                treasur_chest.append(item)

        elif action == "Steal":
            count = int(parts[1])
            stolen_items = []
            if count >= len(treasur_chest):
                stolen_items = treasur_chest
                treasur_chest = []
            else:
                stolen_items = treasur_chest[-count:]
                treasur_chest = treasur_chest[:-count]
            print(", ".join(stolen_items))

    if treasur_chest:
        total_length = sum(len(item) for item in treasur_chest)
        average_gain = total_length / len(treasur_chest)
        print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
    else:
        print("Failed treasure hunt.")

loot1 = input()
command = []
while True:
    command1 = input()
    if command1 == "Yohoho!":
        break
    command.append(command1)

loot_command(loot1, command)