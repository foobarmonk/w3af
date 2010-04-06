import re
from plugins.attack.payloads.base_payload import base_payload

class os_fingerprint(base_payload):
    '''
    This payload detect OS.
    '''
    def api_read(self):
        result = []

        if self.shell.read('/proc/sys/kernel/ostype')[:-1]  == 'Linux':
            result.append('Linux')
        else:
            result.append('Windows')

        return result
    
    def run_read(self):
        result = self.api_read()
        if result == [ ]:
            result.append('Can not detect OS')
        return result
