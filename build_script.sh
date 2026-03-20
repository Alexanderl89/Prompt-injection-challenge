#!/bin/bash
IMAGE_NAME="prompt_injection_challenge_i"
CONTAINER_NAME="prompt_injection_challenge"
INTERNAL_PORT=7884
EXTERNAL_PORT=7884

#echo "[*] Prune cache"
#docker builder prune --filter "label=build_id=prompt_injection_project"

echo "[*] Stop and remove existing container"
docker stop $CONTAINER_NAME 2>/dev/null || true
docker rm $CONTAINER_NAME 2>/dev/null || true

echo "[*] Removing existing image"
docker rmi $IMAGE_NAME 2>/dev/null || true

echo "[*] Building image"
docker build -t $IMAGE_NAME .

if [ $? -eq 0 ]; then
    echo "[+] Build successful!"
    docker run -d --name $CONTAINER_NAME -p $EXTERNAL_PORT:$INTERNAL_PORT $IMAGE_NAME

    if [ $? -eq 0 ]; then
        echo "[+] Container started at: http://127.0.0.1:$EXTERNAL_PORT"
    else
        echo "[-] Container failed to start"

    fi
else
    echo "[-] Build failed!"
fi