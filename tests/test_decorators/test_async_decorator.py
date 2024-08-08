import time

from pyfunctools.decorators import async_decorator


def test_async_decorator():
    import asyncio

    @async_decorator
    def blocking_function(x):
        time.sleep(2)
        return x * 2

    async def main():
        result = await blocking_function(5)
        assert result == 10

    asyncio.run(main())
