#!/usr/bin/python3
# from pyclearpass import *
# Expected format of input file is "mgmt IP , hostname, description, vendor"

import json

cppm_nads = json.loads("cppm_nas_output.json")


def create_hosts(nas_devices, output_file, delimeter=" "):
    with open(nas_devices, "r") as inputfile:
        lines = inputfile.readlines()
    with open(output_file, "w") as outputfile:
        for line in lines:
            mgmtip, hostname, descrip, vendor = line.strip().split(delimeter)
            # device = hostname.strip()
            hostname_modified = hostname.replace("-", "")
            outputfile.write(hostname_modified)
            outputfile.write(" = {\n")
            outputfile.write('\t"description": "')
            outputfile.write(descrip)
            outputfile.write('",\n')
            outputfile.write('\t"name": "')
            outputfile.write(hostname)
            outputfile.write('",\n')
            outputfile.write('\t"ip_address": "')
            outputfile.write(mgmtip)
            outputfile.write('",\n')
            outputfile.write('\t"radius_secret": "<sanitized>",\n')
            outputfile.write('\t"tacacs_secret": "<sanitized>",\n')
            outputfile.write('\t"vendor_name": "Aruba",\n')
            outputfile.write('\t"coa_capable": "True",\n')
            outputfile.write('\t"coa_port": "3799",\n')
            outputfile.write('\t"attributes": {\n')
            outputfile.write('\t\t"Device Type": "IAP"\n')
            outputfile.write("\t\t},\n")
            outputfile.write('\t"device_group_list": [\n')
            outputfile.write('\t\t"NA-Cisco-Switches-ALL", \n')
            outputfile.write('\t\t"NA-Core-Cisco-Switches", \n')
            outputfile.write('\t\t"NA-Cisco-Switches" \n')
            outputfile.write("\t]\n")
            outputfile.write("}\n")
        outputfile.close


def create_host_groupings(nas_devices, output_file, delimeter=" "):
    device_list = []
    with open(nas_devices, "r") as inputfile:
        for line in inputfile:
            mgmtip, hostname, descrip, vendor = line.strip().split(delimeter)
            device = hostname.strip()
            device_modified = hostname.replace("-", "")
            device_list.append(device_modified)
    with open(output_file, "a") as outputfile:
        outputfile.write("new_nas")
        outputfile.write(" = [")
        for device in device_list:
            hostname_modified = device.replace("-", "")
            outputfile.write(hostname_modified)
            outputfile.write(",")
        outputfile.write("]\n\n")
        outputfile.close


if __name__ == "__main__":
    nas_devices = "spreadsheet_nases.txt"
    # nas_devices = 'spreadsheet_emea_inventory.txt'
    # nas_devices = 'spreadsheet_na_inventory.txt'
    output_file = "nas_devices_autogen.py"
    # create_hosts(nas_devices, output_file)
    create_host_groupings(nas_devices, output_file)
