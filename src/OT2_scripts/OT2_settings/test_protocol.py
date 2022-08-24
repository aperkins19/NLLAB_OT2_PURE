from opentrons import protocol_api
import json

# metadata
metadata = {
    "protocolName": "Test protocol to check importin json file",
    "author": "Michael Stam",
    "email": "a.j.p.perkins@sms.ed.ac.uk",
    "description": "Test",
    "apiLevel": "2.3",
}


def run(protocol: protocol_api.ProtocolContext):

    json_settings_file_path = "/data/user_storage/al_cell_free/test.json"

    # Reading in json json_settings_file
    json_settings_file = json.load(open(json_settings_file_path, 'r'))

    protocol.comment(json_settings_file["message"])
