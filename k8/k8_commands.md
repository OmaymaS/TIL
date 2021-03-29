
Copy from pod to local directory.
```
kubectl cp MY_NAMESPACE/POD_NAME:/DIR/FILE_NAME LOCAL_DIR
```

Get the pods in a namespace.
```
kubectl get pods --namespace=MY_NAMESPACE
```

Login to a pod *(my case was a deployed project on GCP)*
```
kubectl exec --stdin --tty <POD_NAME> -- /bin/bash
```
