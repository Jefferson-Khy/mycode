
def main():
    # main.py
    with open('coolpeeps.txt', 'r') as file:
        file_content = file.read()

    # Convert the string content to a dictionary
    exec(file_content)

    # Now coolpeeps should be available as a dictionary
    print(file)
    print(file["all"][0]["First"])
    
main()
