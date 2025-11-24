import uvicorn
import os

os.environ["ADK_AGENT_DIR"] = "./agents"

# Run the webserver
if __name__ == "__main__":
    uvicorn.run("agui_adk_endpoint.webserver:create_webserver", host="0.0.0.0", port=8000, reload=True)