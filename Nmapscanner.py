#First Step: Recon

import nmap

def nmapscan(ip_addr):
    nmscanner = nmap.PortScanner()
    nmscanner.scan(ip_addr, '22-443')

    """
    print('Host : %s (%s)' % (host, scanner[host].hostname()))
    print(f'Scan info: {scanner.scaninfo()}')
    print('State : %s' % scanner[host].state())
    final_result = scanner[host]['tcp'].keys()
    port_list = list(final_result)
    print("Open Ports: ", port_list)
    detail_list = list(scanner[host]['tcp'].values())
    for port, i in zip(port_list, detail_list):
        item = i.values()
        print(f'Detail for port {port} {list(item)}')
    """

    nmscan_results = {
        'host info': {
            'hostname': nmscanner[ip_addr].hostname(),
            'hostip' : ip_addr,
            'state': nmscanner[ip_addr].state(),
            'scan info': nmscanner.scaninfo()
        },
        'open_ports': list(nmscanner[ip_addr]['tcp'].keys()),
        'port_details': []
    }

    for port, details in nmscanner[ip_addr]['tcp'].items():
        port_detail = {
        'port': port,
        'state': details['state'],
        'reason': details['reason'],
        'name': details['name'],
        'product': details['product'],
        'version': details['version'],  # Add version here
        'extrainfo': details['extrainfo'],
        'conf': details['conf'],
        'cpe': details['cpe']
    }
    nmscan_results['port_details'].append(port_detail)

    return nmscan_results
