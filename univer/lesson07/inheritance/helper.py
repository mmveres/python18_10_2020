class Helper:
    def save_human_to_file(humans, filename="humans.txt"):
        with open(filename, "w") as humans_data:
            for human in humans:
                humans_data.write(human.__str__())
                humans_data.write("\n")