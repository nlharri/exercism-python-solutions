def raindrops(n):
    output = ""
    if (n%3 == 0):
        output = "{}{}".format(output, "Pling")
    if (n%5 == 0):
        output = "{}{}".format(output, "Plang")
    if (n%7 == 0):
        output = "{}{}".format(output, "Plong")
    return "{}".format(n) if output == "" else output
