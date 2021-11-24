import subprocess


def main():
    filename = "requirements.txt"

    with open(filename, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            print(line)
            command = f"pip install { line }"
            subprocess.call(command, shell=True)


if __name__ == "__main__":
    main()
