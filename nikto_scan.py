import subprocess
import json
import datetime

def run_nikto_scan(target):
    result = subprocess.run(['nikto', '-h', target], capture_output=True, text=True)
    scan_result = {
        'date': str(datetime.datetime.now()),
        'target': target,
        'output': result.stdout
    }
    return scan_result

def save_report(scan_result, filepath):
    with open(filepath, 'w') as f:
        json.dump(scan_result, f, indent=4)

if __name__ == "__main__":
    target = 'http://your_target'
    scan_result = run_nikto_scan(target)
    save_report(scan_result, 'reports/nikto_scan.json')
