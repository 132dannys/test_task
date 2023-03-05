from pydantic import BaseModel, Field, root_validator


class Product(BaseModel):
    article: int = Field(alias='nm_id')
    brand: str 
    title: str 

    @root_validator(pre=True)
    def validate_brand(cls, values):
        values['brand'] = values['selling']['brand_name']
        values['title'] = f"{values['brand']} / {values['imt_name']}"
        return values
    