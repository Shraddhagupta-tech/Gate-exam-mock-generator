User
- id int auto-increment primary key
- name varchar(50) not null
- email varchar(50) unique
- password_hash varchar(255) not null
- role (student/admin) default student
- created_at timestamp default current_timestamp
- updated_at timestamp default current_timestamp

Subject
- id int auto-increment primary key
- name varchar(50) unique

Topic
- id int auto-increment primary key
- subject_id int fk from subject
- name varchar(50)

Subtopic
- id int auto-increment primary key
- topic_id int fk from topic
- name varchar(50)

Concept
- id int auto-increment primary key
- concept_code varchar(50) unique
- subtopic_id int fk from subtopic
- difficulty_level enum(easy/medium/hard) 
- exam enum(CSE / DA)
- weightage 

Question
- id int primary key auto-increment
- concept_id int not null fk from concept
- template_id int fk from template
- question_text text not null
- question_type enum(MCQ / MSQ / NAT) not null
- difficulty enum(easy/medium/hard) not null
- explaination text
-- NAT specific
- correct_answer_value DECIMAL(10,4) NULL
- answer_tolerance DECIMAL(10,4) DEFAULT 0
- source enum(PYQ / AI / curated)
- created_at timestamp default current_timestamp

QuestionOption
- id int primary key auto_increment
- question_id int not null fk from question
- option_text text not null
- is_correct boolean not null

Template
- id int primary key auto-increment
- concept_id int not null fk from concept
- template_type (math/logic/graph)
- difficulty_range 

MockTest
- id int primary key auto-increment
- title varchar(100)
- exam_type ENUM('CSE','DA')
- created_by INT null fk from user
- total_marks int default 100
- total_questions int default 65
- duration_minutes int default 180
- is_generated BOOLEAN   ← AI or prebuilt
- created_at timestamp default current_timestamp

MockQuestion
- id int auto-increment primary key
- mocktest_id  int fk from mocktest
- question_id int fk from question
- question_order int 
- marks int
- UNIQUE(mocktest_id, question_order)
- UNIQUE(mocktest_id, question_id)

StudentAttempt
- id int auto-increment primary key
- user_id int fk from user
- mocktest_id int fk from mocktest
- score int default 0
- started_at timestamp
- completed_at timestamp
- status ENUM('in_progress','completed','submitted')

AttemptAnswer
- id int primary key auto-increment
- attempt_id int not null fk from StudentAttempt
- question_id int not null fk from Question
-- NAT answer
- answer_numeric DECIMAL(10,4) NULL
- answer_text TEXT NULL
- is_correct boolean
- marks_awarded int

AttemptOption
- id int pk auto-increment
- attempt_answer_id int not null
- option_id int not null


TopicPerformance
- id int 
- user_id
- concept_id
- accuracy
- attempts
- last_updated

MockAnalytics
- id
- attempt_id
- time_per_question
- accuracy_per_topic (JSON)

add indexes  
Question(concept_id)
MockQuestion(mocktest_id)
StudentAttempt(user_id)
AttemptAnswer(attempt_id)
AttemptAnswer(attempt_id, question_id)
AttemptOption(attempt_answer_id)