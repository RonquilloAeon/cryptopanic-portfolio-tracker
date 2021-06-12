# Crpyto Panic Portfolio Tracker

A simple script to download your portfolio data for analysis.

## Usage

- Create Python 3.9 virtual environment in `venv` directory
- Activate virtualenv and install dependencies: `pip install -r requirements.txt`
- Create `.env` file. See format below.
- Set up cron job on your machine
- Run `crontab -e`
- Add: `* */2 * * * FETCHER_PATH/fetcher.sh > /dev/null 2>&1`. Modify 

## .env format

You'll need a free [Crypto Panic](https://cryptopanic.com) API auth token.

```
API_TOKEN=[CRYPTO PANIC API TOKEN]
LOG_LEVEL=info
```

## Cleanup

- To view your jobs: `crontab -l`
- To remove ALL cron jobs on your machine: `crontab -r`

## Resources

- https://monicagranbois.com/blog/python/cron-and-python-virtualenv/
