"""Local API scaffold. No production deployment is claimed."""
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field,ConfigDict
app=FastAPI(title='Resource allocation under uncertainty',version="0.1.0",description="Research baseline; see README for assumptions and incomplete work.")
@app.get("/health")
def health():return {"status":"ok","implementation":"research_baseline","version":"0.1.0"}
class CandidateInput(BaseModel):
 model_config=ConfigDict(extra="forbid",allow_inf_nan=False)
 id: str=Field(min_length=1,max_length=80)
 position: str=Field(min_length=1,max_length=30)
 cost: float=Field(ge=0)
 mean: float
 variance: float=Field(ge=0)
class Request(BaseModel):
 model_config=ConfigDict(extra="forbid",allow_inf_nan=False)
 candidates:list[CandidateInput]=Field(max_length=20)
 budget:float=Field(ge=0)
 requirements:dict[str,int]
 risk_aversion:float=Field(default=0,ge=0)
@app.post("/v1/baseline")
def baseline(request:Request):
 from .core import Candidate,allocate
 try:
  result=allocate([Candidate(**c.model_dump()) for c in request.candidates],request.budget,request.requirements,request.risk_aversion)
 except ValueError as e:raise HTTPException(422,str(e)) from e
 return {"version":"0.1.0","status":"research_baseline","result":result}
