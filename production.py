import os
import json
import time
import logging

class ConfigLoader:
    def __init__(self):
        self.config = {}
        self.load_time = None

    def load(self):
        logging.info("Loading configuration files...")
        time.sleep(0.5)

        self.config = {
            "service": "Instant Software Solutions API",
            "version": "1.3.7",
            "debug": False,zer
            "region": "internal-prod",
        }

        self.config["dev_credentials"] = {
            "smb_user": "ctfuser",
            "ssh_pass": "Password123!",
            "note": "REMOVE BEFORE PRODUCTION"
        }

        self.load_time = time.time()
        logging.info("Config loaded successfully")

    def get_config(self):
        return self.config


class FakeAPIService:
    def __init__(self, config):
        self.config = config

    def authenticate(self, user, password):
        if user == self.config["dev_credentials"]["ssh_user"] and \
           password == self.config["dev_credentials"]["ssh_pass"]:
            return True
        return False

    def run(self):
        print("Starting Instant Software Internal Service...")
        print("Service running in restricted mode...\n")

        # fake loop
        for i in range(3):
            print(f"Heartbeat {i+1}: OK")
            time.sleep(1)

        print("\nService status: STABLE")


def main():
    logging.basicConfig(level=logging.INFO)

    loader = ConfigLoader()
    loader.load()

    config = loader.get_config()

    service = FakeAPIService(config)
    service.run()

    # hidden debug print (CTF hint style)
    print("\n[DEBUG LOG]")
    print(json.dumps(config, indent=4))


if __name__ == "__main__":
    main()
