KEYWORDS = ["root",  "in", "and", "swap", "line"]
    
def fileReader(fileName):
    try:
        with open(fileName, "r") as file:
            data = file.read()
            if data: yield data
    except Exception as error:
        raise Exception(f"Error parsing file: {error}")
    