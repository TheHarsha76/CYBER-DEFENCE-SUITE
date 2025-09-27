import nmap
import ipaddress
import socket
import subprocess
import sys
import os

# Function to scan local network automatically
def scan_my_network():
    try:
        # Detect local IP
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        network = str(ipaddress.IPv4Network(local_ip + "/24", strict=False))

        print(f"\n🔍 Detected Local Network: {network}")
        scan_custom_range(network)

    except Exception as e:
        print(f"❌ Error detecting local network: {e}")


# Function to scan a custom IP range
def scan_custom_range(target_range):
    print(f"\n🚀 Scanning IP Range: {target_range}")
    try:
        result = subprocess.check_output(["nmap", "-sn", target_range], text=True)
        print(result)
    except Exception as e:
        print(f"❌ Error scanning range: {e}")


# Function to scan an external server
def scan_external_server(target):
    print(f"\n🌍 Scanning External Server: {target}")
    try:
        result = subprocess.check_output(["nmap", "-Pn", target], text=True)
        print(result)
    except Exception as e:
        print(f"❌ Error scanning external server: {e}")


# -------- Utility Functions -------- #
def get_local_ip():
    """Get the local IP address of the machine."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "Unable to determine local IP"


# -------- Core Scan Functions -------- #
def scan_target(target):
    """Perform a network scan on the given target."""
    nm = nmap.PortScanner()
    print(f"\n[+] Scanning target: {target}\n")

    try:
        nm.scan(hosts=target, arguments='-sn')  # -sn = ping scan
        for host in nm.all_hosts():
            print(f"Host: {host} ({nm[host].hostname()}) - State: {nm[host].state()}")

            if nm[host].state() == "up":
                print(f"  -> Scanning ports on {host}...\n")
                nm.scan(hosts=host, arguments='-sV --top-ports 20')

                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()
                    for port in sorted(lport):
                        state = nm[host][proto][port]["state"]
                        name = nm[host][proto][port]["name"]
                        product = nm[host][proto][port].get("product", "")
                        version = nm[host][proto][port].get("version", "")
                        extra = f"{product} {version}".strip()
                        print(f"     Port {port}/{proto} - {state} - {name} {extra}")

    except Exception as e:
        print(f"[!] Error scanning target {target}: {e}")


def full_port_scan(target):
    """Perform a full port scan on the given target."""
    nm = nmap.PortScanner()
    print(f"\n⚡ Full Port Scan on {target}")

    choice = input("\nChoose scan type:\n1. 🔎 Top 1000 Ports\n2. 🚀 All 65535 Ports\n👉 ").strip()

    if choice == "1":
        arguments = "-sV --top-ports 1000"
        print("\n[+] Scanning top 1000 ports...")
    elif choice == "2":
        arguments = "-sV -p-"
        print("\n[+] Scanning ALL 65535 ports (this may take a while)...")
    else:
        print("⚠️ Invalid choice. Returning to Network Scanner menu.")
        return

    try:
        nm.scan(hosts=target, arguments=arguments)
        for host in nm.all_hosts():
            print(f"\nHost: {host} ({nm[host].hostname()}) - State: {nm[host].state()}")

            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    state = nm[host][proto][port]["state"]
                    name = nm[host][proto][port]["name"]
                    product = nm[host][proto][port].get("product", "")
                    version = nm[host][proto][port].get("version", "")
                    extra = f"{product} {version}".strip()
                    print(f"     Port {port}/{proto} - {state} - {name} {extra}")

    except Exception as e:
        print(f"[!] Error scanning target {target}: {e}")

    input("\nPress Enter to return to Network Scanner menu...")  # ✅ stays inside scanner menu


# -------- Network Scanner Menu -------- #
def network_scanner_menu():
    while True:
        print("\n=== 🌐 Network Scanner ===")
        print("1. 📡 Scan my local network")
        print("2. 🎯 Scan a custom IP or range")
        print("3. 🌍 Scan an external server (like google.com)")
        print("4. 🚀 Full Port Scan")
        print("5. 🔙 Back to Main Menu")

        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            scan_my_network()
            input("\nPress Enter to return to Network Scanner menu...")

        elif choice == "2":
            target = input("Enter target IP or range: ").strip()
            scan_custom_range(target)
            input("\nPress Enter to return to Network Scanner menu...")

        elif choice == "3":
            domain = input("Enter domain (e.g., google.com): ").strip()
            try:
                ip = socket.gethostbyname(domain)
                scan_external_server(ip)
            except socket.gaierror:
                print("[!] Could not resolve domain.")
            input("\nPress Enter to return to Network Scanner menu...")

        elif choice == "4":
            target = input("Enter target IP or domain for full port scan: ").strip()
            full_port_scan(target)

        elif choice == "5":
            break  # ✅ back to Main Menu

        else:
            print("[!] Invalid choice.")


# -------- Main Menu -------- #
def main():
    while True:
        print("\n==================================================")
        print("🔐 Cybersecurity Toolkit - Interactive Menu 🔐")
        print("==================================================")
        print("1. 🖥️  Display System Information")
        print("2. 🌐 Network Scanner")
        print("3. ⚡ Vulnerability Scanner")
        print("4. ❌ Exit")

        choice = input("\n👉 Enter your choice: ").strip()

        if choice == "1":
            print("\n[System Info placeholder here]")
            input("\nPress Enter to return to Main Menu...")

        elif choice == "2":
            network_scanner_menu()  # ✅ stays inside until user exits

        elif choice == "3":
            print("\n[Vulnerability Scanner placeholder here]")
            input("\nPress Enter to return to Main Menu...")

        elif choice == "4":
            print("Exiting...")
            sys.exit()

        else:
            print("[!] Invalid choice.")


if __name__ == "__main__":
    main()
