
      _____     _          _           ____             _             
     |  ___|_ _| |__  _ __(_) ___     |  _ \  ___ _ __ | | ___  _   _ 
     | |_ / _` | '_ \| '__| |/ __|____| | | |/ _ \ '_ \| |/ _ \| | | |
     |  _| (_| | |_) | |  | | (_|_____| |_| |  __/ |_) | | (_) | |_| |
     |_|  \__,_|_.__/|_|  |_|\___|    |____/ \___| .__/|_|\___/ \__, |
                                                 |_|            |___/ 
      == A tool to deploy physical configuration on an ACI fabric ==


Introduction
=============
Fabric-Deploy is a tool to automate the deployment of physical configuration 
(access ports, port channels and VPCs) to an ACI fabric. The tool reads port
allocations from an Excel spreadsheet and automatically pushes all relevant
configuration to the fabric to configure such ports. Supported types include
regular access ports, port channels, and VPCs. The tool also instances
default interface policies for CDP, LLDP, LACP, MCP, STP, etc.


Requirements
=============
- Python3.3 or above.
- The "acifabriclib" library
    - Download it from the following URL and install it using "python3 setup.py install" 
        - https://github.com/datacenter/acifabriclib
- The "requests" library.


Usage
=====

    $ python3 aci-fabric-deploy.py --input <spreadhseet> 
  
    Optional arguments:
      -u URL, --url URL                 APIC IP address.
      -l LOGIN, --login LOGIN           APIC login ID.
      -p PASSWORD, --password PASSWORD  APIC login password.
      -i INPUT, --input INPUT           Input file
      -d DEBUG, --debug DEBUG           Enable debug mode


The application also takes the regular parameters for APIC address, username and 
password, as well as parses any existing *credentials.py* file stored in the
same directory. In that case, the content of the *credentials.py* file must 
follow this format:

    URL="https://192.168.0.90"
    LOGIN="admin"
    PASSWORD="Ap1cPass123"

If the *credentials.py* does not exist and the credentials are not supplied from
the command line, the application will ask for them interactively.

Usage Examples
==============
    
    $ python3 aci-fabric-deploy.py --input Sample_PortMapping.xlsx
    $ python3 aci-fabric-deploy.py --input Sample_PortMapping.xlsx --debug yes
    $ python3 aci-fabric-deploy.py --input Sample_PortMapping.xlsx -l admin -p "Ap1cPass123" -u "https://192.168.0.90"

Output Examples
===============

    $ python3 aci-fabric-deploy.py --input Sample_PortMapping.xlsx
    
       _____     _          _           ____             _
      |  ___|_ _| |__  _ __(_) ___     |  _ \  ___ _ __ | | ___  _   _
      | |_ / _` | '_ \| '__| |/ __|____| | | |/ _ \ '_ \| |/ _ \| | | |
      |  _| (_| | |_) | |  | | (_|_____| |_| |  __/ |_) | | (_) | |_| |
      |_|  \__,_|_.__/|_|  |_|\___|    |____/ \___| .__/|_|\___/ \__, |
                                                  |_|            |___/
    
      == A tool to deploy physical configuration on an ACI fabric ==
    
    [+] Creating standard interface policies
    [+] Creating interface 'Access_DC001_ESX1_452'
    [+] Creating interface 'Access_DC001_ESX1_454'
    [+] Creating interface 'VPC_DC001_ESX7_583'
    [+] Creating interface 'VPC_DC001_ESX7_584'
    [+] Creating interface 'VPC_DC001_ESX7_585'
    [+] Creating interface 'VPC_DC001_ESX7_586'
    [+] Creating interface 'VPC_DC001_ESX1_690'
    [+] Creating interface 'VPC_DC001_ESX1_703'
    [+] Creating interface 'PC_DC001_ESX7_284'



    
