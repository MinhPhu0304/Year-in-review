# Year in review

Year in review is a Python script to see your Github activity of the current year. The script will generate a pie chart showing primary language in repositories you contributed to.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies.

```bash
pip install -r requirements.txt
```
You will need your private Github token to access your information. To get your own Github token go to [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

Create a .env file at the root of the directory. Then add these line bellow
```
GITHUB_TOKEN=YOUR_GITHUB_TOKEN_HERE
```

## Usage

```python
python main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
