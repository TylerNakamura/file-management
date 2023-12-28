# File Management

```bash
docker build -t date-adder:latest --build-arg SOURCE_DIR=/Users/tylernakamura/Desktop/src .
docker run -v /Users/tylernakamura/Desktop/src:/app/src date-adder:latest
```
