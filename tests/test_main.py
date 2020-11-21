import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url='http://test') as cli:
        response = await cli.get('/')
        print(response.json())
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


@pytest.mark.asyncio
async def test_sum():
    async with AsyncClient(app=app, base_url='http://test') as cli:
        response = await cli.get('/sum', params={
            'a': 25,
            'b': 15
        })
        print(response.json())
    assert response.status_code == 200
    assert response.json() == {"sum": 40}
