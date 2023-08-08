from fastapi import Depends
from pydantic import Field
from app.utils import AppModel
from ..service import Service, get_service
from . import router


class GetModel(AppModel):
    phys: dict = Field(alias="Физика")
    math: dict = Field(alias="Математика")
    chem: dict = Field(alias="Химия")


@router.get("/json", response_model=GetModel)
def get_topic(
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    json = svc.repository.get_topic_by_id()
    return GetModel(phys=json["Физика"], math=json["Математика"], chem=json["Химия"])
