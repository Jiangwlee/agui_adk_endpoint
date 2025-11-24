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

## License

MIT