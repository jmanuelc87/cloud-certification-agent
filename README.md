# Cloud Certification Study Agent

A Cloud certification study agent that helps you to build knowledge for a given cloud certification.

## System Context Diagram

```mermaid
flowchart TD
    User["`**Student**
    [Person]
    A person trying to get a cloud certification`"]


    subgraph CCA[Cloud Certification Agent]
        Guide["`**Guide Agent**
        [Software System]
        An agent capable of helping students to get their certifications`"]

        RAG["`**RAG Agent**
        [Software Sytem]
        Process documents and scrape web pages`"]
    end

    LLM["`**Large Language Model API**
    [External Software System]
    External API`"]

    DB["`**Store**
    [External Software System]
    Stores the embeddings to documents and resources found on internet`"]

    User -- "Access" --> CCA

    CCA -- "ReAct" --> LLM
    Guide -- "Retrieve" --> DB
    RAG -- "Stores" --> DB


    classDef focusSystem fill:#1168bd,stroke:#0b4884,color:#ffffff
    classDef supportingSystem fill:#666,stroke:#0b4884,color:#ffffff
    classDef person fill:#08427b,stroke:#052e56,color:#ffffff

    class User person
    class Guide,RAG focusSystem
    class LLM,DB supportingSystem
```

## System Container Diagram

```mermaid
flowchart LR
    User["`**Student**
    [Person]
    A person trying to get a cloud certification`"]

    subgraph Guide[Guide Agent]
        direction TB

        Router["`**Orquestrator Agent**
        [Container]
        An agent that routes the requests to a more specialized agent`"]

        Mentor["`**Mentor Agent**
        [Container]
        An agent that help students create a learning path`"]

        Teacher["`**Teacher Agent **
        [Container]
        An agent that helps students in their learning process`"]

        Library["`**Library Agent**
        [Container]
        An agent that retrieves specific information from the store and shows the resources to the student`"]

        Simulator["`**Simulator Exam Agent**
        [Container]
        An agent that creates exams to test the student habilities`"]

        Router -- "Routes" --> Mentor
        Router -- "Routes" --> Simulator
        Router -- "Routes" --> Library
        Router -- "Routes" --> Teacher
    end


    subgraph RAG[RAG Agent]
        direction LR

        Seed["`**Seed Agent**
        [Container]
        Creates a list of possible sites that contain information`"]

        Scraper["`**Scraper**
        [Container]
        Scrapes information from the websites in internet`"]

        Extractor["`**Extractor**
        [Container]
        Extracts the information stored in the bucket`"]

        Chunker["`**Chunker**
        [Container]
        Splits the information in maneagable pieces`"]

        Embedding["`**Embedding**
        [Container]
        Creates embeddings from the chunks of information`"]

        Seed -- "Sends" --> Scraper -- "Sends" --> Extractor -- "Send" --> Chunker -- "Sends" --> Embedding
    end

    Internet["`**Internet**
    [External Software System]
    External resource to access for scrape`"]

    DB["`**Store**
    [External Software System]
    Stores the embeddings to documents and resources found on internet`"]

    Bucket["`**Store**
    [External Software System]
    Stores the raw documents`"]

    LLM["`**Large Language Model API**
    [External Software System]
    External API`"]

    User -- "Access" --> Guide
    Guide -- "ReAct" --> LLM
    Seed -- "ReAct" --> LLM

    Library -- "Retrieve" --> DB
    Embedding -- "Store" --> DB
    RAG -- "Scrapes" --> Internet

    Scraper -- "Stores" --> Bucket
    Bucket -- "Retrieves" --> Extractor


    classDef person fill:#08427b,stroke:#052e56,color:#ffffff
    classDef container fill:#1168bd,stroke:#0b4884,color:#ffffff
    classDef supportingSystem fill:#666,stroke:#0b4884,color:#ffffff

    class User person
    class Router,Mentor,Simulator,Library,Teacher,Searcher,Scraper,Seed,Extractor,Chunker,Embedding container
    class LLM,DB,Bucket,Internet supportingSystem
```