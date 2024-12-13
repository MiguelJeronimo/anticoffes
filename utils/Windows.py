import subprocess

class Windows:
    def blocked(self):
        """
        Bloqueo de pc en windows

        """
        cmd = 'rundll32.exe user32.dll, LockWorkStation'
        subprocess.call(cmd)