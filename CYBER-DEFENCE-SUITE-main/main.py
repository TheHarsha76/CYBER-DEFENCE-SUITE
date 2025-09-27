import os
import time
import sys
from modules import system_info, network_scanner, vuln_scanner

# === Helper Animation Functions ===
def loading_animation(text="Loading", duration=2):
    print(f"\n{text}", end="")
    for _ in range(duration * 4):  # 4 cycles per second
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.25)
    print("\n")

def typing_effect(text, delay=0.04):
    """Simulate typing effect for text output"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Windows = cls, Linux/Mac = clear

# === ASCII Banner ===
def banner():
    clear_screen()  # <<< Make sure old text is gone
    print(r"""
   ______      __                 ____       ____                   
  / ____/_  __/ /_  ___  _____   / __ \___  / __/__  ____  ________ 
 / /   / / / / __ \/ _ \/ ___/  / / / / _ \/ /_/ _ \/ __ \/ ___/ _ \
/ /___/ /_/ / /_/ /  __/ /     / /_/ /  __/ __/  __/ / / / /__/  __/
\____/\__, /_.___/\___/_/     /_____/\___/_/  \___/_/ /_/\___/\___/ 
     /____/                                                         
   _____       _ __     
  / ___/__  __(_) /____ 
  \__ \/ / / / / __/ _ \
 ___/ / /_/ / / /_/  __/
/____/\__,_/_/\__/\___/ 

        🛡️  Cyber Defence Suite - Interactive Menu  🛡️
""")

# === Main Program ===
def main():
    while True:
        banner()
        print("\nSelect an option:")
        print("1. 🖥️  Display System Information")
        print("2. 🌐 Network Scanner")
        print("3. ⚡ Vulnerability Scanner")
        print("4. ❌ Exit")

        choice = input("\n👉 Enter your choice: ")

        if choice == "1":
            loading_animation("Fetching System Information")
            system_info.display_system_info()
            input("\nPress Enter to return to main menu...")

        elif choice == "2":
            # === Network Scanner Loop ===
            while True:
                clear_screen()   # fresh sub-menu
                print("\nChoose Network Scan Mode:")
                print("1. 📡 Scan My Network")
                print("2. 🎯 Scan Custom Range")
                print("3. 🌍 Scan External Server")
                print("4. 🚀 Full Port Scan")
                print("5. 🔙 Back to Main Menu")

                scan_choice = input("\n👉 Enter your choice: ")

                if scan_choice == "1":
                    loading_animation("Scanning Local Network")
                    network_scanner.scan_my_network()

                elif scan_choice == "2":
                    target_range = input("Enter custom IP range (e.g., 192.168.1.0/24): ")
                    loading_animation(f"Scanning Range {target_range}")
                    network_scanner.scan_custom_range(target_range)

                elif scan_choice == "3":
                    external_target = input("Enter external server/domain (e.g., example.com): ")
                    loading_animation(f"Scanning {external_target}")
                    network_scanner.scan_external_server(external_target)

                elif scan_choice == "4":
                    target = input("Enter target IP or domain for full port scan: ")
                    loading_animation(f"Running Full Port Scan on {target}")
                    network_scanner.full_port_scan(target)

                elif scan_choice == "5":
                    typing_effect("🔙 Returning to main menu...", 0.03)
                    break  # Exit Network Scanner loop

                else:
                    typing_effect("⚠️ Invalid choice. Please try again.", 0.03)
                    time.sleep(1)

                input("\nPress Enter to return to Network Scanner menu...")

        elif choice == "3":
            target = input("👉 Enter target IP or domain: ")
            loading_animation(f"Scanning {target} for vulnerabilities")
            vuln_scanner.scan_vulnerabilities(target)
            input("\nPress Enter to return to main menu...")

        elif choice == "4":
            typing_effect("👋 Exiting Cyber Defence Suite. Stay Safe!", 0.03)
            break

        else:
            typing_effect("⚠️ Invalid choice. Please try again.", 0.03)
            time.sleep(1)

if __name__ == "__main__":
    main()
