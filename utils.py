import os


class Utils:
    def __init__(self):
        self.system = os.name

    def _clear_screen(self):
        operating_system = self.system
        if operating_system == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def _draw_bar(self, curr_val, max_val, status="", bar_length=25):
        filled = int(bar_length * curr_val / max_val)
        empty = bar_length - filled
        bar = "█" * filled + "-" * empty

        if status == "hunger":
            percent = curr_val / max_val
            if percent >= 0.8:
                color = "\033[91m"  # red
            elif percent >= 0.5:
                color = "\033[93m"  # yellow
            else:
                color = "\033[92m"  # green
        else:
            percent = curr_val / max_val
            if percent <= 0.5:
                color = "\033[91m"  # red
            elif percent <= 0.8:
                color = "\033[93m"  # yellow
            else:
                color = "\033[92m"  # green

        return f"{color}{bar}\033[0m"
