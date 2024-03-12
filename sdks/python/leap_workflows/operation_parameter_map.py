operation_parameter_map = {
    '/v1/runs/bulk/{bulk_run_id}-GET': {
        'parameters': [
            {
                'name': 'bulk_run_id'
            },
        ]
    },
    '/v1/runs/bulk-POST': {
        'parameters': [
            {
                'name': 'workflow_id'
            },
            {
                'name': 'input_csv_url'
            },
            {
                'name': 'webhook_url'
            },
        ]
    },
    '/v1/runs/{workflow_run_id}-GET': {
        'parameters': [
            {
                'name': 'workflow_run_id'
            },
        ]
    },
    '/v1/runs-POST': {
        'parameters': [
            {
                'name': 'workflow_id'
            },
            {
                'name': 'webhook_url'
            },
            {
                'name': 'input'
            },
        ]
    },
};