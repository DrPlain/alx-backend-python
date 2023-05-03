#!/usr/bin/env python3
""" Async generator """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """asycn generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
