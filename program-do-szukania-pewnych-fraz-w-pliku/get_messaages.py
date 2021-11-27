messages = open("messages.txt")

read_messages = messages.read()

lines = read_messages.split("\n")


def get_idx(lines, adr):
    adr_idx = []
    for idx, word in enumerate(lines):
        if word == adr:
            adr_idx.append(idx)

    return adr_idx


def get_messages(idx, lines):
    messages_list = []
    for word in lines[idx+1:]:
        if word != "":
            messages_list.append(word)
        else:
            break

    return messages_list


adr_idx = get_idx(lines, "#penzu")

filtered_messages = []

for idx in adr_idx:
    filtered_messages.append(get_messages(idx, lines))

for message in filtered_messages:
    print(" ".join(message))
    print(" ")
