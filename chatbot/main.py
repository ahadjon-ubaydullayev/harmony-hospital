from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import generator  

# Define a Pydantic model for the input
class QueryRequest(BaseModel):
    question: str

# Create a FastAPI app instance
app = FastAPI()

@app.post("/generate/")
async def generate_response(query: QueryRequest):
    try:
        # Call the generator's review_chain with the user's question
        response = generator.review_chain.invoke(query.question)
        print(response)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health check endpoint
@app.get("/")
async def health_check():
    return {"message": "Backend is running!"}
