
from aiohttp import web
import yaml
from datetime import datetime
import aiohttp
import asyncio
import os
from rich import print

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# async def _tick_(request):
#     try:
#         # 0 : extract payload dict
#         json = await request.json()
#         print(json)

#         return web.json_response(dict(json=json))

#     # $>
#     except Exception as exp:
#     # <!
#         # !0 return what's wrong in string and the type of the exception should be enough to understand where you're wrong noobs
#         return web.json_response({'err':{'str':str(exp),'typ':str(type(exp))}}, status=500)
# #`< - - - - - - - - - - - -


async def tick_all(request):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://51.15.17.205:9000/tick/mhu') as resp:
                transport = AIOHTTPTransport(
                    url="https://dbschool.alcyone.life/graphql")
                jsonResponse = await resp.json()
                elements = jsonResponse['data']

                # Using `async with` on the client will start a connection on the transport
                # and provide a `session` variable to execute queries on this connection
                for data in elements:

                    async with Client(
                        transport=transport, fetch_schema_from_transport=True,
                    ) as session:

                        # Execute single query
                        query = gql(
                            """
                                mutation {
                                        createTicker(input: { data: { symbol: "%s" , price: %f } }) {
                                            ticker {
                                            symbol
                                            price
                                        }
                                    }
                                }
                            """
                            % (str(data['symbol']), float(data['price']))
                        )

                        result = await session.execute(query)
                        print(result)

        return web.json_response(info)
    except Exception as e:
        print(e)
        raise e

# loop = asyncio.get_event_loop()
# loop.run_until_complete()
