# AG-UI ADK Endpoint

[AG-UI](https://github.com/ag-ui-protocol/ag-ui/blob/main/integrations/adk-middleware/python/src/ag_ui_adk/) has realeased a ADK middleware for python. But it does not fullfill Google ADK's core features. Some functionality like ADK plugin is not supported.

I start this project to add some missing features. It could be used as a fundamental ADK middleware for your project.

## Get started

Install `just` and `uv` command before start:
```bash
sudo apt install just
```

Set up the environment variables:
```bash
export GOOGLE_API_KEY=<your-google-api-key>
```

1. Build the `agui_adk_endpoint`
```bash
just build
```

2. Install the `agui_adk_endpoint` to example
```bash
just install
```

3. Run the example
```bash
just run-backend
just run-frontend
```

## Usage

1. Install `agui_adk_endpoint` to your project
```bash
pip install agui_adk_endpoint
```

2. Use `agui_adk_endpoint` in your project

`agui_adk_endpoint` would scan the `ADK_AGENT_DIR` environment variable to find all agents. The agents should be in the `agents` folder and follows `Google ADK`'s agent structure. The follow code would create a webserver with ag-ui endpoints `http://0.0.0.0:8000/adk/{agent_name}/run`.

```python
import uvicorn
import os

os.environ["ADK_AGENT_DIR"] = "./agents"

# Run the webserver
if __name__ == "__main__":
    uvicorn.run("agui_adk_endpoint.webserver:create_webserver", host="0.0.0.0", port=8000, reload=True)
```

## License

MIT