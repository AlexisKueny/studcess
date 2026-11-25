# Studcess development plan

## W0: Planning
Goal: define the MVP and plan out the expected deliverables for each week

- Review this plan
- Define MVP (minimal viable product)
- Define the MVP subjects. My proposition are commonly shared first year's bachelor's subject such as **analysis**,**linear algebra**,**intro to programming**,**intro to physics**, **probability and statistics** 
- Define supported languages (english/french etc.)
- Create application mockups
- Find a suitable local or cloud LLM model for the RAG
- Discuss legal contraints (fair use, licensing and copyright), especially for exam papers
- Plan the project milestones across the 4 week period

Done definition: The MVP has been defined and a workload outline for the next 4 weeks has been established.

## W1: Setup
Goal: setup everything to begin development

- Create github repository
- Create nextJS application
- Setup fastAPI backend
- Setup supabase (postgres DB, auth, object storage, vector DB)
- Establish 3 environments (dev,staging,prod)
- Get a cloud LLM API key for the RAG, or running local model with ollama
- Setup CI/CD with github actions (lint + basic tests)
- Initial deployment

Suggestion: use a NextJS starter template to skip much of the secondary steps and start right away with a baseline

Done definition: Everything setup and functional

## W2: Warmup - Python fundamentals "mini-RAG"
Goal: make a tiny RAG specialized in python fundamentals. Should be able to answer user questions, generate exercises and verify user reponses

- Ingest a small amount of varied data: official textbook chapters, exercise pages, sample exams
- Setup basic text/pdf extraction
- Clean and normalization of ingested documents step
- Setup metadata schema
- Setup a basic chunking strategy
- Select an embedding model
- Store and embed the chunks into the vector database following the 2 above strategies
- Design a search engine to retrieve the closest emebeddings
- Setup LLM prompt template (eg. you are a teacher proficient in python fundatementals etc.)
- Test the model
- Create an evaluation set to evaluate the responses
- Gather metrics (latency, etc.)

Done definition: A small python RAG specialized in one topic able to correctly answer user requests as well as evaluation metrics

## W3: Ingestion pipeline
Goal: create a working, reusable pipeline for corpus ingestion.

- Define metadata schema
- Develop pdf and text extraction
    - Find a solution for extracting diagrams and images
- Develop normalization and cleaning step
- Develop the chunking strategy (eg. question and solutions together)
- Confirm the embedding model
- Methods for vector database population
- Setup duplication checking
- Create rules for a metadata tagging strategy
- Determine a processing strategy for handling ingestion jobs (eg. queue)
- Handle deletion and reingestion of an ingested document

Done definition: A working end to end pipeline, tested and no errors

## W4: Data collection 
Goal: setup a core corpus which covers all of the initial launch subjects

- Define the data sources and maintain a register (eg. online textbooks, exercises, published past exams etc)
- Ingest theory
- Ingest exercises
- Ingest past exams
- Verify the final result

Done definition: A base corpus of 5-10 documents of mixed content per subject, expand if it is not sufficient

## W5: Retrieval and RAG core
Goal: establish a strategy for the retrieval step

- Expanded retrieval: embed query, similarity search and apply metadata filters
- Expand the LLM prompt template for all of the use cases
- Handle special cases: "out of scope", prompt injection attacks
- Expand the evaluation set
- Continuously collect metrics

Done definition: Working RAG on the launch subjects. Evaluation metrics collected.

## W6: Backend 
Goal: Integrate the backend to support the application (authentication, routes, error tracking)

- Integrate the RAG into the backend
- Authentication (email + password)
    - Session handling
    - Optional: SSO with OpenID connect or SAML
- Create endpoints for the routes
    - Protect routes with middleware
    - RBAC: user and admin accounts
- LLM use control
    - Rate limiting
    - Prompt injection defense
- Logging and error tracking

Done definition: All RAG features are callable with the API, RBAC is there and working authentication


## W7: Frontend integration
Goal: Build a frontend to support user interaction

- Page design, layout and navigation
- Signup and login pages
- Profile page for the user
- Study plan CRUD
    - Study plan form: Users add exam date, exam description, topics etc to help specify their study plans for the exam they are preparing
    - Users can have multiple ongoing study plans and should easily be able to switch between them
    - Users can update their ongoing study plans by modifying information
    - Users can delete their study plans
