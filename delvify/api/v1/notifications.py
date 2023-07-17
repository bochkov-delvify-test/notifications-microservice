from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from delvify import schemas
from delvify.core import get_email_service, logger

endpoint = APIRouter()


@endpoint.post("/email", response_model=None)
def send_email(*, form: schemas.Email, email_service=Depends(get_email_service)) -> Any:
    try:
        email_service.send_email(email=form)
        return
    except Exception as e:
        logger.error("Failed to send email", exc_info=e)
        raise HTTPException(status_code=500, detail="Failed to send email.")
