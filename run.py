from typing import List
from fastapi import FastAPI, HTTPException

from schemas.account_schemas import AccountCreate

app = FastAPI()

@app.post("/accounts/", response_model=AccountCreate)
def create_account(account: AccountCreate):
    return account.model_dump()


@app.get("/accounts/", response_model=List[AccountCreate])
def get_all_accounts():
    return [AccountCreate.Config.json_schema_extra["example"]]

@app.get("/accounts/{account_id}")
async def get_account_by_id(account_id):
    return {"message": account_id}
