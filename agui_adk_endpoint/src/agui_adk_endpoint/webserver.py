from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .endpoint import AdkFastAPIEndpoint
from .validator import validate_parameters

def create_webserver(
        host: str = '127.0.0.1', 
        port: int = 8000,
        allow_origins: Optional[list[str]] = None,) -> FastAPI:
    params = validate_parameters()

    app = FastAPI()

    if allow_origins:
      app.add_middleware(
          CORSMiddleware,
          allow_origins=allow_origins,
          allow_credentials=True,
          allow_methods=["*"],
          allow_headers=["*"],
      )

    # Add AG-UI endpoint
    endpoint = AdkFastAPIEndpoint(params=params)
    endpoint.add_fastapi_endpoint(app)

    return app


    