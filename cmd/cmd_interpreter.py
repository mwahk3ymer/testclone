import cmd

class AirbnbCmd(cmd.Cmd):
    prompt = "AirBnB> "

    def do_create(self, args):
        # Implement the 'create' command logic here
        pass

    def do_show(self, args):
        # Implement the 'show' command logic here
        pass

    def do_update(self, args):
        # Implement the 'update' command logic here
        pass

    def do_quit(self, args):
        # Implement the 'quit' command logic here
        return True

    def do_EOF(self, args):
        # Handle the end-of-file (Ctrl+D) here
        return True

if __name__ == "__main__":
    airbnb_cmd = AirbnbCmd()
    airbnb_cmd.cmdloop()
