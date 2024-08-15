


def main():
    lineCount = 0
    with open("dracula.txt", "r") as foo, open("vampytimes.txt", "w") as output:
        for line in foo:
            if "vampire" in line.lower():
                lineCount += 1
                output.write(line)  # Write the line to the new file

    print("Total lines: ", lineCount)

main()

