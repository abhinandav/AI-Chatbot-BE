from fastapi import APIRouter
from pydantic import BaseModel
from app.services.embedder import get_embedding
from app.services.retriever import retrieve_top_k
from app.services.gemini import generate_answer
from app.storage.redis_client import add_to_history, get_history, clear_history



router = APIRouter()

# Request body schema
class ChatRequest(BaseModel):
    message: str
    session_id: str

# Response schema
class ChatResponse(BaseModel):
    answer: str



@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    context_chunks = retrieve_top_k(request.message, k=3)
    context = "\n".join(context_chunks)

    # Step 3: Placeholder LLM call
    final_answer = generate_answer(context=context, query=request.message)
    add_to_history(request.session_id,request.message,final_answer)

    return ChatResponse(answer=final_answer)


@router.get("/session/{session_id}")
async def get_session_history(session_id: str):
    history = get_history(session_id)
    return {"session_id": session_id, "history": history}

@router.delete("/session/{session_id}")
async def delete_session_history(session_id: str):
    clear_history(session_id)
    return {"message": f"Session {session_id} cleared."}