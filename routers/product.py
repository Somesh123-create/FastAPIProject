from fastapi import APIRouter, Depends, Header
from typing import Optional, List
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch', 'camera', 'phone']

@router.get("/all")
def all_product():
    data = " ".join(products)
    return Response(content=data, media_type='text/plain')



@router.get("/customheader")
def custom_headers(response: Response):
    if custom_header:
        response.headers['test_header'] = " and Hello "
    return products

@router.get('/{id}',responses={
    200:{
        "content":{
            "text/html" : {
                "example":"<div>Product</div>"
            }
        },
        "description":"Returns HTML for object"
    },
    404:{
        "content":{
            "text/plain":{
                "example": "Product not available"
            }
        },
        "description":"Returns cleartext error message"
    }
    })
def get_product(id:int):
    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(status_code=404, content=out, media_type="text/plain")
    else:
        product = products[id]
        out = f"""
        <head>
        <style>
        .product {{
            color:black;
            background-color:blue;
            text-align:center;
        }}
        </style>
        </head>
        <div class="product">
        {product}
        <div>
        """
        return HTMLResponse(content=out, media_type="text/html")
