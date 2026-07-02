from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.services import get_events, get_statistics
from fastapi.responses import FileResponse

from system.system_health import health
import os

router = APIRouter()

templates = Jinja2Templates(
    directory="backend/templates"
)


@router.get("/")
def api():

    return {
        "project": "CADMS",
        "status": "Running"
    }


@router.get("/events")
def events():

    return get_events()


@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "events": get_events(),

            "stats": get_statistics()

        }
    )

@router.get("/evidence")
def view_evidence(path: str):

    if os.path.exists(path):
        return FileResponse(path)

    return {
        "error": "Evidence not found"
    }

@router.get("/stats")
def stats():

    return get_statistics()

@router.get("/system")
def system():

    return health.read()