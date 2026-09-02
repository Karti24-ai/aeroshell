import os
import sys
import subprocess
import platform
from datetime import datetime

# Standard ANSI Terminal Escape Color Codes
COLOR_RESET  = "\033[0m"
COLOR_BOLD   = "\033[1m"
COLOR_CYAN   = "\033[36m"
COLOR_GREEN  = "\033[32m"
COLOR_RED    = "\033[31m"

class AeroShell:
    def __init__(self):
        self.username = os.getlogin()
        self.hostname = platform.node()
        self.active_directory = os.path.expanduser("~")
        os.chdir(self.active_directory)
        
    def render_welcome_banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        current_time = datetime.now().strftime('%a %b %d %H:%M:%S')
        print(f"Last login: {current_time} on ttys000")
        print(f"AeroShell Environment Core {COLOR_CYAN}v1.4.4{COLOR_RESET}")
        print("Type 'help' for internal system commands or 'kget [app]' for global downloads.\n")

    def handle_custom_installer(self, app_name: str):
        """Dynamic package manager that intercepts text and handles status codes"""
        app_database = {
            "chrome": "Google.Chrome",
            "python": "Python.Python.3.12",
            "git": "Git.Git",
            "notepad++": "Notepad++.Notepad++",
            "node": "OpenJS.NodeJS",
            "vscode": "Microsoft.VisualStudioCode",
            "steam": "Valve.Steam",
            "discord": "Discord.Discord"
        }
        
        target_app = app_name.lower()
        winget_target = app_database[target_app] if target_app in app_database else app_name
        
        print(f"\n{COLOR_GREEN}==> kget: Initiating global distribution query for target: '{winget_target}'{COLOR_RESET}")
        print(f"{COLOR_GREEN}==> kget: Contacting remote repositories...{COLOR_RESET}\n")
        
        try:
            process = subprocess.Popen(
                ["winget", "install", winget_target, "--silent", "--accept-source-agreements", "--accept-package-agreements"],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="ignore"
            )
            
            while True:
                line = process.stdout.readline()
                if not line and process.poll() is not None:
                    break
                if line:
                    if "Microsoft is not responsible" in line:
                        line = line.replace("Microsoft is not responsible", "KGet is not responsible")
                    print(line, end="")
            
            # Catch both absolute success (0) and up-to-date system warning hex codes (2316632107 / -1978335189)
            if process.returncode in [0, 2316632107, -1978335189]:
                print(f"\n{COLOR_GREEN}==> kget: Success! '{app_name}' is fully configured and up to date.{COLOR_RESET}\n")
            else:
                print(f"\n{COLOR_RED}Error: Global installation pipeline closed with code {process.returncode}{COLOR_RESET}\n")
                
        except Exception as e:
            print(f"{COLOR_RED}Error: Global installation pipeline failed: {e}{COLOR_RESET}\n")

    def execute_system_command(self, raw_input_string: str):
        tokens = raw_input_string.strip().split()
        if not tokens:
            return

        command_key = tokens[0].lower()

        if command_key == "kget":
            if len(tokens) > 1:
                self.handle_custom_installer(" ".join(tokens[1:]))
            else:
                print(f"\n{COLOR_RED}Error: Missing required argument. Usage: kget [package_name]{COLOR_RESET}\n")
            return

        elif command_key == "exit":
            print("\n[Process completed]")
            sys.exit(0)
            
        elif command_key == "help":
            print(f"\n{COLOR_BOLD}AeroShell Core Commands:{COLOR_RESET}")
            print(f"  help              Display this system configuration reference index.")
            print(f"  clear / cls       Flush current shell window display streams.")
            print(f"  kget [any_app]    Natively install any global application in the world.")
            print(f"  neofetch          Query system kernel architecture metadata fields.")
            print(f"  cd [path]         Modify environment context directory pointers.")
            print(f"  exit              Terminate terminal process execution loop.\n")
            return

        elif command_key in ["clear", "cls"]:
            os.system('cls' if os.name == 'nt' else 'clear')
            return

        elif command_key == "neofetch":
            print(f"\n   /\\_/\\_      {COLOR_BOLD}OS:{COLOR_RESET} {platform.system()} {platform.release()}")
            print(f"  ( o.o )     {COLOR_BOLD}Kernel:{COLOR_RESET} {platform.version()}")
            print(f"   > ^ <      {COLOR_BOLD}Shell:{COLOR_RESET} AeroShell Core v1.4.4")
            print(f"  /     \\     {COLOR_BOLD}Uptime:{COLOR_RESET} Local machine runtime sync active")
            print(f" |       |    {COLOR_BOLD}User Context:{COLOR_RESET} {self.username}@{self.hostname}\n")
            return

        elif command_key == "cd":
            target_path = " ".join(tokens[1:]) if len(tokens) > 1 else os.path.expanduser("~")
            try:
                os.chdir(target_path)
                self.active_directory = os.getcwd()
            except Exception as error:
                print(f"{COLOR_RED}cd: {error}{COLOR_RESET}")
            return

        else:
            try:
                subprocess.run(raw_input_string, shell=True, text=True)
            except Exception as critical_error:
                print(f"{COLOR_RED}Shell execution failure: {critical_error}{COLOR_RESET}")

    def boot_interactive_loop(self):
        self.render_welcome_banner()
        while True:
            try:
                short_dir = self.active_directory.replace(os.path.expanduser("~"), "~")
                prompt_string = f"{self.username}@{self.hostname} {COLOR_CYAN}{short_dir}{COLOR_RESET} % "
                user_entry = input(prompt_string)
                self.execute_system_command(user_entry)
            except (KeyboardInterrupt, EOFError):
                print(f"\n\n{COLOR_RED}Signal break captured. Type 'exit' to terminate shell process.{COLOR_RESET}")
                continue

if __name__ == "__main__":
    os.system("")
    shell_instance = AeroShell()
    shell_instance.boot_interactive_loop()
