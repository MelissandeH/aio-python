import aiohttp
import asyncio
from rich import print


from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


async def main():

  # async with aiohttp.ClientSession() as session:
    # async with session.get('http://51.15.17.205:9000/plotsymbol/mhu') as resp:
    # print(resp.status)
    # print(await resp.json())

    transport = AIOHTTPTransport(
        url="https://dbschool.alcyone.life/graphql")

    # Using `async with` on the client will start a connection on the transport
    # and provide a `session` variable to execute queries on this connection
    async with Client(
        transport=transport, fetch_schema_from_transport=True,
    ) as session:

        # Execute single query
        query = gql(
            """
                query {
                tickers(where: { symbol_contains: "BTCUSDT" }) {
                    symbol
                    price
                    created_at
                }
            }
        """
        )

        result = await session.execute(query)
        print(result)


# asyncio.run(main())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
