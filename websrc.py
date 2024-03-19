import os
import whois
import socket
from colorama import Fore, Style

def print_separator():
    print("=" * 50)

def print_color(text, color):
    print(color + text + Style.RESET_ALL)

def print_heading(text):
    print("\n" + Fore.GREEN + Style.BRIGHT + "#" * 50)
    print("#" + " " * 48 + "#")
    print("#" + text.center(48) + "#")
    print("#" + " " * 48 + "#")
    print("#" * 50)

def print_info(info):
    print_color(info, Fore.BLUE)

def get_server_info(url):
    try:
        response = requests.head(url)
        server_info = response.headers['Server']
        return f"Server: {server_info}\n"
    except Exception as e:
        return "Error retrieving server information: " + str(e) + "\n"

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        info = "WHOIS Information\n" + "=" * 50 + "\n"
        info += f"Domain Name: {', '.join(w.domain_name)}\n"
        info += f"Registrar: {w.registrar}\n"
        info += f"WHOIS Server: {w.whois_server}\n"
        info += f"Updated Date: {', '.join(map(str, w.updated_date))}\n"
        info += f"Creation Date: {', '.join(map(str, w.creation_date))}\n"
        info += f"Expiration Date: {', '.join(map(str, w.expiration_date))}\n"
        info += f"Name Servers: {', '.join(w.name_servers)}\n"
        info += f"Status: {', '.join(w.status)}\n"
        info += f"Emails: {', '.join(w.emails)}\n"
        info += f"Organization: {w.org}\n"
        info += f"State: {w.state}\n"
        info += f"Country: {w.country}\n"
        return info
    except Exception as e:
        return "Error retrieving WHOIS information: " + str(e) + "\n"

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return f"IP Address: {ip_address}\n"
    except Exception as e:
        return "Error retrieving IP address: " + str(e) + "\n"

def save_info_to_file(url, info):
    folder_name = "website_info"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    domain = url.split("//")[-1].split("/")[0]
    file_name = os.path.join(folder_name, f"{domain}.txt")
    with open(file_name, "w") as file:
        file.write(info)

def main():
    while True:
        url = input("Enter the URL to scan (or type 'exit' to quit): ")
        if url.lower() == 'exit':
            break
        
        domain = url.split("//")[-1].split("/")[0]
        print_heading("Scanning " + url)
        print_separator()

        server_info = get_server_info(url)
        whois_info = get_whois_info(domain)
        ip_info = get_ip_address(domain)

        all_info = server_info + "\n" + whois_info + "\n" + ip_info
        print_info(all_info)

        save_info_to_file(url, all_info)
        print_color("Information saved to file.", Fore.GREEN)

if __name__ == "__main__":
    main()

