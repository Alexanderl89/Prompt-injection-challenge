FROM ubuntu:22.04

LABEL project="prompt_injection_project"

RUN apt update && apt install -y \
    vim \
    build-essential \
    cmake \
    ninja-build \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /
COPY models/* /models/

WORKDIR /app
COPY main.py requirements.txt sys_prompt.py challenge_instructions.py /app/

RUN pip3 install -r requirements.txt

EXPOSE 7884

CMD ["python3","main.py"]
