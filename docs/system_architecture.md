# System Architecture

# GATE Mock Test Generation & Analytics Platform

## Overview

The GATE Mock Test Generation & Analytics Platform is a full-stack web application that generates balanced GATE Computer Science (CSE) mock tests using a rule-based generation engine. Instead of serving predefined question papers, the system dynamically assembles mock tests by selecting questions from a structured question bank while following GATE blueprint constraints.
The platform also evaluates student submissions and provides performance analytics .

---

# High-Level Architecture

```
                    +----------------------+
                    |      Frontend        |
                    |  React Application   |
                    +----------+-----------+
                               |
                               | HTTP Requests
                               |
                    +----------v-----------+
                    |     FastAPI APIs     |
                    | (Route Handlers)     |
                    +----------+-----------+
                               |
                 +-------------+--------------+
                 |                            |
                 |                            |
        +--------v--------+          +--------v--------+
        |   Auth System   |          |  Pydantic Schemas|
        | (JWT / Security)|          | (Validation)     |
        +--------+--------+          +------------------+
                 |
                 |
        +--------v--------+
        |   Service Layer  |
        | (Business Logic) |
        +--------+--------+
                 |
     +-----------+------------+
     |                        |
     |                        |
+----v-----+          +--------v--------+
|Generation|          |   Analytics     |
| Engine   |          |     Engine      |
+----+-----+          +--------+--------+
     |                         |
     +------------+------------+
                  |
        +---------v----------+
        | PostgreSQL Database |
        +---------+----------+
                  |
      +-----------+------------+
      |                        |
      |                        |
+-----v------+          +-------v------+
|Question Bank|          |Knowledge Base|
+-------------+          +--------------+
---

# Layered Architecture

The application follows a layered architecture to ensure modularity, maintainability, and separation of concerns.

## 1. Presentation Layer

Responsible for user interaction.

Components:

- Login
- Dashboard
- Mock Test Interface
- Results Page
- Analytics Dashboard

Technology:

- React
- HTML
- CSS
- JavaScript

---

## 2. API Layer

Acts as the communication bridge between the frontend and backend.

Responsibilities:

- Receive HTTP requests
- Validate input
- Route requests
- Return JSON responses

Endpoints include:

- Authentication
- Mock generation
- Mock retrieval
- Attempt submission
- Analytics

---

## 3. Service Layer

Contains the business logic of the application.

Responsibilities:

- Generate mock tests
- Evaluate attempts
- Calculate scores
- Retrieve questions
- Generate analytics

Services:

- Mock Generation Service
- Question Service
- Analytics Service
- Authentication Service

---

## 4. Generation Engine

The generation engine ensures:

- Balanced topic coverage
- Balanced difficulty distribution
- No duplicate questions
- Correct number of questions
- Correct mark allocation

---

# Mock Generation Workflow

```
Student
   │
   ▼
POST /mock/generate
   │
   ▼
FastAPI Route Handler
   │
   ▼
Service Function (generate_mock)
   │
   ▼
Database (Concepts + Questions)
   │
   ▼
Rule-Based Selection Logic
   │
   ├── Weightage Allocation
   ├── Difficulty Split
   ├── Question Sampling
   ├── Deduplication
   └── Shuffling + Trimming
   │
   ▼
MockTest + MockQuestion DB Insert
   │
   ▼
Response (mock_test)
```

---

# Attempt Evaluation Workflow

```
Student
    │
    ▼
Submit Answers
    │
    ▼
Attempt API
    │
    ▼
Store Attempt
    │
    ▼
Evaluate Answers
    │
    ▼
Calculate Score
    │
    ▼
Generate Analytics
    │
    ▼
Store Results
    │
    ▼
Return Performance Report
```

---

# Analytics Workflow

```
Student Attempt
        │
        ▼
Compare with Correct Answers
        │
        ▼
Calculate Score
        │
        ▼
Generate Performance Summary
```

Generated analytics include:

- Total Score
- Accuracy 
- Attempted and Not-Attempted no. of questions
- Marks gained and Marks lost
- Attempt History

---

# Database Layer

The platform uses PostgreSQL as the primary database.

Major entities:

- User
- Subject
- Topic
- Subtopic
- Concept
- Question
- Question Option
- Mock Test
- Mock Question
- Student Attempt
- Attempt Answer

The database supports:

- Multiple attempts
- Multiple Mock Tssts
- Future scalability

---

# Project Structure

- Frontend(React)

src/
├── api/              → API communication layer(axios, endpoints)
├── components/      → Reusable UI components
├── pages/           → Application screens
├── utils/           → Helper functions (score, time)
├── App.jsx
├── main.jsx
└── index.css

- Backend(FastAPI)

backend/
├── models/          → Database models (SQLAlchemy)
├── database/        → DB connection & config
├── utils.py         → Helper functions (auth, selection logic)
├── schema.py        → Pydantic request/response schemas
└── main.py          → FastAPI entry point

- Data Layer

data/
├── question_bank/   → Stored questions
└── knowledge_base/  → Concept/topic metadata

---

# Technology Stack

## Frontend

- React
- HTML
- CSS
- JavaScript

## Backend

- Python
- FastAPI

## Database

- PostgreSQL
- SQLAlchemy

## Development Tools

- Git
- GitHub
- Postman

---

# Future Enhancements

The current implementation supports GATE CSE and GATE DA.

Future versions may include:


- AI-generated explanations
- Adaptive mock generation based on previous performance
- Personalized suggestions
- Timed sectional tests
- Leaderboards
- Performance prediction
- Question bookmarking

---

# Summary

This is a FastAPI-based mock test generation system that creates balanced exams using concept weightage and difficulty rules from a question bank. It also evaluates attempts and provides basic performance analytics. The design is modular, scalable, and easy to extend for new exams and features.