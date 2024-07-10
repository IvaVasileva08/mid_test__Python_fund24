def process_commands(targets, commands):
    for command in commands:
        parts = command.split()
        action = parts[0]

        if action == "Shoot":
            index = int(parts[1])
            power = int(parts[2])
            if 0 <= index < len(targets):
                targets[index] -= power
                if targets[index] <= 0:
                    targets.pop(index)

        elif action == "Add":
            index = int(parts[1])
            value = int(parts[2])
            if 0 <= index <= len(targets):
                targets.insert(index, value)
            else:
                print("Invalid placement!")

        elif action == "Strike":
            index = int(parts[1])
            radius = int(parts[2])
            start = index - radius
            end = index + radius
            if start >= 0 and end < len(targets):
                del targets[start:end + 1]
            else:
                print("Strike missed!")

    print("|".join(map(str, targets)))

initial_targets = list(map(int, input().split()))
commands = []
while True:
    command = input()
    if command == "End":
        break
    commands.append(command)
process_commands(initial_targets, commands)