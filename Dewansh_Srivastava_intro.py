from rich.console import Console

console = Console()

def main():
    console.print("[green]Welcome to My CLI Resume![/green]")
    console.print("[blue]Type 'help' to see the commands.[/blue]")
    
    while True:
        command = console.input("[bold green]$ [/bold green]").strip()
        if command == "help":
            console.print("Available commands: help, show name, show skills, show Domain expertise, show Achievements, show experience, show download resume, exit")
        elif command == "show name":
            console.print("Dewansh srivastava \n"
                        "profession :Software Engineer")
        elif command == "show skills":
            console.print("Skills: Python, FastAPI, MongoDB \n"
            "TCP/IP, DNS, DHCP, Virtualization (ESX/KVM/Hyper-V) \n"
            "Network Security (NAT, VPN),(VLAN/802.1Q) \n"
            "Cisco ACI, SD-WAN \n")
        elif command == "show Domain expertise":
            console.print("Data Center Solutions \n"
                        "Network Security \n"
                        "Routing & Switching \n"
                        "Software Development")
        elif command == "show experience":
            console.print("Company: Cisco Systems (India) Private Limited\n"
                        "Location: Bengaluru, Karnataka\n"
                        "Position: Software Engineer in Data Center Division\n"
                        "Responsibilities:\n"
                        "  - Designed and implemented Data Center (ACI) testbeds, configuring Nexus 9000 series switches, APICs, and spine-leaf network topology.\n"
                        "  - Detected and resolved critical SSH and functionality bugs to enhance system reliability.\n"
                        "  - Configured ESXi Virtualization infrastructure and VMM devices for monitoring network traffic within ACI environments.\n"
                        "  - Performed regression and unit testing tailored for AAA feature validation.\n"
                        "  - Developed a custom Cisco ACI Toolkit using Django and REST API, streamlining network management and reducing manual work time for higher authorities by 30%.\n",
                        "  - Designed RESTful API endpoints over HTTP, improving the design of existing data accessor and interface layers of the profiler tool.\n"
                        "Company: Amity software systems limited\n"
                        "Location: Noida, U.P \n"
                        "Position: Software Engineer\n"
                        "Responsibilities:\n"
                        "  - Developed and maintained the NDRP Dashboard using Python, FastAPI, MongoDB, and Kafka for real-time \n"
                        "  - data processing and analytics. Configured Kafka to streamline data ingestion and integration, enabling seamless \n"
                        "  - communication between microservices and enhancing system performance.\n ")
        elif command == "show Achievements":
            console.print("- Earned CCNA certification.\n"
                        "  - Designed and implemented Cisco ACI testbeds with Nexus 9000 series switches. \n"
                        "  - Developed a custom Cisco ACI Toolkit using Django and REST API, reducing manual workload by 30%. \n"
                        "  - Created a FastAPI backend for a lead management system integrated with MongoDB.")
        elif command == "show download resume":
            console.print("https://drive.google.com/file/d/1uzC3myjqBffVQnMUhSLbKhUFiduUyRzu/view?usp=sharing")
        elif command == "exit":
            console.print("[bold red]Goodbye![/bold red]")
            break
        else:
            console.print("[red]Command not found. Type 'help' for a list of commands.[/red]")

if __name__ == "__main__":
    main()