- Interactive theory format
    - Styled, easy to read and understand, correctly seperated and classified (not one big blob)
    - Can be saved into pdf format
    - Nice to have: diagrams and pictures inside the theory pages
- Exercise format
    - Interactive UI such as checkboxes for MCQs, text fields for open-ended questions
    - Direct feedback: users will be able to verify their answers and see what they got right or wrong with reasons
- Mock exam format, simulated to ressemble what the real exam could look like. Would come with an "exam mode" to simulate real exam constraints such as a timer
    - Format modelled after the user's specifications
    - Timer for completion, also taken from the user's specifications
    - Feedback post submission: grade + corrections
    - Possibility to try again, generate a new exam
- Chatbot interface, which the user can use to ask questions
- Load and error states

Done definition: There is a user interface for the project

## W8: User uploads
Goal: Support user uploads to help tailor the RAG to their use

- Upload UI for user provided files
- File validation (type,size etc)
- Setup a user/course namespace inside the vector DB
- Status states (queued, processing, ready, failed)
- CRUD for user document management
- Make sure that each user namespace is isolated, no other users can access it

Done definition: Users are able to upload documents, such as their personal notes to their study plans. Ensure that these documents are isolated into their personal namespaces and can't be leaked

## W9: Calendar scheduling
Goal: Populate a calendar with study sessions for the user. Make it as convenient as possible with the user's preferences

- Collect user's time preferences from the profile (eg. desired daily study time, timezone, off days or off hours etc)
- Sync with the user's personal calendar to understand their availabilities.
- Develop an algorithm to:
    - Split the full exam prep material (topic theory + topic exercises) into sensible partitions optimized for the desired daily study period (eg 1-3 hours). Make sure that the split is clean (eg. segment the material per topic and assign each day to a different topic)
    - Optimize the slots to schedule at the best possible times for a user, taking under consideration their availabilities and make common sense scheduling (eg. no study periods during lunch times or at 3 am in the morning)
- Allow users to modify this suggested calendar, add their own events or altogether disregard it if they would like to handle the scheduling themselves

Done definition: Upon study plan creation an in-application calendar is displayed, populated and interactable by the user.

## W10: Progress dashboard
Goal: Create a progress dashboard to track an illustrate the student's performance with the study materials at hand

- Per study plan progress: track number of exercises done, hours spent study and performance in answering the questions. Estimate the student's readiness for an exam based on these metrics
- Overall progress: track the the user's performance across all ongoing study plans. 
- Weak and strong point profiling: setup an algorithm to determine the user's strong and weak points, and display on the study plan's dashboard

Done definition: Working and meaningful dashboard to highlight progress metrics.

## W11: Dynamic study plan readaptation
Goal: Dynamic modification of the study plan, i.e. calendar hours and material to adjust to the student's performance

- Strong point handling: increase the complexity of the future exercises, or remove extra material if the user is at ease with the topic
- Weak point handling: add or modify the upcoming study sessions with extra focus on the student's weak points.
- A small feedback section after every study period can be helpful
- Find a way to make this non intrusive and inform the user

Done definition: Dynamic rewriting of the study plan is functional

## W12: Admin account
Goal create an admin interface for application administrators

- Administrators can view the created user accounts 
- Administrators can consult the list of available subjects
- Administrators can view basic statistics for each user, e.g. how many study plans created per user etc.

Done definition: a working functional interface for admin users

## W13: Scaling and performance
Goal: Understand how the application behaves under load, find the bottlenecks and sacle the application (eg. more users, bigger corpus)

- Define scale goals (number of users, number of chunks)
- Define target metrics: retrieval latency, ingestion latency, error rate, projected cost per user
- Create a test dataset and script to simulate typical user interactions with the application (creating study plans, uploading/downloading documents etc)
- Setup a dashboard inside the administrator account or use a service to visualize these metrics
    - Continuous logging
    - Alerts
    - Queue backlogs
- Work on optimizing each bottleneck

Done definition: Application metrics can be visualized through the admministrator dashboard, the application responds well to scaling.

## W14: Continuous maintenance (throughout project development)
Goal: develop unit tests for continuous test integration and write documentation

- Write unit tests to cover most of the application code and the API routes
- Keep track and address important bugs
- Write a technical guide to describe the technical aspects of the app
- Write a user manual for using the app
- Continuously collect performance metrics

## W15: Project wrapup
Goal: prepare the project for the presentation

- Plan the project demo
- Create the presentation slides
- Gather graphs for visualization of the application metrics