# FastAPI — Interview-Ready Study Guide

A concept-by-concept walkthrough covering everything in a typical FastAPI series. Each section gives you the *what*, the *why*, the *code*, and the *interview angle*.

---

## 0. The 30-Second Pitch (memorize this)

FastAPI is a modern, high-performance Python web framework for building APIs, built on **Starlette** (web/ASGI layer) and **Pydantic** (data validation). Its three selling points:

1. **Fast** — comparable to Node.js/Go because it's async (ASGI), not WSGI.
2. **Type-driven** — you write standard Python type hints; FastAPI uses them for validation, serialization, and docs automatically.
3. **Auto docs** — generates interactive Swagger UI (`/docs`) and ReDoc (`/redoc`) for free from your code.

> **Interview line:** "FastAPI gives you editor autocompletion, runtime validation, and OpenAPI docs all from a single source of truth: Python type hints."

---

## 1. Setup & First App

```bash
pip install "fastapi[standard]"   # includes uvicorn
```

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

Run it:
```bash
uvicorn main:app --reload     # main = file, app = FastAPI instance
# or with newer CLI:
fastapi dev main.py
```

**Why uvicorn?** FastAPI is an *ASGI* framework (asynchronous). Uvicorn is the ASGI *server* that actually runs it. Flask uses WSGI (synchronous) servers like Gunicorn.

> **Interview angle:** Know the difference — **WSGI** (sync, one request blocks a worker) vs **ASGI** (async, can handle many concurrent connections on one worker via an event loop).

---

## 2. Path Parameters

Parts of the URL path itself.

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):      # type hint → automatic validation + conversion
    return {"item_id": item_id}
```

- `/items/5` → `item_id` becomes the integer `5`.
- `/items/abc` → automatic **422 Unprocessable Entity** error, because `abc` isn't an int. You wrote zero validation code.

**Order matters.** Fixed paths must come *before* parameterized ones:
```python
@app.get("/users/me")        # define this FIRST
def current_user(): ...

@app.get("/users/{user_id}") # otherwise "me" gets captured as user_id
def get_user(user_id: int): ...
```

**Enum for fixed choices:**
```python
from enum import Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"

@app.get("/models/{name}")
def get_model(name: ModelName):
    return {"model": name}
```

---

## 3. Query Parameters

Function arguments that *aren't* in the path become query params (`?key=value`).

```python
@app.get("/items/")
def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
# GET /items/?skip=20&limit=5
```

- A **default value** → optional query param.
- **No default** → required.
- `q: str | None = None` → optional, can be omitted.

**Rule of thumb interviewers like:** If the param name appears in the path string `{}`, it's a path param; otherwise FastAPI treats it as a query param.

---

## 4. Request Body & Pydantic Models

This is the heart of FastAPI. You declare the shape of incoming JSON as a Pydantic model.

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
def create_item(item: Item):
    return item
```

What FastAPI does automatically:
1. Reads the request body as JSON.
2. Validates each field against its type (rejects bad data with 422).
3. Gives you a typed `item` object with editor autocomplete.
4. Documents the body schema in `/docs`.

**Combining all three sources** — path, query, and body — in one endpoint:
```python
@app.put("/items/{item_id}")
def update(item_id: int, item: Item, q: str | None = None):
    ...
# item_id → path, item → body (it's a Pydantic model), q → query
```
FastAPI tells them apart by type: Pydantic model = body, singular type = path/query.

> **Interview gold:** "Pydantic is doing the validation, not FastAPI itself. FastAPI orchestrates; Pydantic enforces the schema."

---

## 5. Validation: Query, Path, and Field

Use `Query`, `Path`, and Pydantic's `Field` to add constraints and metadata.

```python
from fastapi import Query, Path
from typing import Annotated

@app.get("/items/")
def read(
    q: Annotated[str | None, Query(max_length=50, min_length=3)] = None,
    item_id: Annotated[int, Path(ge=1)] = ...,
):
    ...
```

Common constraints: `gt`, `ge`, `lt`, `le` (numbers), `min_length`, `max_length`, `pattern` (strings).

