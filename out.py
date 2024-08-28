from datetime import datetime as dt

def to_file(lines, file, time_format):
    file.write("# Manx v0.1\n")
    file.write(f"# Published: {dt.now().strftime(time_format)}\n")
    file.write(f"# Unique Entries: {len(lines)}\n")
    for line in lines:
        file.write(f"{line}\n")

def install(file, dest):
    pass