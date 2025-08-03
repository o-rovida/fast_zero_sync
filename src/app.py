from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root() -> Dict[str, str]:
    return {'message': 'O mundo é bão, Sebastião!'}
