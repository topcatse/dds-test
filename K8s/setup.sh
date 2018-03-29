minikube start

eval $(minikube docker-env)

pushd server && docker build -rm --no-cache -t server-image . && popd
pushd device && docker build -rm --no-cache -t device-image . && popd

kubectl run bw-minikube --image=gcr.io/google_containers/echoserver:1.4 --port=8080
kubectl expose deployment hello-minikube --type=NodePort



kubectl delete deployments --all


