from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    """
        responsabilidade para intereção com HTTP
    """
    def validate_and_create(self, http_request: HttpRequest) -> HttpRequest:
        body = http_request.body
        product_code = body["product_code"]

    
        
        return HttpResponse(status_code=200, body={"hello": "Word"})