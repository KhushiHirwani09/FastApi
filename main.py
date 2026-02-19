from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session
import model
from database import engine,sessionlocal

app=FastAPI()



def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/createuser")
def create_user(username:str,age:int,id:int,department:str,phoneno:str,db:Session=Depends(get_db)):
    user=model.User(username=username,age=age,id=id,department=department,phoneno=phoneno)
    db.add(user)
    db.commit()
    db.refresh(user)
    return{
        "id":user.id,
        "name":user.username,
        "age":user.age,
        "department":user.department,
        "phoneno":user.phoneno,
    }

@app.put("/updateuser")
def update_user(username:str,age:int,id:str,department:str,phoneno:str,db:Session=Depends(get_db)):
    user=db.query(model.User).filter(model.User.id==id).first()
    if not user:
        raise HTTPException(status_code=404,detail="user doesnot exist..")
    if username is not None:
        user.username=username
    if age is not None:
        user.age=age
    if department is not None:
        user.department=department
    if phoneno is not None:
        user.phoneno=phoneno
    db.commit()
    

    return{
        "id":user.id,
        "name":user.username,
        "age":user.age,
        "department":user.department,
        "phoneno":user.phoneno,
    }

@app.delete("/deleteuser")
def delete_user(id:int,db:Session=Depends(get_db)):
    user=db.query(model.User).filter(model.User.id==id).first()
    if not user:
        raise HTTPException(status_code=404,detail="user doesnot exist..")
    db.delete(user)
    db.commit()
    return {"message":"f user with Id {user.id} has been deleted."}
    