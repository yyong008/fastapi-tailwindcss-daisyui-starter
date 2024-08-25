import arel
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_tailwindcss_daisyui_starter.config.config import settings

app = FastAPI()

app.mount('/static', StaticFiles(directory="static"), name='static')

templates = Jinja2Templates(directory="./fastapi_tailwindcss_daisyui_starter/templates")

if settings.DEBUG:
    hot_reload = arel.HotReload(paths=[arel.Path(".")])
    app.add_websocket_route("/hot-reload", route=hot_reload, name="hot-reload")
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    templates.env.globals["DEBUG"] = settings.DEBUG
    templates.env.globals["hot_reload"] = hot_reload

@app.get("/")
def home(request: Request):
  return templates.TemplateResponse('index.html', { "request": request, "data": {} })

def start():
  import uvicorn
  uvicorn.run("main:app", reload=True, port=8888)

if __name__ == "__main__":
  start()
