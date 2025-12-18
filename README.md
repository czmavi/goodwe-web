# Goodwe Web

## Webserver

Run `python3 -m flask run`

Get inverter detail `http://127.0.0.1:5000/inverter/192.168.20.119` 

## Docker

[https://hub.docker.com/repository/docker/czmavi/goodwe-web](https://hub.docker.com/repository/docker/czmavi/goodwe-web)

### Available Tags

- `latest` - Latest build from main branch
- `x.y.z` - Specific version releases (e.g., `1.0.0`, `1.2.3`)
- `x.y` - Latest patch version for a minor release (e.g., `1.2`)
- `x` - Latest minor version for a major release (e.g., `1`)

### Creating a New Release

To create a new versioned release:

1. Tag the commit with a semantic version:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. The GitHub Action will automatically:
   - Create a GitHub release with release notes
   - Build and push Docker images with version tags (e.g., `1.0.0`, `1.0`, `1`)

Note: The `latest` tag is updated on every push to the main branch, whether from a regular commit or a tagged release.

Example usage:
```bash
docker pull czmavi/goodwe-web:latest
docker pull czmavi/goodwe-web:1.0.0
```
