# kopf-example
Simple Kubernetes operator with kopf

Make sure you install kopf and kubernetes client (pip install kopf kubernetes)
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

If you want to be able to modify the custom resource (e.g. change the number of replicas), run the with_update.py operator:

    kopf run with_update.py
    
To run the operator in Kubernetes, build and push a container image with the provided Dockerfile. Next, deploy the operator with:

    kubectl apply -f deploy_operator.yaml
    
**Note:**: before deploying the operator, create a service account that has the requires access rights

Blog post: https://blog.baeke.info/2020/01/26/writing-a-kubernetes-operator-with-kopf/