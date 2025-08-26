# Define new NAS (Network Access System), see import above
new_nas = [
    {
        "description": "yAye-TACACS-Auth",
        "name": "yAye-MGMT-Devices",
        "ip_address": "1.1.1.0/24",
        "radius_secret": "S1!$Xsw1fb0",
        "tacacs_secret": "S1!$Xsw1fb0",
        "vendor_name": "Aruba",
        "coa_capable": "True",
        "coa_port": "3799",
        "attributes": {"Device Type": "IAP"},
        "device_group_list": ["NA-Cisco-Switches-ALL", "NA-Core-Cisco-Switches", "NA-Cisco-Switches"],
    },
    {
        "description": "yBee-TACACS-Auth",
        "name": "yBee-MGMT-Devices",
        "ip_address": "2.2.1.0/24",
        "radius_secret": "Rt&Zac9S",
        "tacacs_secret": "Rt&Zac9S",
        "vendor_name": "Aruba",
        "coa_capable": "True",
        "coa_port": "3799",
        "attributes": {"Device Type": "IAP"},
        "device_group_list": ["NA-Cisco-Switches-ALL", "NA-Core-Cisco-Switches", "NA-Cisco-Switches"],
    },
]
