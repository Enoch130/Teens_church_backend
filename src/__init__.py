from fastapi import FastAPI
from src.middleware.cors_validation import cors_validation_middleware
from src.middleware.error_response_wrapper import register_exception_handlers
from src.middleware.security import security_headers_middleware
from src.middleware.success_response_wrapper import SuccessResponseWrapperMiddleware
from src.middleware.whitelisting_middleware import IPWhitelist
from src.shared import override_docs
from contextlib import asynccontextmanager
from src.db.session import init_db
import os
# from src.shared.services.cloudinary.file_router import irouter


# Dynamically get the GeoIP DB path based on the current file location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Folder where __init__.py is located
GEOIP_DB_PATH = os.path.join(BASE_DIR, "GeoLite2-Country.mmdb")

@asynccontextmanager
async def life_span(app: FastAPI):
    """Run tasks when the app starts and stops."""
    print("Server Is Starting up...")
    await init_db()  # Initialize database connection/session
    yield
    print("Server Is Shutting down...")

# Create the FastAPI app instance
app = FastAPI(
    title="BinByte Backend API",
    description="API that supports the backend of BinByte Application",
    version="1.0.0",
    docs_url=None,  # Disable default Swagger docs (for security)
    redoc_url=None,  # Disable ReDoc docs
    lifespan=life_span
)

# ========================
# Exception Registration
# ========================
register_exception_handlers(app)


# ========================
# Middleware Registration
# ========================

#2️⃣ IP + Country whitelisting (runs first)
app.add_middleware(
   IPWhitelist,
   allowed_ips=["*"],     # Directly allowed IPs
   allowed_countries=["GH","US"],      # ISO country code for Ghana
    geoip_db_path=GEOIP_DB_PATH    # Local GeoIP DB (absolute path)
)

# 3️⃣ CORS validation (runs after whitelist check)
app.middleware("http")(cors_validation_middleware)
app.middleware("http")(security_headers_middleware)

# 4️⃣ Success response wrapper (runs last)
app.add_middleware(SuccessResponseWrapperMiddleware)

# ========================
# Routers
# ========================
app.include_router(router=override_docs.router, prefix="/bapi")



# ========================
# Test Route
# ========================
@app.get("/")
async def home():
    """Test route to confirm the server is working."""
    return {"message": "Welcome, Ghana!"}

