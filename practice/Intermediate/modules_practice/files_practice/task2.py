from pathlib import Path

new_directory = Path('.') / 'data_logs'

# Create new directory if it doesn't exist
new_directory.mkdir(exist_ok=True)

# Create new file named 'app_info.log' if it doesn't exist and write the following text.
with open(new_directory / 'app_info.log', 'w') as f:
    text = ["INFO: Server started",
            "INFO: Server is working properly",
            "INFO: Server is going to be closed in 5min"]
    for message in text:
        f.write(message + '\n')

# Create new file named 'app_error.log' if it doesn't exist and write the following text.
with open(new_directory / 'app_error.log', 'w') as f:
    text = ["ERROR: Connection lost",
            "ERROR: An error has occured!",
            "ERROR: Server was closed unexpectedly"]
    for message in text:
        f.write(message + '\n')

# Create new file named 'notes.txt' if it doesn't exist and write the following text.
with open(new_directory / 'notes.txt', 'w') as f:
    f.write("There are some notes")

# Find all files with extension '.log'
for file in new_directory.glob('*.log'):
    print(file)

# create new list
total_text = []

# add all messages from app_info.log into total_text list
with open(new_directory / 'app_info.log') as f:
    for message in f.readlines():
        total_text.append(message.strip())

# add all messages from app_error.log into total_text list
with open(new_directory / 'app_error.log') as f:
    for message in f.readlines():
        total_text.append(message.strip())

# create summary log and add all logs in it
with open(new_directory / 'summary.log', 'w') as f:
    for item in total_text:
        f.write(item + '\n')

# add message "End of summary"
with open(new_directory / 'summary.log', 'a') as f:
    f.write("--- END OF SUMMARY ---")

# Delete all files in the directory
for file in new_directory.iterdir():
    file.unlink()

# Delete directory if it's empty
new_directory.rmdir()
