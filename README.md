# Manx
Download, parse, and filter multiple blocklists and inject them directly into your dnsmasq or hosts configurations.
## Docker
Build the docker image using the following command in project root directory:

`$ docker build . --tag manx:dev`

Application can be run by using the following command, where /path/to/config points to a directory containing both a blocklist.txt and whitelist.txt file to be consumed. The whitelist can be empty. A combined output file named blacklist.conf will be produced in the same directory if the process completes successfully:

`$ docker run --rm --name manx -v /path/to/config:/manx manx:dev`

## Usage
There are several ways to configure this application to produce the requested output.

`$ manx [-h|--help] [-o|--output FILE] [-T FORMAT] [-v] [-x] [-s|--syntax KEY] [-w|-W FILE] FILE`

### Simple
All uses require a list of blocklist urls outlined in an external text file. Urls must be line-delimited.

`$ python main.py blocklist.txt`

### Whitelist
Similar to the blocklist file, a whitelist text file may be provided that contains urls to omit from the final blacklist. Use -w to comment out matching urls, or -W to remove them from the list completely.

`$ python main.py -w whitelist.txt blocklist.txt`

### Output
Specify an output configuration file. This file is typically lead by some information about this application and a timestamp. By default, blacklist.conf is produced in the script directory.

`$ python main.py -o /etc/dnsmasq.d/blacklist.conf -w whitelist.txt blocklist.txt`

### Time Format
Unless `-x` is passed (where this step would be otherwise skipped), manx provides some basic information at the top of the output configuration file. One of these lines includes a time stamp representing when the file was created. By default, the format used is of ISO 8601. However, another format can be selected by passing the `-T` parameter.

`$ python main.py -w whitelist.txt -T '%Y-%m-%d %H:%M:%S' blocklist.txt`

### Syntax
Manx can write the output file in any format that it can interpret. By default, the format used is dnsmasq >= 2.86. Options below are passed with the `-s` or `--syntax` directive

| Format        |  Argument   |
| :---          |       ----: |
| dnsmasq>=2.86 | `local`     |
| dnsmasq<2.86  | `server`    |
| hosts         | `hosts`     |
| adblock       | `adblock`   |
| domain-only   | `domain`    |
