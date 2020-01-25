import kopf


@kopf.on.create('baeke.info', 'v1', 'demowebs')
def create_fn(spec, **kwargs):
    print(f"Creating: {spec}")
    return {'message': 'done'}  # will be the new status
