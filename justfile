set dotenv-load := true
set export

build:
  echo "Building agui_adk_endpoint..."
  cd agui_adk_endpoint && uv clean && uv build

install:
  echo "Installing agui_adk_endpoint to example backend..."
  cd examples/backend && uv pip uninstall agui-adk-endpoint && uv pip install ../../agui_adk_endpoint/dist/*.whl

run-backend:
  echo "Running example backend..."
  cd examples/backend && uv run main.py

run-frontend:
  echo "Running example frontend..."
  cd examples/frontend/copilotkit-next && npm run dev

clean:
  echo "Cleaning agui_adk_endpoint..."
  cd agui_adk_endpoint && uv clean


