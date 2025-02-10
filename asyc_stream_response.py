@app.post("/stream")
async def stream_agent(user_input: StreamInput):
    """
    Stream the agent's response to a user input, including intermediate messages and tokens.
    
    Use thread_id to persist and continue a multi-turn conversation. run_id kwarg
    is also attached to all messages for recording feedback.
    """
    return StreamingResponse(message_generator(user_input), media_type="text/event-stream")
