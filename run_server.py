import uvicorn


if __name__ == "__main__":
    app_name = "app:app"
    uvicorn.run(
        app_name,
        host="127.0.0.1",
        port=9090, 
        reload=True
        )