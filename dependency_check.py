import subprocess
import json
import datetime

def run_dependency_check():
    result = subprocess.run(['dependency-check.sh', '--project', 'my-project', '--out', 'reports'], capture_output=True, text=True)
    scan_result = {
        'date': str(datetime.datetime.now()),
        'output': result.stdout
    }
    return scan_result

def save_report(scan_result, filepath):
    with open(filepath, 'w') as f:
        json.dump(scan_result, f, indent=4)

if __name__ == "__main__":
    scan_result = run_dependency_check()
    save_report(scan_result, 'reports/dependency_check.json')
