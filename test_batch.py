import ssl
import truststore
import httpx
from openai import OpenAI

ssl_context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

client = OpenAI(
    base_url="https://portal.ai.gateway/v1",
    api_key="sk-GsNwdMUVXAnlLiEvxjh4VA",
    http_client=httpx.Client(verify=ssl_context),
)

batch = client.batches.retrieve("batch_6a46a6ec20b08190b4748741934e0218")
print(batch)