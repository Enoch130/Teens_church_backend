import time
from redis.asyncio import Redis
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.types import ASGIApp


class RedisRateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        redis: Redis,
        limit: int = 100,
        window: int = 60,
        prefix: str = "rate_limit",
    ) -> None:
        super().__init__(app)
        self.redis = redis
        self.limit = limit
        self.window = window  # in seconds
        self.prefix = prefix

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        ip: str = request.client.host  # type: ignore
        key: str = f"{self.prefix}:{ip}"
        current_ts: int = int(time.time())

        pipeline = self.redis.pipeline()
        pipeline.zadd(key, {str(current_ts): current_ts})
        pipeline.zremrangebyscore(key, 0, current_ts - self.window)
        pipeline.zcard(key)
        pipeline.expire(key, self.window + 10)

        _, _, count, _ = await pipeline.execute()

        if count > self.limit:
            raise HTTPException(
                status_code=429, detail="Rate limit exceeded. Try again later."
            )

        return await call_next(request)


# from redis.asyncio import Redis
# from src.middleware.rate_limiting_middleware import RedisRateLimitMiddleware


# redis = Redis.from_url("redis://localhost", decode_responses=True)  # type: ignore


# Redis Rate Limiting Middleware
# app.add_middleware(
#     RedisRateLimitMiddleware,
#     redis=redis,
#     limit=50,  # e.g. 50 requests
#     window=60,  # in 60 seconds
#     prefix="ratelimit",  # optional
# )
