# Goodwe Web

## Webserver

Run `python3 -m flask run`

Get inverter detail `http://127.0.0.1:5000/inverter/192.168.20.119` 

## Docker

[https://hub.docker.com/repository/docker/czmavi/goodwe-web](https://hub.docker.com/repository/docker/czmavi/goodwe-web)

### Available Tags

- `x.y.z` - Specific version releases (e.g., `1.0.0`, `1.2.3`)

### Creating a New Release

To create a new versioned release:

1. Create a GitHub release with a semantic version tag (e.g., v1.0.0) through the GitHub UI or GitHub CLI:
   ```bash
   gh release create v1.0.0 --generate-notes
   ```

2. The GitHub Action will automatically:
   - Build and push Docker image with the version tag (e.g., `1.0.0`)

Example usage:
```bash
docker pull czmavi/goodwe-web:1.0.0
```
