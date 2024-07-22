from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForMaskedLM, pipeline

app = FastAPI()

# Load the language model and tokenizer
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForMaskedLM.from_pretrained(model_name)
fill_mask = pipeline("fill-mask", model=model, tokenizer=tokenizer)

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    filled_texts: list

@app.get("/")
def read_root():
    return {"message": "Welcome to the BERT Language Model API"}

@app.post("/generate_text")
async def generate_text(request: TextRequest):
    if "[MASK]" not in request.text:
        raise HTTPException(status_code=400, detail="The input text must contain the [MASK] token.")

    try:
        results = fill_mask(request.text)
        filled_texts = [result['sequence'] for result in results]
        return TextResponse(filled_texts=filled_texts)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating text: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
