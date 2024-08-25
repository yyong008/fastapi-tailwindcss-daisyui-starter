# fastapi-tailwindcss-daisyui-starter

fastapi-tailwindcss-daisyui-starter is starter with tailwindcss and daisyui. you can easy controller you website and css styles。

## Python and Node.js Env

- Python and Poetry
- Node.js and pnpm

## starter

```sh
git clone https://github.com/yyong008/fastapi-tailwindcss-daisyui-starter

cd <fastapi-tailwindcss-daisyui-starter dir>

poetry install

pnpm install

pnpm run tailwind # watch templates/html files change

poetry run python main.py # start fastapi server
```

Now, you can visit fastapi server on `http://localhost:8000`, change the  `template/xxx.html` watch browser fresh。

## env

pydantic-settings Control the env DEBUG. if you set False, no browser refresh。

```
DEBUG = True
```

## arel

arel can inject reload script antd use websocket to control the file change

```py
import arel
from fastapi_tailwindcss_daisyui_starter.config.config import settings

if settings.DEBUG:
    hot_reload = arel.HotReload(paths=[arel.Path(".")])
    app.add_websocket_route("/hot-reload", route=hot_reload, name="hot-reload")
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    templates.env.globals["DEBUG"] = settings.DEBUG
    templates.env.globals["hot_reload"] = hot_reload

```

```html
{% if DEBUG %} {{ hot_reload.script(url_for('hot-reload')) | safe }} {% endif %}
```

## daisyui

daisyui base tailwindcss, it's a plugin when where use it。

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
   content: ["./fastapi_tailwindcss_daisyui_starter/templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
}
```

Now you can enjoy it ! Good day~
