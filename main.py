import subprocess ## default on python
import sys

def rn_cmd():
    while True:
        usrinput = input("enter command (or 'exit' to quit): ").strip()
        if usrinput.lower() == 'exit':
            print("exit ok")
            break
        try:
            if usrinput.lower().startswith("-powershell"):
                cm = usrinput[len("-powershell"):].strip()
                rs = subprocess.run(
                    ["powershell", "-Command", cm],
                    capture_output=True, text=True
                )
            elif usrinput.lower().startswith("-cmd"):
                cm = usrinput[len("-cmd"):].strip()
                rs = subprocess.run(
                    ["cmd", "/c", cm],
                    capture_output=True, text=True
                )
            else:
                if sys.platform == "win32":
                    print("specify")
                    continue
                rs = subprocess.run(
                    usrinput, shell=True, capture_output=True, text=True
                )

            if rs.stdout:
                print(rs.stdout)
            if rs.stderr:
                print(f"error: {rs.stderr}")

        except Exception as e:
            print(f"error: {e}")
if __name__ == "__main__":
    rn_cmd()
