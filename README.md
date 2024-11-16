# k8s-hpa
Simple cli app for using calculation of horizontal pod autoscaler (HPA) in Kubernetes.

Currently, supports 2 caclulations:
1. Calculate desired replicas
   - Calculate desired replicas when following values are provided:
     - Resource current usage
     - Container resource requested
     - Desired metric
     - Current replicas
2. Calculate container resource requested value
   - Calculate container resource requested value when following values are provided:
     - Current resource usage
     - Desired metric
     - Current replicas
     - Desired replicas

## How to use

- Calculation type and Inputs should be provided in `config.yaml` file.
- Calculation type
  - Calculation desired replicas: 1
  - Calculate container resource requested value: 2
- Inputs
  - Current resource usage
  - Container resource requested
  - Desired metric
  - Current replicas
  - Desired replicas
- In calculation desired replicas,
  - Only desired metric can be `null`
  - All the other values should be provided
  - Current resource usage and container resource requested should in same units
- In calculate container resource requested value,
  - Only requested resource value can be `null`
  - All the other values should be provided
  - Requested resource value will be provided in same units as current resource usage
