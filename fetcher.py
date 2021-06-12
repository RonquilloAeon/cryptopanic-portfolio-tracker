import asyncio
import json
import logging
import os
from pathlib import Path

import arrow
import httpx

from config import Config

config = Config()

logging.basicConfig(
    format="[%(asctime)s]\t[%(levelname)s]\t%(message)s", datefmt="%Y-%m-%d %I:%M:%S%z",
    level=config.LOG_LEVEL.upper()
)
logger = logging.getLogger(__name__)

PORFOLIO_ENDPOINT = f"{config.API_BASE_URL}/portfolio/"
DATA_PATH = Path("data")


async def fetch_portfolio() -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            PORFOLIO_ENDPOINT, params={"auth_token": config.API_TOKEN}
        )
        data = response.json()

    return data


def ensure_data_dir():
    if not DATA_PATH.exists():
        os.mkdir(DATA_PATH)
    else:
        if not DATA_PATH.is_dir():
            raise RuntimeError("'data' path expected to be a directory")


def main():
    ensure_data_dir()
    now = arrow.utcnow()

    with open(
        DATA_PATH / f"{now.format('YYYY-MM-DD-HH-mm')}_data.json", "w"
    ) as f:
        data = asyncio.run(fetch_portfolio())
        data["date"] = now.isoformat()
        json.dump(data, f)

    logger.info("Done!")


if __name__ == "__main__":
    main()
