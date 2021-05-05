#
from plotsymbol.src.plotsymbol import (
    plotsymbol_all
)

#
from aiohttp import web

#
app_plotsymbol = web.Application()

#
app_plotsymbol.add_routes([

    web.post('/',   plotsymbol_all),

])
