input_messages = open("test input.txt")

read_input = input_messages.read()

output_messages = open("test output.txt")

read_output = output_messages.read()


def main(read_input, adr):

    lines = read_input.split("\n")

    adr_idx = get_idx(lines, adr)

    filtered_messages = []

    for idx in adr_idx:
        filtered_messages.append(get_messages(idx, lines))

    joined_messages = []

    for message in filtered_messages:
        joined_messages.append("\n".join(message))

    output = "\n\n".join(joined_messages)

    return output


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


assert main(read_input, "#penzu") == read_output
