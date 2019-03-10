import logging as log
import azure.functions as func
from .src.Classes.file_helper import File_Checker as file_Checker     
from .src.Classes.file_helper import File_Parser  as file_parser


def main(req: func.HttpRequest) -> func.HttpResponse:
    log.info('Python HTTP trigger function processed a request.')
    file_tag = 'file'        
    
    base64_file = req.params.get(file_tag)
    on_header = file_Checker.check_the_file(file_Checker, req, base64_file)
    # Si no esta en el header (Rest) estara en el body (Soap)
    if not on_header:
        base64_file = file_Checker.__getattribute__(file_Checker,'body_base64_file')

    if base64_file:
        file_parser.__init__(file_parser)
        #string = str(file_parser.base64_decode)
        return func.HttpResponse(f""+ str(file_parser.base64_decode(file_parser,base64_file)))
        #return func.HttpResponse(f"Hello {'Va bien el test'}!")
    else:
        return func.HttpResponse(
             "Please pass a valid Base64 File on the query string or in the request body",
             status_code=400
        )
