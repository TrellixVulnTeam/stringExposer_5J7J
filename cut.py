def add_title():
    with open('strings.txt', 'r') as original: data = original.read()
    with open('strings.txt', 'w') as modified: modified.write("HEADER LINE NOT PART OF EXTRACTED STRINGS\n" + data)

def remove_title():
    with open('strings.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('strings.txt', 'w') as fout:
        fout.writelines(data[1:])

add_title()


remove_title()

