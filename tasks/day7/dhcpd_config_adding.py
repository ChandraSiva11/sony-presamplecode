"""Adding the DHCP new IP to DHCP Server config"""
import sys


def path_decision():
    """Path of the script location is selected"""
    path = ''
    if sys.argv[0].count('/') == 0:
        path = './'
    else:
        path = '/'.join(sys.argv[0].split('/')[0:-1])+'/'
    print("Path ->", path)
    return path


def dhcpd_last_conf_reading(path):
    """Config reading doc string"""
    cnf_fd_read = open(path+'dhcpd.conf', 'r')
    hw_id_set = set()
    while True:
        line = cnf_fd_read.readline()
        # print("lines test ->", line.find('host',0))
        if line.find('host',0) != -1:
            # print('Hostname found', line)
            string = line
        else:
            string += line
            if line.find('hardware ethernet') != -1:
                line = line.lstrip()
                line2 = line.split(' ')
                hw_id = line2[-1].rstrip(';\n')
                hw_id_set.add(hw_id)
                # print('hardware line ->', hw_id_set)
        if line.find('}',0) == 0:
        	pass
            # print('Set one Set ->', string)
        if not line:
            # print('Last set of value on the Config ->',string)
            cnf_fd_read.close()
            return string, hw_id_set


def read_csv(path):
    """Read CSV File Doc string"""	
    csv_read_fd = open(path+'fixed-ip-list.csv','r')
    csv_dict = {}
    while True:
        line = csv_read_fd.readline()
        dev_name = line.split(',')
        if len(dev_name) > 1:
            # print(dev_name, len(dev_name))
            csv_dict[dev_name[0]] = dev_name[1].rstrip('\n')
        if not line:
            csv_read_fd.close()
            return csv_dict


def new_ip_ldigit_calc(last_string):
    """Doc string for ip finding"""
    for line in last_string.split('\n'):
    	if line.find('fixed-address') != -1:
            line = line.lstrip()
            line = line.split()
            l_digit = line[1].split('.')[-1].rstrip(';')
            # print('IP line ->', l_digit)
            return(int(l_digit))


def cre_new_dhcp_cfg (l_digit, csv_dict, hw_set):
    """Doc string for new config creation"""
    old_hw_list = list(hw_set)
    string = ''
    for dev_name, hw_id in csv_dict.items():
        # print(dev_name, hw_id)
        if hw_id not in old_hw_list:
            l_digit += 1
            print('New hardware IP :', '192.168.1.'+ str(l_digit))
            string += 'host ' + dev_name + ' {\n'
            string += ' '*8 + 'hardware ethernet ' + hw_id + ';\n'
            string += ' '*8 + 'fixed-address ' + '192.168.1.'+ str(l_digit) + ';\n'
            string += ' '*8 + 'option routers 192.168.1.1;\n}\n\n'
        else:
            print('This hardware ID already exist So not added', hw_id)
    return string


def final_cgfg_write(path, new_dhcp_string):
    "Doc String for adding new config on the file"
    cnf_fd_write = open(path+'dhcpd.conf', 'a')
    cnf_fd_write.write(new_dhcp_string)
    cnf_fd_write.close()


def main():
    """Main function Doc string"""
    path = path_decision()
    last_str, hw_set = dhcpd_last_conf_reading(path)
    csv_dict = read_csv(path)
    l_digit = new_ip_ldigit_calc(last_str)
    new_dhcp_string = cre_new_dhcp_cfg(l_digit, csv_dict, hw_set)
    final_cgfg_write(path, new_dhcp_string)
    # print('CSV DICT ->', csv_dict, l_digit, last_str, hw_set)
    print('New String ->', new_dhcp_string)


if __name__ == '__main__':
    main()
