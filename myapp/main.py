import uvicorn
from fastapi import FastAPI
from mangum import Mangum


###############################################################################
#   Application object for the API                                            #
###############################################################################
myapp_api = FastAPI(title="My FastAPI application")


###############################################################################
#   GET API endpoints                                                         #
###############################################################################
@myapp_api.get("/")
async def welcome_page():
      return {"message": "Welcome to My APP"}

@myapp_api.get(path="/test")
async def test_page():
        return {"message": "Test Works!"}


###############################################################################
#   Handler for AWS Lambda                                                    #
###############################################################################
handler = Mangum(myapp_api)

###############################################################################
#   Run the self contained application                                        #
###############################################################################
if __name__ == "__main__":
    uvicorn.run(myapp_api, host="0.0.0.0", port=5000)
