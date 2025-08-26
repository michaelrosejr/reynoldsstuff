#!/usr/bin/python3
import json

import httpx
from pyclearpass import ApiPolicyElements, ClearPassAPILogin
from rich import print

from config import settings
from newnas import new_nas

# Authentication
login = ClearPassAPILogin(
    server=f"https://{settings.cppm_server}/api",
    granttype="client_credentials",
    clientid=settings.client_id,
    clientsecret=settings.client_secret,
    verify_ssl=False,
)


# Create NAS
def create_nad():
    print("Creating NAS devices...")
    cppm_output = []
    for each_nas in new_nas:
        response = ApiPolicyElements.new_network_device(login, body=each_nas)
        cppm_output.append(response)
    with open("cppm_nas_output.json", "w") as outputfile:
        for item in cppm_output:
            json.dump(item, outputfile, indent=4)
    print(cppm_output)


def get_nad():
    print("Fetching NAS devices...")
    return ApiPolicyElements.get_network_device(login)


def get_nad_group():
    print("Fetching NAS device groups...")
    return ApiPolicyElements.get_network_device_group(login)


def create_nad_group(nad_group):
    print("Creating NAS device groups...")
    return ApiPolicyElements.new_network_device_group(login, body=nad_group)


def show_roles():
    print("Fetching roles...")
    return ApiPolicyElements.get_role(login)


def new_nad_group(login, group_body):
    print(f"Creating NAS device group: {group_body['name']}")
    URL = f"{login.server}/network-device-group"
    # print(dir(login))
    from pyclearpass.common import _new_api_token

    token = _new_api_token(login)
    print(f"API Token: {token['access_token']}")
    print(f"URL: {URL}")
    response = httpx.post(
        URL,
        headers={
            "Authorization": f"Bearer {token['access_token']}",
            "Content-Type": "application/json",
        },
        json=group_body,
        verify=login.verify_ssl,
    )
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")


if __name__ == "__main__":
    # roles = show_roles()
    # print(roles)
    # create_nad()
    ngn = "nad_reynolds_group"
    # print(create_nad_group(ngn))
    nad_group = {
        "name": ngn,
        "description": "Created via API",
        "group_format": "list",
        "value": "1.1.1.0/24, 2.2.1.0/24",
    }
    # print("List NADs")
    # print(get_nad())
    print(f"Create NAD Group: {nad_group}")
    print(create_nad_group(nad_group))
    # print(new_nad_group(login, nad_group))
    print(get_nad_group())
    print("Done.")
