# MONGO OPERATOR POC

1. Install the operator

```bash
helm repo add mongodb https://mongodb.github.io/helm-charts
helm install mongo-operator mongodb/community-operator -n mongo-operator --create-namespace
```

2. Apply a Sample Mongo DB Instance

```bash
kubectl apply -f mdbc.yaml
```

3. Check the status of the instance

```bash
kubectl get mdbc
```

4. Get the Credentials

```bash
kubectl get secret/test-mongo-admin-master -o json | jq -r '.data | with_entries(.value |= @base64d)' 
```

Expected Output

```json
{
  "connectionString.standard": "mongodb://master:1234678@test-mongo-0.test-mongo-svc.mongo-operator.svc.cluster.local:27017,test-mongo-1.test-mongo-svc.mongo-operator.svc.cluster.local:27017,test-mongo-2.test-mongo-svc.mongo-operator.svc.cluster.local:27017/admin?replicaSet=test-mongo&ssl=false",
  "connectionString.standardSrv": "mongodb+srv://master:1234678@test-mongo-svc.mongo-operator.svc.cluster.local/admin?replicaSet=test-mongo&ssl=false",
  "password": "1234678",
  "username": "master"
}
```

5. Test if Client is able to connect to the instance

```bash
python3 app.py # Make sure you edit the connection string inside the app.py file
```