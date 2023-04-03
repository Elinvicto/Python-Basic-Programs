#Q19. lkjfkdhffedkjc
with open("Tutorial.rdsf", "r") as file:
    for line in file:
        if line.startswith('#'):
            continue  # skip comments
        line = line.strip()