
async def restart_run_tasks():
    import parserkufar
    parserkufar.should_run=False
async def start_run_tasks():
    import parserkufar
    parserkufar.should_run=True