def parsing(commit):

    step1 = commit.replace(": #", "/")

    space_pos = step1.find(" ")

    step2 = step1[:space_pos]+"/"+step1[space_pos+1:].lower()

    step3 = step2.replace(" ", "-")

    print(step3)

print("")

parsing("feat: #OLDM-324 SKLF SKdlfja asldfk")
parsing("fix: #WW-11 improve error handling")

print("")

assert parsing("feat: #OLDM-324 SKLF SKdlfja asldfk") == print("feat/OLDM-324/sklf-skdlfja-asldfk")
assert parsing("fix: #WW-11 improve error handling") == print("fix/WW-11/improve-error-handling")
