import time

class SIM800L:
    def __init__(self):
        self.connected = False
        self.apn = None

    def send_at(self, command):
        responses = {
            "AT": "OK",
            "AT+CSQ": "+CSQ: 18,0\nOK",
            "AT+CREG?": "+CREG: 0,1\nOK",
            "AT+SAPBR=1,1": "OK",
            "AT+HTTPINIT": "OK"
        }
        time.sleep(0.3)
        response = responses.get(command, "OK")
        print(f"  AT >> {command}")
        print(f"  << {response}")
        return response

    def setup_gprs(self, apn="internet"):
        self.apn = apn
        print("\n--- Initializing SIM800L ---")
        commands = ["AT", "AT+CSQ", "AT+CREG?", "AT+SAPBR=1,1", "AT+HTTPINIT"]
        for cmd in commands:
            self.send_at(cmd)
        self.connected = True
        print("--- GPRS Connected ---\n")
        return True
