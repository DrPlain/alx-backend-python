#!/usr/bin/env python3
""" Basic async syntax """
import asyncio
import random


async def wait_random(max_delay=10):
    """Basic async coroutine"""
    # uniform returns a floating num between two specified nums both included
    num = random.uniform(1, max_delay)
    await asyncio.sleep(num)
    return num
