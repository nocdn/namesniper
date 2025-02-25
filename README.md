# namesniper

> a script to query the mojang api to check available minecraft usernames

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### installation

I recommend using a virtual environment to install the dependencies to prevent any conflicts with your system's python installation.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

The script can be run with several command-line options:

- `-i, --input` : Read usernames from a file (one per line or space-separated)
- `-u, --usernames` : Directly specify usernames via command line (space-separated)
- `-o, --output` : Save available usernames to a specified output file
- `-p, --progress-bar` : Show a progress bar during username checking
- `-h, --help` : Show help message and exit

If no input method is specified, the script will prompt for username input.

The script checks each username against the Mojang API to determine availability. A username is considered available if the API returns a non-200 status code.

### Examples

Check a single username:

```bash
python namesniper.py -u nocdn
```

Check multiple usernames with progress bar:

```bash
python namesniper.py -p -u nocdn notch jeb_
```

Read usernames from a file, with a progress bar, and save available usernames to a file:

```bash
python namesniper.py -i usernames.txt -o available_usernames.txt -p
```

Save available usernames to a file:

```bash
python namesniper.py -i usernames.txt -o available_usernames.txt
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
