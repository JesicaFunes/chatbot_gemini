from pydantic import BaseModel 


class chatRequest(BaseModel):
   
    mensaje: str
    
    
    role: str = "asistente"
    
    
    reset: bool = False
    

class chatResponse (BaseModel):
   
    respuesta: str
    