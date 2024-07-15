
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from user.endpoints import router as user_router
from annotation.endpoints import router as annotation_router
from inspections.endpoints import router as inspection_router
from reports.endpoints import router as report_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup_event():
#     # Initiate the image broadcasting task with a default image folder and interval
#     image_folder = "Images"  # Specify your image folder here
#     asyncio.create_task(broadcast_images(image_folder, 1))

app.include_router(user_router, prefix='/accounts')
app.include_router(annotation_router, prefix='/annotation')
app.include_router(inspection_router, prefix='/inspection')
app.include_router(report_router, prefix='/report')

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
    