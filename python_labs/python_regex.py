import re

def extract_log_details(log_entry):
    pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) \[(?P<log_level>\w+)\] \((?P<module>\w+)\): (?P<message>.+)'
    match = re.match(pattern, log_entry)
    if match:
        return match.groupdict()
    return None

# Example usage
log_entry = "2023-10-01 12:34:56 [ERROR] (auth_module): Failed to authenticate user"
print(extract_log_details(log_entry))

# Output:
# {
#     'date': '2023-10-01',
#     'time': '12:34:56',
#     'log_level': 'ERROR',
#     'module': 'auth_module',
#     'message': 'Failed to authenticate user'
# }