# Project 5: GitOps-Based Kubernetes Application Deployment using ArgoCD

## Project Overview

This project demonstrates a **GitOps workflow** for Kubernetes applications using **ArgoCD**. All deployments follow GitOps principles:

> "No manual kubectl changes in production. All deployments happen via Git repository updates."

## Technologies & Tools

* Docker
* Kubernetes (EKS / Minikube)
* ArgoCD
* GitHub

## Project Objectives

1. Containerize the application.
2. Store Kubernetes manifests in Git.
3. Configure ArgoCD to monitor the Git repository.
4. Enable automatic sync on Git commits.
5. Optional: Helm, Ingress, HPA.

## Project Steps

### 1. Containerization

* Dockerfile created.
* Build image:

```bash
docker build -t my-app:latest .
```

* Push to registry:

```bash
docker push <registry_url>/my-app:latest
```

**Screenshots:** Dockerfile, build output, push output.

### 2. Kubernetes Setup

* EKS cluster created (or Minikube).
* Deployment YAML (`deployment.yaml`) and Service YAML (`service.yaml`) created.
* Apply manifests:

```bash
kubectl apply -f deployment.yaml -n my-app
kubectl apply -f service.yaml -n my-app
```

* Verify pods and services:

```bash
kubectl get pods -n my-app
kubectl get svc -n my-app
```

**Screenshots:** Cluster nodes, pods running, service status (LoadBalancer / NodePort).

### 3. ArgoCD Installation

* Namespace created:

```bash
kubectl create namespace argocd
```

* ArgoCD installed:

```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

* ArgoCD UI accessed and logged in.
* New App created pointing to GitHub repo.
* Sync policy set to **Automatic**.
  **Screenshots:** ArgoCD pods running, login screen, new app creation, app sync status (Healthy / Synced).

### 4. Git-Based Deployment

* Modified app code and pushed to GitHub:

```bash
git add .
git commit -m "Update app"
git push origin main
```

* ArgoCD automatically detected changes and deployed to cluster.
* Verified app in browser:

```bash
http://<external-ip>:5000
```

**Screenshots:** Git commit, ArgoCD auto-sync triggered, browser showing running app.

### 5. Optional Enhancements

* Helm chart deployment (if implemented)
* Ingress configuration (if implemented)
* HPA (Horizontal Pod Autoscaler) (if implemented)
  **Screenshots (if implemented):** Helm deploy, Ingress config, HPA dashboard.

## Screenshots Checklist

1. Dockerfile content
2. Docker image build output
3. Docker push output
4. `kubectl get nodes` (EKS cluster nodes)
5. `kubectl get pods -n my-app` (Pods Running)
6. `kubectl get svc -n my-app` (Service status – LoadBalancer / NodePort)
7. `kubectl get pods -n argocd` (ArgoCD pods running)
8. ArgoCD UI login screen
9. ArgoCD New App creation screen
10. ArgoCD App sync status (Healthy / Synced)
11. Git commit of app changes
12. ArgoCD dashboard showing auto-sync triggered
13. Browser showing running app (`http://<external-ip>:5000`)
14. Optional: Helm deployment, Ingress config, HPA dashboard

## GitOps Flow Diagram

![GitOps Flow](./images/gitops_nodeport_diagram.png)

> Flow: GitHub → ArgoCD → EKS → Deployment & NodePort Service → Browser

## Conclusion

* Complete GitOps workflow implemented successfully.
* CI/CD pipeline is automated: Git commit → ArgoCD auto-sync → Deployment → Browser access.
* Project requirements fully met, including containerization, Kubernetes deployment, ArgoCD setup, and automatic Git-based deployment.

## Deliverables

1. Dockerfile
2. Kubernetes YAML files (`deployment.yaml`, `service.yaml`)
3. ArgoCD configuration (app manifests, Git repo link)
4. GitHub repository link
5. Architecture diagram
6. Screenshots as mentioned in the project requirements
