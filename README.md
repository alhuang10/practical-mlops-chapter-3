# Mostly Review

Creating and pushing a Docker container to registry:
```
docker login --username=alhuang1000 --password-stdin docker.io
docker build -t alhuang1000:testingrepo .
docker tag alhuang1000:testingrepo alhuang1000/testingrepo
docker push alhuang1000/testingrepo
```

Running a Container:

```
docker run -rm -it -d alhuang1000:testingrepo

# Starting an interactive bash session
docker exec -it [CONTAINER_ID] bash

# Running a single command
docker exec [CONTAINER_ID] tail /var/log/apt/history.log
```

Linting a Dockerfile with hadolint:
```
docker run --rm -i hadolint/hadolint < Dockerfile
```

- A new layer gets created with every RUN instruction so it's preferable to use a single line to install man dependencies (via &&). This results in a smaller container. 

- Can use the command-line tool **grype** to look for vulnerabilities in dependencies.


Building the Boston Housing Prediction Flask App:
```
docker build -t flask-predict-image .

# Go to http://localhost:5000 to see the home page or run "curl http://localhost:5000"
docker run -p 5000:5000 -d --name flask-predict flask-predict-image

# Make a sample prediction
./make_predict
```


# Edge Devices

- Installing TPU runtime to experiment with models that can be deployed on devices from coral.ai, e.g. image classification on the USB Accelerator.
- Can find Tensorflow models on TensorFlow Hub, model must match specifications on the TPU device.