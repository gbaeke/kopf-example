# kopf-example
Simple Kubernetes operator with kopf

Make sure you install kopf (pip install kopf)
Verify you can execute kopf on the command line
Create the demowebs CRD with:

    kubectl create -f crd.yaml
    
Run the operator with (in another terminal):

    kopf run with_create.py
    
Create the custom resource with:

    kubectl create -f demoweb.yaml
    
You can modify demoweb.yaml with a number of replicas and a path to a public git repository that contains an index.html.

Verify that the number of replicas were created:

    kubectl get pods
    
Connect to a pod:

    kubectl port-forward <pod_name> 8080:80
    
Browse to http://localhost:8080 to verify the content is served.
