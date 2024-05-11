def check_command_file(file_path):
    with open(file_path, "r", encoding="utf-8", errors="replace") as file:
        line_number = 0
        for line in file:
            line_number += 1
            line = line.strip()
            if line and " = " not in line:
                print(f"Invalid format in line {line_number}: {line}")

file_path = "TXT Files/allday_commands.txt"  # Update this to your file path
check_command_file(file_path)