Inside models, use `Field`:
```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    price: float = Field(gt=0, description="Must be positive")
```

`Annotated` is the modern, recommended syntax — know it for interviews.

---

## 6. Response Models

Control and validate what goes *out*. Critical for not leaking sensitive fields (e.g., passwords).

```python
class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str          # no password field

@app.post("/users/", response_model=UserOut)
def create_user(user: UserIn):
    return user            # password is stripped from the response automatically
```

- `response_model` filters the output to only declared fields.
- `response_model_exclude_unset=True` omits fields the client didn't set.

> **Interview angle:** Separate input and output models. Never return your DB/ORM model directly if it has secrets. This is a security best practice they love to hear.

---

## 7. Status Codes & Error Handling

```python
from fastapi import HTTPException, status

@app.get("/items/{id}")
def get(id: int):
    if id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    return db[id]
```

- Set a default success code: `@app.post("/items/", status_code=201)`.
- Raise `HTTPException` for client-facing errors; FastAPI turns it into a clean JSON response.
- Custom exception handlers via `@app.exception_handler(MyError)`.

Know the common codes: **200** OK, **201** Created, **204** No Content, **400** Bad Request, **401** Unauthorized, **403** Forbidden, **404** Not Found, **422** Validation Error (FastAPI's default for bad input), **500** Server Error.

---

## 8. Dependency Injection (the FastAPI superpower)

A dependency is a function whose return value is injected into your endpoint. Used for shared logic: DB sessions, auth, pagination, config.

```python
from fastapi import Depends
from typing import Annotated

def common_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
def items(commons: Annotated[dict, Depends(common_params)]):
    return commons
```

- Dependencies can depend on other dependencies (nested).
- They run *before* your endpoint; results are cached within a request.
- Classes can be dependencies too (`Depends(MyClass)`).

**`yield` dependencies** — for setup/teardown (the classic DB session pattern):
```python
def get_db():
    db = SessionLocal()
    try:
        yield db          # code before yield = setup
    finally:
        db.close()        # code after yield = teardown, runs after response
```

> **Interview gold:** DI is FastAPI's mechanism for reusability and testability. In tests you can `app.dependency_overrides[get_db] = fake_db` to swap a real DB for a mock. This is a *very* common interview question.

---

## 9. Async vs Sync (`async def` vs `def`)

```python
@app.get("/sync")
def sync_route():          # runs in a threadpool, won't block event loop
    ...

@app.get("/async")
async def async_route():   # runs on the event loop
    result = await some_async_db_call()
    ...
```

**The rule:**
- Use `async def` when you call libraries with `await` (async DB drivers, httpx, etc.).
- Use plain `def` when your code is blocking/synchronous (most ORMs like sync SQLAlchemy). FastAPI runs `def` routes in a threadpool so they don't block the loop.
- **Never** put a blocking call (e.g., `time.sleep`, sync `requests`) inside an `async def` — it freezes the entire event loop and kills concurrency.

> **Interview trap:** "Is more async always faster?" No. If your work is CPU-bound or you call blocking libraries, `async def` hurts. Match the keyword to the nature of the work.

---

## 10. Routers — Structuring a Real App

You don't put everything in one file. Split routes with `APIRouter`.

```python
# routers/users.py
from fastapi import APIRouter
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def list_users(): ...

# main.py
from fastapi import FastAPI
from routers import users
app = FastAPI()
app.include_router(users.router)
```

Typical project layout:
```
app/
  main.py          # app instance, include routers
  models.py        # SQLAlchemy ORM models
  schemas.py       # Pydantic models
  database.py      # engine, SessionLocal, get_db
  routers/
    users.py
    items.py
```

> **Interview angle:** Know `tags` (groups endpoints in docs), `prefix`, and `dependencies=[...]` on a router (applies a dependency to every route in it — e.g., auth on a whole admin router).

---

## 11. Database Integration (SQLAlchemy)

The standard stack. Three layers: **engine/session**, **ORM models**, **Pydantic schemas**.

```python
# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///./app.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

```python
# endpoint using the DB dependency
@app.post("/items/")
def create(item: ItemSchema, db: Session = Depends(get_db)):
    db_item = ItemModel(**item.dict())
    db.add(db_item); db.commit(); db.refresh(db_item)
    return db_item
```

To return ORM objects through a Pydantic `response_model`, enable ORM mode:
```python
class ItemOut(BaseModel):
    id: int
    name: str
    model_config = {"from_attributes": True}   # Pydantic v2 (was orm_mode in v1)
```

> **Interview point:** Three model types coexist — **ORM models** (DB tables), **Pydantic schemas** (validation/serialization), and they're deliberately separate concerns.

---

## 12. Authentication (OAuth2 + JWT)

The canonical FastAPI auth flow:

1. User POSTs username/password to `/token`.
2. You verify against the DB (hashed password via `passlib`/`bcrypt`).
3. You return a signed **JWT** access token.
4. Client sends `Authorization: Bearer <token>` on future requests.
5. A dependency decodes/validates the token and returns the current user.

```python
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login(form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # verify user, then:
    token = create_jwt({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    payload = decode_jwt(token)   # raises 401 if invalid
    return get_user(payload["sub"])

@app.get("/users/me")
def me(user: Annotated[User, Depends(get_current_user)]):
    return user
```

Key terms to know: **hashing** (never store plaintext passwords), **JWT** (header.payload.signature, stateless), **Bearer token**, **scopes** (fine-grained permissions).

---

## 13. Other Things Worth Knowing

- **Automatic docs:** `/docs` (Swagger UI), `/redoc` (ReDoc), `/openapi.json` (the schema). All generated from your code.
- **CORS:** `from fastapi.middleware.cors import CORSMiddleware` — needed when a browser frontend on a different origin calls your API.
- **Middleware:** functions that run on every request/response (logging, timing).
- **Background tasks:** `BackgroundTasks` for fire-and-forget work (send email after responding) without blocking the response.
- **`Form` / `File` / `UploadFile`:** for form data and file uploads (requires `python-multipart`).
- **Pydantic v2:** big rewrite, Rust core, much faster. `orm_mode` → `from_attributes`, `.dict()` → `.model_dump()`, `Config` class → `model_config` dict. Mention you know v2 changed these.

---

## 14. Rapid-Fire Interview Q&A

**Q: FastAPI vs Flask?**
A: Flask is WSGI/sync and minimal; you add validation and docs yourself. FastAPI is ASGI/async, with built-in Pydantic validation and auto OpenAPI docs from type hints. FastAPI is generally faster for I/O-bound concurrent workloads.

**Q: Why is FastAPI fast?**
A: It's async (ASGI + uvicorn), so one worker handles many concurrent I/O-bound requests via an event loop instead of blocking.

**Q: What does Pydantic do here?**
A: Validates and parses request data against type hints, serializes responses, and produces the JSON schema for docs. It's the validation engine.

**Q: What is `Depends` for?**
A: Dependency injection — reusable, testable shared logic (DB sessions, auth, pagination). Overridable in tests.

**Q: 422 vs 400?**
A: 422 is FastAPI's automatic response for body/param validation failures. 400 is a general bad-request you raise manually for business-rule violations.

**Q: When NOT to use `async def`?**
A: When calling blocking/synchronous libraries — it would block the event loop. Use plain `def` (runs in a threadpool) instead.

**Q: How do you hide a password from a response?**
A: Use a separate `response_model` (output schema) that doesn't include the field.

**Q: How do you test a FastAPI app?**
A: `TestClient` (or `httpx.AsyncClient`) plus `app.dependency_overrides` to swap real dependencies (like the DB) for fakes.

---

## 15. 3-Day Study Plan

- **Day 1:** Sections 1–7. Build a tiny CRUD app (in-memory dict) covering path/query params, Pydantic bodies, response models, status codes.
- **Day 2:** Sections 8–11. Add dependency injection and SQLAlchemy; split into routers. Internalize async vs sync.
- **Day 3:** Sections 12–14. Add JWT auth; write 2–3 tests with `TestClient` and `dependency_overrides`. Drill the Q&A out loud.

Do the typing yourself — interviewers ask you to reason about *why*, and muscle memory from building beats re-watching video.
