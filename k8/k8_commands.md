
Copy from pod to local directory.
```
kubectl cp MY_NAMESPACE/POD_NAME:/DIR/FILE_NAME LOCAL_DIR
```

Get the pods in a namespace.
```
kubectl get pods --namespace=MY_NAMESPACE
```

Get into a specific pod *(my case was a deployed project on GCP)*
```
kubectl exec --stdin --tty <POD_NAME> -- /bin/bash
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
