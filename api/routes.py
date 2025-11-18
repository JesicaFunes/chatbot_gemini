from fastapi import APIRouter, HTTPException
from schemas import chatRequest, chatResponse
from .chat_service import ChatService 
from roles import RolesPreset

router = APIRouter()


chat_service = ChatService(role=RolesPreset.ASISTENTE)


@router.post("/chat", response_model=chatResponse)

async def chat_endpoint(request: chatRequest):
    
    
    if not request.mensaje:
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío.")
    
    
    if request.reset:
        chat_service.reset() 

    rol_solicitado = RolesPreset(request.role.lower())
    
    if rol_solicitado != chat_service.role:
        try:
            
            chat_service.set_role(rol_solicitado)
        
        except ValueError:
            
            raise HTTPException(status_code=400, detail=f"Rol desconocido: {request.role}")
    
   
    try:
        
        respuesta = chat_service.ask(request.mensaje) 
        
        return chatResponse(respuesta=respuesta) 
    
    except Exception as e:
        
        raise HTTPException(status_code=500, detail=f"Error en el servicio de chat: {str(e)}")