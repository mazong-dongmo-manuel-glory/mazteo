from sanic import Sanic,response
from time import time
app = Sanic("myapp")
@app.get("/city")
async def city(request):
    city = request.args.get("city") 
    print(city)
    return response.json({"city":city,"time":time()})
@app.on_response
async def handler_response(request,response):
    response.headers["Access-Control-Allow-Origin"] ="*"



