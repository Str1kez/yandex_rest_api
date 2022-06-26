from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['code'] = response.status_code
        if response.status_code == 404:
            response.data['message'] = "Item not found"
        else:
            response.data['message'] = response.data['detail']
        response.data.pop('detail')

    return response

