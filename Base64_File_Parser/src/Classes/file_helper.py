import base64 
# Clase con utilidades para comprobaciones del fichero
class File_Checker:
             
    def __init__(self):
        self.file_tag = 'file'
        self.body_base64_file = None

    def check_the_file(self, req, base64_file):
        # Comprobamos que el fichero no este vacío y revisamos en el body por
        # si han usado Soap o Rest
        if not base64_file:
            try:
                req_body = req.get_json()
            except (ValueError, TypeError):
                pass
            else:
                base64_file = req_body.get(self.file_tag)
                self.body_base64_file = base64_file
                return True
        else:
            return True
    
    def __getattribute__(self, name):
        return super().__getattribute__(name)

# Clase encargada de los parseamientos en el fichero
class File_Parser:

    def __init__(self):
        self.new_file = open('FileToSend.txt','w+')        
        
    
    def base64_decode(self, file_to_parse):
        return base64.b64decode(file_to_parse)
    
    


