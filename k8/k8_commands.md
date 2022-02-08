
- Copy from pod to local directory.

```
kubectl cp MY_NAMESPACE/POD_NAME:/DIR/FILE_NAME LOCAL_DIR
```

- Get the pods in a namespace.

```
kubectl get pods --namespace=MY_NAMESPACE
```

- Get into a specific pod

```
kubectl exec --stdin --tty <POD_NAME> -- /bin/bash
```

## Env variables

List the Pod's container environment variables.

```
kubectl exec <POD_NAME> -- printenv
```

## Secrets

Create a generic secret.

```
kubectl create secret generic [SECRETNAME]] \
    --namespace=[MY_NAMESPACE]]\
    --from-literal=user=xxx\
    --from-literal=password=yyy\
```

Delete secret 

```
delete secret [SECRETNAME]
```

- edit deployment 

```
kubectl set image deployment.v1.apps/nginx-deployment nginx=nginx:1.9.1 --record
kubectl rollout status deployment.v1.apps/nginx-deployment
```