from django.http import FileResponse

from django.conf import settings


def home_view(request):
    page = settings.BASE_DIR / "public" / "index.html"
    return FileResponse(page.open("rb"), content_type="text/html; charset=utf-8")
