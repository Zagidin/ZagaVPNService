import sys
import subprocess
from color_terminal import Colors


def install_requirements():
    print(f"{Colors.BOLD}{Colors.GREEN} ========== Установка библиотек... ========== {Colors.ENDC}")
    print(f"\n{Colors.BOLD}{Colors.WARNING}[+] Обновление pip{Colors.ENDC}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

    print(f"\n{Colors.BOLD}{Colors.WARNING}[+] Установка зависимостей{Colors.ENDC}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print(f"\n{Colors.BOLD}{Colors.GREEN} ========== Установлено ========== {Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.BOLD}{Colors.FAIL}[+] --- Произошла ошибка: {e} ---{Colors.ENDC}")

if __name__ == "__main__":
    install_requirements()