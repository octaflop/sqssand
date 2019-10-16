Set up SQS in AWS console.

Edit `smoke_test.py` and change the following variables to your AWS config:

- `QUEUE_URL` to your sqs queue url.
- `AWS_ACCESS_KEY`
- `AWS_SECRET_KEY`
- `AWS_SESSION_TOKEN`


Run this:

```bash
pip install -r requirements.txt
python smoke_test.py
```

